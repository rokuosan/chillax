import discord.ext.commands


async def join_exec(ctx: discord.ext.commands.Context):
    if not ctx.message.author.voice:
        await ctx.send("ボイスチャンネルに接続してからコマンドを実行してください")
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()
