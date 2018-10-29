import discord
import urllib.request, json
import urllib3
urllib3.disable_warnings()
from collections import defaultdict
import operator
import requests
from ast import literal_eval

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


url = 'http://api.champion.gg/champion/annie/matchup?api_key=d143ded682d41d1e3ebe173d0b327e46'
response = requests.get(url, verify=True)
data = response.json();
result = []
for item in data:
    if (item.get('role') == 'Middle'):
       for x in item.get("matchups"):
           result.append(x)

#sorted_d = sorted(result.items(), key=operator.itemgetter(0))

for x in sorted(result, key = lambda i: i['winRate'], reverse=True):
    print(x.get('key'), x.get('winRate'), x.get('games'))

