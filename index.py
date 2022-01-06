# bot.py
import os

import discord
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
statusChannel = 738439111412809730
msgCounter = 0

# vvv Change these variables if needed vvv
numMessages = 30
time = 60 #seconds
channelID = 865211750081101844
roleID = '697149372626108542'
# ^^^ Change these variables if needed ^^^

def getTimeMin():
    timeNow = datetime.now()
    h = int(timeNow.strftime('%H'))
    m = int(timeNow.strftime('%M'))
    return (h * 60) + m

lastTime = getTimeMin()

async def countMessages():
    global msgCounter
    if (msgCounter >= numMessages):
        await client.get_channel(channelID).send('<@&' + roleID + '>')
        msgCounter = 0

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='DutchPilotGirls YouTube Channel'))
    await client.get_channel(statusChannel).send(':green_circle: Bot has started.')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    global msgCounter
    msgCounter += 1

    time = getTimeMin()

    if (time > lastTime):
        await countMessages()

    print('Current Time =', time)
    # await msg.channel.send(time)

client.run(TOKEN)