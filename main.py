import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)
testServer = [1004947709238718564]
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

@bot.slach_command(guild_ids=testServer, name=['commands', 'cmds'])
async def cmds(ctx):
    await ctx.respond("Here are the commands:")
    await ctx.respond("/hello - Says Hello")
    await ctx.respond("/ping - Says Hey, are you there?")
    await ctx.respond("/test *args* - Repeats args back to you in the server")

@bot.command(guild_ids=[1004947709238718564], name='test')
async def test(ctx,arg):
    await ctx.send(arg)


bot.run(os.environ.get('DISCORD_TOKEN'))