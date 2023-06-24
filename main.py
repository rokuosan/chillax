import asyncio
import os
import sys

import discord
import yt_dlp
from dotenv import load_dotenv

from cmd import command_manager

# Read .env
load_dotenv()

# Check discord token
DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None or DISCORD_TOKEN == "":
    print("Failed to load discord token!\nPlease set discord token to your .env file.")
    sys.exit(1)

# Init discord components
intents: discord.Intents = discord.Intents().all()
client: discord.Client = discord.Client(intents=intents)


def main():
    global DISCORD_TOKEN

    command_manager.bot.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()
