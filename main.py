# connecting to discord

import os
import discord
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


analyzer = SentimentIntensityAnalyzer()


def sentiment_analyzer_scores(text):
    score = analyzer.polarity_scores(text)
    lb = score['compound']
    if lb >= 0.05:
        return 'bloomer'
    elif (lb > -0.05) and (lb < 0.05):
        return 'neutral'
    else:
        return 'doomer'


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    sentiment = sentiment_analyzer_scores(message.content)
    print('sentiment: ' + str(sentiment))
    await message.channel.send('You\'ve been assigned ' + str(sentiment))


client.run(TOKEN)