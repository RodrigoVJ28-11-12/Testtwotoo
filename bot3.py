import discord

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$about'):
        await message.channel.send("This Bot was made by MrsDoe (name might not be updated), it's a bot which can tell you hints on what to do with plastic and when does some things you use everyday decompose.")
    elif message.content.startswith('$hint1'):
        await message.channel.send("Hint 1: you can make a car with a carton of milk, 4 small wooden wheels and 2 wooden rods, poke 4 holes in the carton, 2 next to the bottom, 2 next to the opening, then you gotta put the two wooden rods in each one of the holes, make sure the rods are big enough for you to clearly see them poking out of the carton, then make sure the wooden wheels are big enough to fit in the rod but small enough to not dislocate from the rod, add 1 on each side, 2 on the back and 2 on the front, there you have it! a car made with a carton of milk and a few wooden items you would probably throw away!")
    elif message.content.startswith('$hint2'):
        await message.channel.send("one of the things you can do with a bottle of coca-cola, you can make art with it! take the cap from diet, zero sugar, zero coffee, normal, etc. and use them as items for an art. If you're not an artist but you like plants, you can use the bottle as a place to put your plants in, just cut the bottle in the middle, poke a few holes under it and you got a homemade plant pot. IF you dont like any of those things, i'd recommend doing the hint 1!")
    elif message.content.startswith('$hint3'):
        await message.channel.send("when you're bored and you got a bottle of coca-cola, try playing with it like it's a sword! you can even carve it into a sword if you got a stiletto or scissors (if you wanna keep things easier)")
    elif message.content.startswith('$decompose'):
        await message.channel.send("The commands you can use now is: $plastic, $paper, $metal, $fungus and $plants")
        if message.content.continueswith('$plastic'):
            await message.channel.send("plastic is very dependant of what is the type of plastic, it can average from 20 to 600 years.")
        elif message.content.startswith('$paper'):
            await message.channel.send("paper isnt that dependant of the type, it's in average of 2 to 6 months to decompose.")
        elif message.content.startswith('$metal'):
            await message.channel.send("metal is a bit trickier because there are a lot of different metals but it's in average 30 to 500 years.")
        elif message.content.startswith('$fungus'):
            await message.channel.send("actually, fungus is one of the main reasons of why things decompose, cientists even found a fungus who can completely decompose 100% pure plastic in 140 to 150 days! and also fungus doesnt actually decompose.")
        elif message.content.startswith('$plants'):
            await message.channel.send("plants are organic and mostly, organic things take 2 to a whole year to decompose.")
    else:
        await message.channel.send(message.content)

client.run("MTQzNjA4NjQ4MTY1NDY0ODg1Mw.GOUX-9.8LqiL4MwIp3XPFwJDSt7uCze32jziSjola9ldE")