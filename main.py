import os
import discord
from azure.cognitiveservices.search.imagesearch import ImageSearchClient
from msrest.authentication import CognitiveServicesCredentials
import json
import os 
from pprint import pprint
import requests
import random
import bingS
import backup

from dotenv import load_dotenv

load_dotenv()
discordKEY = os.environ.get('DISCORD_API_KEY')

client = discord.Client()
  

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
        return


  elif message.content.lower().startswith('bear'):
 
    try:
          msg = message.content[5:]
          if message.content[5:] == 'hi':
            await message.channel.send('Hello!')
          elif message.content[5:] == 'su':
            if str(message.author.id) == str(os.environ.get('SPECIAL_USER')):
              str2 = ''
              while str2 != 'exit':
                  str2 = input('> ')
                  await message.channel.send(str2)
            else:
              await message.channel.send('you not a cantaloupe!')
          
          elif msg == "help":
            await message.channel.send("go help yourself loafer!")
          
          elif msg == "i love you":
            await message.channel.send('I love you too ' + message.author.mention + '!')
          
          elif msg == "i hate you":
            await message.channel.send("I don't like you either " + message.author.mention + "! >:(")
          
          elif "who is tg" in msg:
            await message.channel.send("Ummmm I think it is:")
            query2 = "tennis girl"
                  
            content_url2 = bingS.bingSearch(query2)
            await message.channel.send(content_url2)
          
          # elif (word in message.content[5:] for word in words):
          #   for x in range (0, len(words)):
          #      if (message.content[5:] == words[x]):
          #         await message.channel.send("blacklisted")

          else:
            content_url = bingS.bingSearch(message.content[5:])
            print(message.content[5:])
            await message.channel.send(content_url)

    except:

        await message.channel.send('1000 imgs have passed')
        await message.channel.send('The bear is so sorry that this happened! 😭')
        await message.channel.send('So here is a backup IMG of ' + message.content[5:] + ':')
        await message.channel.send(backup.backup(message.content[5:]))
   
      

client.run(discordKEY)
