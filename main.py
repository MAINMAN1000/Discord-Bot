import discord
from discord.ext import commands
import sqlite3

# Create intents
intents = discord.Intents.default()
intents.message_content = True

# Create the bot instance
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

# Import your commands from command.py
import command  # Import here so it has access to 'bot'
command.setup(bot)  # Call setup after importing

# Run the bot
bot.run('MTI2MTE0MzI1OTg0MTk1Mzg0Mw.Gz-iMx.m3YOnORu-uhD6v195DfnRvNHRvrDMrSH2hfEl8')  