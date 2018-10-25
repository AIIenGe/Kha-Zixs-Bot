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
        await client.send_message(message.channel, 'hello', tts=True)


client.run("NTA0Nzg4NjA3NDQyMjIzMTM0.DrKZBw.gYtkzt_4qFZDOf2Id1OQ_5th3dk")
