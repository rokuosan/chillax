import discord.ext.commands


async def quit_exec(ctx: discord.ext.commands.Context):
    voice_client = ctx.channel.guild.voice_client
    if voice_client.client.is_ready():
        await voice_client.disconnect(force=True)
    else:
        await ctx.send("The bot is not connected to a voice channel.")