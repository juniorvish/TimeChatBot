import discord
from discord.ext import commands
import pytz
from datetime import datetime
import config

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if checkTimeRestriction():
        await handleMessageEvent(message)
    else:
        await message.delete()
        await message.channel.send(f"{message.author.mention}, you can only chat between 8PM IST and 10PM IST.", delete_after=5)

    await bot.process_commands(message)

def checkTimeRestriction():
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    allowed_start_time = now.replace(hour=20, minute=0, second=0, microsecond=0)
    allowed_end_time = now.replace(hour=22, minute=0, second=0, microsecond=0)

    return allowed_start_time <= now <= allowed_end_time

async def handleMessageEvent(message):
    if message.content.startswith("!"):
        return

    await message.channel.send(f"{message.author.mention}: {message.content}")

bot.run(config.TOKEN)