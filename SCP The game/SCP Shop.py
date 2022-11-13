import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def info(ctx):
    await ctx.send('Надо добавить инфу о игре')

@bot.command()
async def shop(ctx, obj):
    if obj == 'info':
        await ctx.send('Надо добавить инфу')

    if obj == 'list':
        await ctx.send('Надо добавить list')

    if obj == 'link':
        await ctx.send('Донатить по этому номеру +37368458507')
  

bot.run('ODgwMTYyODAyODM5NDg2NTA0.YSaRfA.d4zKGrxdqmgTQ5Os2ls-KXL4bB4')
