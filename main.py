import discord
import os

client = discord.Client()


@client.event
async def onReady():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.author.name == "mikrowil":
        await message.channel.send("Yea, this guy knows what he's saying")


client.run('ODYwMDk0Mzk3MjU2MTcxNTIw.YN2PVA.ytLXXewA8Mjy-aDlVhfyEQUGhGo')
