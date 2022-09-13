
import discord
import random

TOKEN = 'Insert Token Here'
client = discord.Client()

coinflips = ('Heads','Tails')
who = ('Survs' , 'Pixqll' , 'Cchorus' , 'Hugo')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'bot-testing':
       if user_message.lower() == 'you suck <@1007731389019476159>':
           await message.channel.send(f'no you lol!')
           return
       elif user_message.lower() == 'nice bot':
           await message.channel.send(f'thank you :D {username}!')
           return
       elif user_message.lower() == '-random':
           response = f'this is a totally 100% no cap ong fr fr random number: {random.randrange(1000000)}'
           await message.channel.send(response)
           return
       elif user_message.lower() == '-coinflip':
           toss = random.choice(coinflips)
           await message.channel.send(toss)
           return
       elif user_message.lower() == 'this bot is trash':
           await message.channel.send(f'no you, are i run you up LOLOLOLOLOLOLOLOLOL')
           return
       elif user_message.lower() == 'isnt that right':
           await message.channel.send(f'yeah thats right')
           return
       elif user_message.lower() == 'whos the best monkey gang member?':
           whoisbetter = random.choice(who)
           await message.channel.send(whoisbetter)
           return


client.run(TOKEN)
