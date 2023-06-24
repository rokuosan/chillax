import asyncio
import time

import discord.ext
from discord import VoiceChannel, ClientException
from discord.utils import get

from cmd import command_manager


def repeat(voice):
    name = "sounds/music.mp3"
    pcm = discord.FFmpegPCMAudio(source=name)
    audio = discord.PCMVolumeTransformer(pcm, volume=0.08)

    if not voice.is_playing:
        time.sleep(3)
        voice.play(audio, after=lambda e: repeat(voice))


async def play_exec(ctx: discord.ext.commands.bot.Context):
    voice_channel = ctx.author.voice.channel
    if voice_channel:
        voice_client = await voice_channel.connect()
        try:
            while True:
                pcm = discord.FFmpegPCMAudio(source="sounds/music.mp3")
                audio = discord.PCMVolumeTransformer(pcm, volume=0.08)
                voice_client.play(audio)
                # 再生が終了するまで待つ
                while voice_client.is_playing():
                    await asyncio.sleep(1)
        except ClientException:
            return
