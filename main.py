import discord
from discord.ext import commands
import os
import dotenv

dotenv.load_dotenv() 
token = str(os.getenv('TOKEN')) 
intents = discord.Intents().all()
client = discord.Client(intents=intents)
owners = [375797651486015488, ]
bot = discord.Bot(intents=intents, owner_ids = set(owners))
@bot.event 
async def on_ready():
    # eascii() 
    print(f'\n{bot.user} turned on the amp!') 
    botactivity = discord.Activity(type=discord.ActivityType.listening, name="/music commands")
    await bot.change_presence(activity=botactivity, status=discord.Status.online)

cogs_list = [
    'music'
    
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')
bot.run(token)