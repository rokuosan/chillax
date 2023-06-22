async def ping(ctx):
    print(type(ctx))
    await ctx.send('pong')
