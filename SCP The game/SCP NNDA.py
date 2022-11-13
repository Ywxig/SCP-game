import discord
import random

watch = ['посмотрим', "Посмотрим", 'посмотреть']
search = ['Найди', 'найди', 'Найти', 'найти', 'Вычисли', 'вычесли', 'Вычеслите', 'вычеслите']


def wat():
    arr = ['Давай найдём в scp', "Го что-то посмотрим", "Может посмотрим SCP?", "Мы можем что то найти в scp"]
    arr_name = ['https://www.youtube.com/channel/UC3M_RxlDLqUPreOpa9git5A', "https://www.youtube.com/user/ERIBestGame"]
    j = len(arr)
    j = j - 1
    r = random.randint(0, j)
    j = len(arr_name)
    j = j - 1
    r1 = random.randint(0, j)
    AWAITE = arr[r] + '\n' + arr_name[r1]
    return AWAITE

def sSCP(List):

    task = List
    s = 'http://scpfoundation.net/scp-' + task
    return s

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == message.content:
            ms = message.content
            ms_l = ms.split()
            for i in ms_l:
                if i in watch:
                    await message.channel.send(wat())

                if i in search:
                    del ms_l[0]
                    await message.channel.send(sSCP(ms_l[0]))


client = MyClient()
client.run('ODgwMTcwMDQwMjExNjczMTc4.YSaYOg.fUjovOSUTXR5-kP5Vp8moNQP3VE')
