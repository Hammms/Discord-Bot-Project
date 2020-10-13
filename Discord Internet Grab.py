#packages used:
# discord.py | Beautiful Soup 4 | Google  | re | requests 

import discord
import googlesearch
import re
import requests
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
      return
    
  if message.content.endswith('stats'):
      try: 
        from googlesearch import search 
      except ImportError:  
            print("No module named 'google' found")

      query = message.content
      query = query.replace('jeff','')
      query = query.replace('stats','')
      print(query)
      for j in search(query, tld="co.in", num=1, stop=1, pause=2): # no reason for this to be a for loop
        print('suceess')
        


      res = requests.get(j)
      #Unpacks
      sauce = BeautifulSoup(res.text, 'lxml')
      print(sauce.select('.infobox-nested')[28])
      #Web Scraping specfic class on the osrs wiki website to pull information about each weapon
      x = [5,6,7,8,9,15,16,17,18,19,25,26,27,28]
      stats = []
      for i in range(0,14):
        getstats = str(sauce.select('.infobox-nested')[x[i]].getText())
        stats.insert(i,getstats)
      print(stats)
      output = (f'stab: {stats[0]} Slash: {stats[1]} Crush: {stats[2]} Magic: {stats[3]} Ranged: {stats[4]}  \n stab: {stats[5]} Slash: {stats[6]} Crush: {stats[7]} Magic: {stats[8]} Ranged: {stats[9]}  \n Strength Bonus: {stats[10]} Ranged Strength: {stats[11]} Magic Strength: {stats[12]}  Prayer Strength: {stats[13]}')     
      await message.channel.send(output)
      # await message.channel.send(output)
      return

  if message.content.startswith('jeff'):
    try: 
      from googlesearch import search 
    except ImportError:  
          print("No module named 'google' found") 

    query = message.content
    query = query.replace('jeff','')
    print(query)
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        print('suceess')
        await message.channel.send(j)
client.run('this is where you place your from the discord dev site to run your bot.')

#Slash: {stats[1]} Crush: {stats[2]} Magic: {stats[3]} Ranged: {stats[4]}

#on message for reciving information
#on ready to do something with that information 
#triggers on every message 