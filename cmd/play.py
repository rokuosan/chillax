import discord.ext


async def play_exec(ctx: discord.ext.commands.Context, url):
    try:
        await ctx.send("Sorry, not implemented.")
    except Exception as _:
        await ctx.send("The bot is not connected to a voice channel.")
