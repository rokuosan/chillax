import discord.ext
from discord import ClientException


async def play_exec(ctx: discord.ext.commands.bot.Context):
    try:
        server = ctx.message.guild
        vc = server.voice_client

        async with ctx.typing():
            fn = "sounds/music.mp3"
            pcm = discord.FFmpegPCMAudio(source=fn)
            audio = discord.PCMVolumeTransformer(pcm, volume=0.08)
            vc.play(audio)
        await ctx.send("再生を開始します")
    except (ClientException, TypeError):
        await ctx.send("再生に失敗しました。")
    except Exception:
        await ctx.send("VCに接続してからコマンドを実行してください")

