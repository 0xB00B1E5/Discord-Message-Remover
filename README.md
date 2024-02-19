# Discord Message Remover

This Python script allows you to delete your own messages in Discord

## Installation
1. Clone or download this repository.
2. Install the required dependencies by running the following command:
   ```bash
   pip install discord.py==1.7.3 requests asyncio

## Usage
1. Run the script.
2. The script will start monitoring your Discord channels.
3. To trigger the message deletion, send a message that starts with the specified prefix followed by the command you set during configuration.
4. The script will then start deleting your messages in the same channel where the trigger message was sent.

## Configuration
- `token`: Your Discord token.
- `prefix`: The prefix for the command that triggers message deletion.
- `command`: The command that triggers message deletion.

## Notes
- Make sure to keep your Discord token secure and do not share it publicly.
- By default, there's no cooldown between message deletions. You can enable a cooldown by uncommenting the line with `await asyncio.sleep(3)`.
- Be cautious when using this script
