#�ɤJ Discord.py
import discord
#client �O�ڭ̻P Discord �s��������
client = discord.Client()

#�ե� event �禡�w
@client.event
#������H�����Ұʮ�
async def on_ready():
    print('�ثe�n�J�����G', client.user)

@client.event
#���T����
async def on_message(message):
    #�ư��ۤv���T���A�קK���J�L���`��
    if message.author == client.user:
        return
    #�p�G�]�t ping�A�����H�^�� pong
    if message.content == 'ping':
        await message.channel.send('pong')

client.run('�A�������H TOKEN') #TOKEN �b��� Discord Developer ����uBOT�v�����̭�