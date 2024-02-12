import discord
import asyncio
import os
import json
import datetime

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

def save_config(token, prefix, command):
    config = {
        "token": token,
        "prefix": prefix,
        "command": command
    }
    with open("config.json", "w") as f:
        json.dump(config, f)

def load_config():
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            config = json.load(f)
            return config["token"], config["prefix"], config["command"]
    else:
        token = input("Enter your discord token: ")
        prefix = input("Enter the prefix for the command: ")
        command = input("Enter the command: ")
        save_config(token, prefix, command)
        return token, prefix, command

token, prefix, command = load_config()

async def delete_messages(channel):
    async for msg in channel.history(limit=None):
        if msg.author == client.user and not msg.type == discord.MessageType.pins_add:
            try:
                await msg.delete()
                print(f"Deleted message: {msg.content} (ID: {msg.id})")
               # await asyncio.sleep(3) # Remove the "#" in the beginning to add a cooldown
            except discord.Forbidden:
                pass
            except discord.HTTPException as e:
                if e.status == 429:
                    await delete_messages(channel)
                else:
                    raise

@client.event
async def on_ready():
    print("Message Remover is ready")
    print("You have set the command to: " + prefix + command)

@client.event
async def on_message(message):
    if message.author == client.user and message.content.startswith(prefix + command):
        if isinstance(message.channel, discord.DMChannel):
            await delete_messages(message.channel)

        elif isinstance(message.channel, discord.TextChannel) or isinstance(message.channel, discord.GroupChannel):
            await delete_messages(message.channel)


client.run(token, bot=False)
