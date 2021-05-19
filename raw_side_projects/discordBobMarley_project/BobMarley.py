import discord
from discord.ext import commands
import logging
from pathlib import Path
import json


cwd = Path(__file__).parent[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

#Defining a few things
secret_file = json.load(open(cwd+'/bot_config/secrets.json'))
bot = commands.bot(command_prefix='#',case_insensitive=True)
bot.config_token = secret_file['token']
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is #-----")
