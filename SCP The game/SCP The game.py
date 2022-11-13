#SCP The game!
import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def login(ctx, nic):
    filename = nic + '.txt'
    file = open(filename, 'w')
    file.write(nic)
    await ctx.send('log how:'+nic)
    file = open('Журнал.txt', 'a')
    file.write(nic + ' ')

@bot.command()
async def pvp(ctx):
    t1 = 0
    t2 = 0
    file = open('Журнал.txt', 'r')
    plaers = file.read()
    plaers_l = plaers.split()
    print(plaers_l)
    for j in plaers_l:
        print(j)
    q = len(plaers_l)
    q = q - 1
    print(q)
    r = random.randint(0, q)
    r2 = random.randint(0, q)
    await ctx.send(plaers_l[r] + ' VS ' + plaers_l[r2])
    file = open(plaers_l[r]+'-time.txt' , 'r')
    scp1 = file.read()
    scp1_l = scp1.split()

    file = open(plaers_l[r2]+'-time.txt' , 'r')
    scp2 = file.read()
    scp2_l = scp2.split()


    file = open('C:/Users/Dima_VAIO/Desktop/SCP The game/scp_profel/' + scp1_l[0] + '.txt')
    slot11 = file.read()

    file = open('C:/Users/Dima_VAIO/Desktop/SCP The game/scp_profel/' + scp1_l[1] + '.txt')
    slot21 = file.read()

    file = open('C:/Users/Dima_VAIO/Desktop/SCP The game/scp_profel/' + scp1_l[2] + '.txt')
    slot31 = file.read()

    file = open('C:/Users/Dima_VAIO/Desktop/SCP The game/scp_profel/' + scp1_l[3] + '.txt')
    slot41 = file.read()

#time 2

    file = open('C:/Users/Dima_VAIO/Desktop/SCP The game/scp_profel/' + scp2_l[0] + '.txt')
    slot12 = file.read()

    file = open('C:/Users/Dima_VAIO/Desktop/SCP The game/scp_profel/' + scp2_l[1] + '.txt')
    slot22 = file.read()

    file = open('C:/Users/Dima_VAIO/Desktop/SCP The game/scp_profel/' + scp2_l[2] + '.txt')
    slot32 = file.read()

    file = open('C:/Users/Dima_VAIO/Desktop/SCP The game/scp_profel/' + scp2_l[3] + '.txt')
    slot42 = file.read()

    s11 = slot11.split()
    s21 = slot21.split()
    s31 = slot31.split()
    s41 = slot41.split()

    s12 = slot12.split()
    s22 = slot22.split()
    s32 = slot32.split()
    s42 = slot42.split()

    print('команда 1: ' + slot11)   
    print('команда 1: ' + slot21)
    print('команда 1: ' + slot31)
    print('команда 1: ' + slot41)

    print('команда 2: ' + slot12)   
    print('команда 2: ' + slot22)
    print('команда 2: ' + slot32)
    print('команда 2: ' + slot42)


        

    hp1 = ''.join(s11[0])
    hp2 = ''.join(s21[0])
    hp3 = ''.join(s31[0])
    hp4 = ''.join(s41[0])

    dm1 = ''.join(s11[2])
    dm2 = ''.join(s21[2])
    dm3 = ''.join(s31[2])
    dm4 = ''.join(s41[2])

    df1 = s11[3]
    df2 = s21[3]
    df3 = s31[3]
    df4 = s41[3]

    hp1b = ''.join(s12[0])
    hp2b = ''.join(s22[0])
    hp3b = ''.join(s32[0])
    hp4b = ''.join(s42[0])

    dm1b = ''.join(s12[2])
    dm2b = ''.join(s22[2])
    dm3b = ''.join(s32[2])
    dm4b = ''.join(s42[2])

    df1b = s12[3]
    df2b = s22[3]
    df3b = s32[3]
    df4b = s42[3]

    time_dm1 = dm1 + dm2 + dm3 + dm4
    time_dm2 = dm1b + dm2b + dm3b + dm4b

    if time_dm2 >= hp1:
        t1 = t1 + 1

    if time_dm1 >= hp1b:
        t2 = t2 + 1

    if time_dm2 >= hp2:
        t1 = t1 + 1

    if time_dm1 >= hp2b:
        t2 = t2 + 1

    if time_dm2 >= hp3:
        t1 = t1 + 1

    if time_dm1 >= hp3b:
        t2 = t2 + 1  

    if time_dm2 >= hp4:
        t1 = t1 + 1

    if time_dm1 >= hp4b:
        t2 = t2 + 1 

    print(str(t1) + ' VS ' + str(t2))



    if t1 > t2:
        await ctx.send(plaers_l[r] + ' win!')

    if t2 > t1:
        await ctx.send(plaers_l[r2] + ' win!')

    if t1 == t2:
        await ctx.send('Ничья!')
    
@bot.command()
async def time(ctx, name, scp1, scp2, scp3, scp4):
    file = open(name+'.txt' , 'r')
    time = file.read()

    env_l = time.split()

    for i in env_l:
        print(name+' '+i)
        env = time

        if scp1 in env_l:
            pass

        if scp2 in env_l:
            pass

        if scp3 in env_l:
            pass

        if scp4 in env_l:
            pass

        else:
            await ctx.send('Ошибка нет такого обекта в инвенторе!')
            
    file = open(name+'-time.txt' , 'w')
    time = file.write(scp1 + ' ' + scp2 + ' ' + scp3 + ' ' + scp4)

    
    
    
    
bot.run('ODgxMTk5MjY1NDYzMDEzNDE2.YSpWxA.7Bd7xwSApNGu7sBKL7GyCkQV9kE')
