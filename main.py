# import os
#
# import discord
# from dotenv import load_dotenv
#
# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')
#
# client = discord.Client()
#
# @client.event
# async def on_ready():
#     guild = discord.utils.get(client.guilds, name=GUILD)
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )
#
# client.run(TOKEN)

#This is a decorator implementation of the above
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.slash_command(guild_ids=[1004947709238718564])
async def hello(ctx):
    await ctx.respond("Hello!")

@bot.slash_command(guild_ids=[1004947709238718564])
async def ping(ctx):
    await ctx.respond("Hey, are you there?")

@bot.command(guild_ids=[1004947709238718564], name='test')
async def test(ctx,arg):
    await ctx.send(arg)

bot.run(os.environ.get('DISCORD_TOKEN'))