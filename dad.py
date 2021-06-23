from requests.models import ContentDecodingError
import discord
import requests
import json
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
    index=message.content.lower().find('blague')
    if index > -1:
        session = requests.Session()
        session.headers.update({'Authorization': f'Bearer {keys.token_joke}'})
        response = session.get('https://www.blagues-api.fr/api/random')
        if response.status_code == 200:
            content = json.loads(response.content)  
            message = f"AH des blagues ! J'en connais plein ! \n {content['joke']} \n {content['answer']}\n🤣🤣🤣🤣🤣🤣"
    
# Run bot (arg is the bot token)
client.run(keys.token)