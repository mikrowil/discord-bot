import discord
import os
from scrapy.crawler import CrawlerProcess
from scrappyScraper import IGNNewsUpdater
from scrappyScraper import getContents

client = discord.Client()

process = CrawlerProcess(settings={
    'FEED': {
        "items.json": {"format": "json"},
    }
})
process.crawl(IGNNewsUpdater)
process.start()

@client.event
async def onReady():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello bot'):

        await message.channel.send('Hello!')

        return

    if message.content.startswith('$ign news'):
        process.crawl(IGNNewsUpdater)
        myArr = getContents()

        for item in myArr:
            await message.channel.send(item['link'])

        return


client.run(os.environ['BOTCODE'])
