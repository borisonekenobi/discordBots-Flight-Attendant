# bot.py
import os
import asyncio

import discord
from dotenv import load_dotenv
from datetime import datetime
from config import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
statusChannel = 738439111412809730
msgCounter = 0



async def countMessages():
    while True:
        global msgCounter
        if (msgCounter >= numMessages):
            print('Messages exceeded ' + str(numMessages) + ' in the last ' + str(time) + ' seconds!')
            await client.get_channel(channelID).send('<@&' + roleID + '>')
        msgCounter = 0

        await asyncio.sleep(time)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='DutchPilotGirls YouTube Channel'))
    await client.get_channel(statusChannel).send(':green_circle: Bot has started.')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.guild.id == serverID:
        global msgCounter
        msgCounter += 1

def main():
    asyncio.get_event_loop().create_task(countMessages())

    client.run(TOKEN)

main()