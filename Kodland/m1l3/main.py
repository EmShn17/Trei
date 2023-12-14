import discord
import random

def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "Yazı Çıktı :)"
    else:
        return "Tura Çıktı :)"

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
    elif message.content.startswith('$en sevdiğin renk nedir'):
        await message.channel.send("En sevdiğim renk tabikide yeşil.")
    elif message.content.startswith('$kaç yaşındasın'):
        await message.channel.send("Ben bir robot olduğum için yaşlanmıyorum.")
    elif message.content.startswith('$coin'):
        await message.channel.send(yazi_tura())
    elif message.content.startswith('$'):
        await message.channel.send("Bu komutu anlayamadım :(")
client.run("MTE4MDIxMTQ1ODg3Nzk0Nzk5NA.GnabUR.3wRRytM6rTNatfj31QTo7RvZNu8JzktF_aGE8Y")
