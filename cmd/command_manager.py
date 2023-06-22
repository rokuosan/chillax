import discord
from discord.ext import commands

from main import intents, DataSource, ffmpeg_opt
from .ping import ping

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='play', help='To play song')
async def play(ctx, url):
    try:
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await DataSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename,
                                                      options=f"-af volume=-20dB -y"))
        await ctx.send('**Now playing:** {}'.format(filename))
    except Exception as _:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")


@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        try:
            await voice_client.stop()
        except Exception as _:
            print('Stopped a music by ' + ctx.message.author.name)
    else:
        await ctx.send("The bot is not playing anything at the moment.")
