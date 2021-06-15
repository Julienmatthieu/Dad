import discord
import keys

client = discord.Client()

# Registering Loggin event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Registering Receving Message event
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    index=message.content.lower().find('je suis')
    if index > -1:
        name = message.content.lower().split('je suis')[1]
        text = f'Bonjour {name}. Je suis papa !'
        if len(text) >= 2000:
            await message.channel.send('T\'es un marrant toi. Je t\'aime bien. Tu serais pas papa aussi ?')
            return
        await message.channel.send('Bonjour' + name + '. Je suis papa !')

# Run bot (arg is the bot token)
client.run(keys.token)