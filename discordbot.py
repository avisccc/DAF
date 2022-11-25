import discord
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True
intents.message_content = True
client = discord.Client(command_prefix='?',intents=intents)

@client.event
async def on_ready():
    print('Bot Online', client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #�p�G�]�t ping�A�����H�^�� pong
    if message.content == 'ping':
        await message.channel.send('pong')

client.run('MTA0NTM2NzY4MjUxOTgxNDI0NA.GSdXLH.IuFrN87tR_yL7aoWPiaMPepJ_k-g5DVlPSIZ4I') 