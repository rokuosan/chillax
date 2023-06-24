from discord.ext.commands import Context


async def ping_exec(ctx: Context):
    await ctx.reply("Pong!")

