import asyncio

import discord
from discord import VoiceClient, ClientException
from discord.ext import commands

from main import intents
from .join import join_exec
from .ping import ping_exec
from .play import play_exec
from .quit import quit_exec

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command(name='quit', help='To make the bot leave the voice channel')
async def leave(ctx):
    await quit_exec(ctx)


@bot.command(name='play', help='To play song')
async def play(ctx):
    await play_exec(ctx)


@bot.command()
async def stop(ctx):
    # noinspection PyTypeChecker
    voice_client: VoiceClient = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice_client.is_playing():
        voice_client.stop()
        await voice_client.disconnect()


@bot.command(name='ping', help='Pong')
async def ping(ctx):
    await ping_exec(ctx)
