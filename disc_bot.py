import discord
import random
import requests
import json
import os

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

sad_response = [
    "Well.. sucks.",
    "Nobody's perfect.",
    "Nice.",
    "Nobody cares.",
    ]

happy_words = ["happy", "excited", "ecstatic", "hyped"]

happy_response = [
    "Feel free to share the love.",
    "I wanna be that guy.",
    "Must be nice.",

]
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('!'):
        await message.channel.send('I see how it is, done with me already, huh?')

    if msg.startswith('@'):
        await message.channel.send("Leave em alone why don't ya!")

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(sad_response))

    if any(word in msg for word in happy_words):
        await message.channel.send(random.choice(happy_response))


client.run(os.getenv('TOKEN'))
