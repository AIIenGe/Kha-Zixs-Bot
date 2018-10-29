import discord
import requests
import urllib.request, json
import urllib3

urllib3.disable_warnings()
from collections import defaultdict
import operator
import requests
from ast import literal_eval

client = discord.Client()


@client.event
async def on_ready():
    print(f"We are logged in as {client.user}")


input = ""


@client.event
async def on_message(message):  # event that happens per any message.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if "!champion" in message.content:
        input = message.content.replace("!champion ", "").split()[0]
        role = message.content.replace("!champion ", "").split()[1]
        output = getChampion(input, role)
        for x in output:
            await client.send_message(message.channel, x, tts=True)


def getChampion(input, role):
    url = 'http://api.champion.gg/champion/' + input + '/matchup?api_key=d143ded682d41d1e3ebe173d0b327e46'
    response = requests.get(url, verify=True)
    data = response.json();
    result = []

    for item in data:
        if (item.get('role') == role):
            for x in item.get("matchups"):

                result.append(x)

    print(result)
    # sorted_d = sorted(result.items(), key=operator.itemgetter(0))
    win = 0;
    resultPrint = []
    for x in sorted(result, key=lambda i: (i['winRate'], i['games']), reverse=True):
        if (x.get('winRate') > 50):
            str = x.get('key'), x.get('winRate'), x.get('games')
            resultPrint.append(str)
    return resultPrint

client.run("NTA0Nzg4NjA3NDQyMjIzMTM0.DrKZBw.gYtkzt_4qFZDOf2Id1OQ_5th3dk")
