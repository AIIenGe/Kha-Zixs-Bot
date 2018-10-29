import discord
#print(discord.__version__)  # check to make sure at least once you're on the right version!

client = discord.Client()

@client.event
async def on_ready():
    print(f"We are logged in as {client.user}")

@client.event
async def on_message(message):  # event that happens per any message.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if "hello" in message.content:
        await client.send_message(message.channel, 'Goodbye', tts=True)


client.run("NTA0Nzg4NjA3NDQyMjIzMTM0.DrKZBw.gYtkzt_4qFZDOf2Id1OQ_5th3dk")


#champion.gg
import urllib3
urllib3.disable_warnings()
'''
http = urllib3.PoolManager()
heroes = http.request('GET', 'http://api.champion.gg/champion/annie/matchup?api_key=d143ded682d41d1e3ebe173d0b327e46')
heroes_dict = json.loads(heroes.data.decode('UTF-8'))
print(heroes_dict)
for hero in heroes_dict:
    print(hero['localized_name'])
'''

import requests

url = 'http://api.champion.gg/champion/annie/matchup?api_key=d143ded682d41d1e3ebe173d0b327e46'
response = requests.get(url, verify=True)
data = response.json();
for c in data['role']['matchups']:
    print(c['games'], c['key'])

