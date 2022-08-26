import os
import discord
import python_weather
import asyncio
import datetime

# class MyView(discord.ui.View):
#     @discord.ui.button(label="Click me!", style=discord.ButtonStyle.success)
#     async def button_callback(self, button, interaction):
#         await interaction.response.send_message("You clicked the button!")
#intents = discord.Intents.all()
intents = discord.Intents.default()
intents.members = True
bot = discord.Bot(intents=intents)
testServer = [1004947709238718564]
def getguilds():
    i =[]
    for g in bot.guilds:
        i.append(g.id)
    return i
def hrole(u,rid):
    pass

# def getroles():
#     i = []
#     for r in :
#         i.append(r.id)
#     return i    

async def getweather(c):
    async with python_weather.Client() as client:
        weather = await client.get(c)
        forecasts = {}
        for forecast in weather.forecasts:
            forecasts.update({forecast.date:forecast.average_temperature})
    return forecasts


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.send("Hey, welcome to the test server.")

@bot.slash_command(guild_ids=[1004947709238718564])
async def hello(ctx):
    await ctx.respond("Hello!")

# @bot.slash_command(guild_ids=[1004947709238718564])
# async def react(ctx):
#     if ctx.author.id != 177746970956267520:
#         return await ctx.respond("You are not the owner")
#     x = await ctx.respond("smth",view=MyView())


@bot.slash_command(guild_ids=[1004947709238718564])
async def ping(ctx):
    await ctx.respond("Hey, are you there?")

@bot.command(guild_ids=[1004947709238718564],name="weather")
async def whatstheweather(ctx:discord.ApplicationContext,country:discord.Option(str)):
    w = await getweather(country)
    t = datetime.date.today()
    temp = w[t]
    await ctx.respond(f"Today's temperature is {temp} degrees")

@bot.slash_command(guild_ids=testServer, name='commands')
async def cmds(ctx):
    await ctx.respond("Here are the commands:")
    await ctx.respond("/hello - Says Hello")
    await ctx.respond("/ping - Says Hey, are you there?")
    await ctx.respond("/test *args* - Repeats args back to you in the server")

# role_ids = getroles()
# class RoleButton(discord.ui.Button):
#     def __init__(self,role: discord.Role):
#         super().__init__(
#             label=role.name,
#             style=discord.ButtonStyle.primary,
#             custom_id=str(role.id),
#         )



async def callback(self, interaction: discord.Interaction):
    user = interaction.user
    role = interaction.guild_get_role(int(self.custom_id))


@bot.command(guild_ids=[1004947709238718564], name='test')
async def test(ctx,arg):
    await ctx.send(arg)


bot.run(os.environ.get('DISCORD_TOKEN'))
#bot.run("MTAwNDk0Mjg1Mjc5NjczMTM5Mg.G635uG.RurD2SbVWBw9CwvMQ35mN8ot5xwPcNW0Mm_6lI")