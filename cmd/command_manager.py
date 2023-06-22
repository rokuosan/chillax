from discord.ext import commands

from main import intents
from .ping import ping


bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command(name='ping')
async def command_ping(ctx):
    await ping(ctx)

