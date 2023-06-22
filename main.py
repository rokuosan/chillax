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

ytdl_opt = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_opt = {
    'options': '-vn -volume=-6dB'
}

ytdl = yt_dlp.YoutubeDL(ytdl_opt)


class DataSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.01):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename


def main():
    global DISCORD_TOKEN

    command_manager.bot.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()
