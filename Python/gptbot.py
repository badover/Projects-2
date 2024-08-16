import discord
from discord.ext import commands
import random
import time
import cat
import asyncpraw
import openai


intents = discord.Intents.all()

intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
openai.api_key=''

@bot.event
async def on_ready():
     while True:
          await bot.change_presence(status=discord.Status.online, activity=discord.Game("ZE WARUDO OVER HEAVEN!"))

@bot.command(name='g')
async def cont(ctx: commands.context, *,args):
    result = str(args)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=result,
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=['You']
    )
    await  ctx.send(embed=discord.Embed(title=f'{result}', description=response['choices'][0]['text']))

@bot.command()
async def info(ctx):
    await ctx.send('Bot created for server: ')

@bot.command()
async def rkott(ctx):
    emb = discord.Embed(title = "Your pic", colour=discord.Colour.yellow())
    emb.set_image(url = "https://www.cat-gpt.com/")
    await ctx.send(embed = emb)


bot.run('')


