import discord
import json
import os

client = discord.Client()

def get_meme():
    response = request.get
    ("https://meme-api.herokuapp.com/gimme")
    json_data = json.loads(response.text)


@client.event
async def on_ready():
     print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('audi'):
        await message.channel.send('Get timed out nerd!')



#discord token goes here
client.run('ODM3Mzg0MDUxMzIwNDIyNDEw.YIrwqw.jGpg_zx_-LENjUhCcPY2s7a8qJo')