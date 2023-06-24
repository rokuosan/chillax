import discord
from discord.ext import commands

from main import intents
from .join import join_exec
from .play import play_exec
from .quit import quit_exec

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    await join_exec(ctx)


@bot.command(name='quit', help='To make the bot leave the voice channel')
async def leave(ctx):
    await quit_exec(ctx)


@bot.command(name='play', help='To play song')
async def play(ctx, url):
    await play_exec(ctx, url)
