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
    await member.send("Hey, welcome to the test server.")

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