import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Merhaba!")
    elif message.content.startswith('$görüşürüz'):
        await message.channel.send("Görüşürüz!")
    elif message.content.startswith('$nasılsın'):
        await message.channel.send("Ben iyiyim sen?")
    elif message.content.startswith('bende iyiyim'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$senin adın ne'):
        await message.channel.send("Benim adım GreenCreeper ve ben bir discord botuyum!")
    elif message.content.startswith('$'):
        await message.channel.send("Bu komutu anlayamadım :(")
client.run("MTE4MDIxMTQ1ODg3Nzk0Nzk5NA.GYAkG_.yHbucFlklERO_B6UnKj0ryj3haoZ89Zz53Fd1c")
