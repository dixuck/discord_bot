import os
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from dotenv import load_dotenv
from gpt import get_context, write_to_json, get_response

# initializing
load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

#commands
@bot.command() 
async def help(ctx):
    embed = discord.Embed(
        colour=discord.Colour.purple()
    )
    embed.set_author(name='Че надо')
    embed.add_field(name='?', value='↓ далбоеб')
    embed.set_footer(text=f'Requested by <@{ctx.author}>', icon_url=ctx.author.avatar)

    await ctx.send(embed=embed)

@bot.command() 
async def hello(ctx: Context):
    author = ctx.message.author 
    data = []
    async for message in ctx.history(limit=50):
        if message.author == ctx.author:
            data.append(message.content)
    print(data)
    await ctx.send(f'ya dolboeb, {author.mention}!')

@bot.command()
async def check(ctx):
    data = []
    async for message in ctx.history(limit=50):
        if message.author == ctx.author:
            data.append(message.content)
    await ctx.send(f'history:\n{data}')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}ms')

@bot.command()
async def chat(ctx, *, msg=None):
    if msg is not None:
        context = get_context('context.json')
        context['messages'].append({'role': 'user', 'content': msg})
        response = await get_response(context['messages'])
        await ctx.reply(response)
        context['messages'].append({'role': 'assistant', 'content': response})
        write_to_json(context, 'context.json')
    else:
        await ctx.reply('Хули тут пусто')

        
# events
# @bot.event
# async def on_command_error(ctx, error):
#     await ctx.send(f'Error {error}. Type $help')

# run
if __name__ == '__main__':
    bot.run(os.environ.get('TOKEN'))
