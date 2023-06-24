import asyncio

import discord.ext.commands


async def join_exec(ctx: discord.ext.commands.Context):
    try:
        vc = ctx.author.voice.channel

        await vc.connect(timeout=10, reconnect=False)
    except discord.ClientException:
        await ctx.reply("VCに接続してから再度コマンドを実行してください。")
    except asyncio.TimeoutError:
        await ctx.reply("VCへの接続がタイムアウトしました。")
