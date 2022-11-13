

import discord
global information
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
            print(ms_l)

            if ms_l[0] == '!setscp':
                
                del ms_l[0]
                index = ms_l[0]
                del ms_l[0]
                clas = ms_l[0]
                del ms_l[0]
                img = ms_l[0]
                del ms_l[0]
                information = ' '.join(ms_l)
                scp =    "if nomber == '" + index + "':\n        info = '" + information + "'\n        imgg = '" + img + "'\n        q = info + img\n        await ctx.send(clas('" + clas +"') ' ' + q)"
                file = open('scp.txt', 'a')
                file.write('\n\n' + scp)
                print(scp)
                await message.channel.send('\n\n\nMTF выехоли для поимки scp-'+ index)

client = MyClient()
client.run('ODc5OTY5MTMyMDg5NTkzOTA2.YSXdHg.GIuA9iUSIXfylcWRaVYYNV7IYrM')
