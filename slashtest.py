import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix=['!'])

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[1004947709238718564])
async def hello(ctx):
    await ctx.respond("Hello!")

@bot.slash_command(guild_ids=[1004947709238718564])
async def ping(ctx):
    await ctx.respond("Hey, are you there?")

@bot.command(guild_ids=[1004947709238718564], name='test')
async def test(ctx,arg):
    await ctx.send(arg)


bot.run("MTAwNDk0Mjg1Mjc5NjczMTM5Mg.G1GvYq.6tU9fzRf8xRFSSpP7ROCj5urbDI3Jtqcj2CxCM")
