from battle import battle
import classes as cl
import battle
import time
import pandas as pd
import os 
import sqlite3
clear = lambda: os.system('cls')


def higer(arr, n):
    i = 0
    l = len(arr)-1
    

    arr[l]+=1
    a = 0
    while a<=l:

        if arr[l-a] > n:
            arr[l-a] = 1
            arr[l -1 - a] += 1

        a+=1

    return arr



def add_to_arr(player_team, monster_team, win, len_p, len_m, rounds, HP_player, HP_monster):
    
    player_team_str = []
    monster_team_str = []

    for i in player_team:
        player_team_str += [str(i)]

    for i in monster_team:
        monster_team_str += [str(i)]

    player_team = '-'.join(player_team_str)
    monster_team = '-'.join(monster_team_str)

    if win == -1:
        result = win*(len_p*25 + HP_player*100/len_p) # (-200; -25)
    else:
        result = win*(len_m*25 + HP_monster*100/len_m) #(25; 200)
    
    if result < -70:
        return [-7, 0, 0, 0, 0, 0, 0, 0, 0]
    else:
        return [player_team, monster_team, win, rounds, len_p, len_m, HP_player, HP_monster, result]

def add_to_db(all_data):

    con = sqlite3.connect("data.db")
    cur = con.cursor()


    df = pd.DataFrame(
    all_data,
    columns = ["player_team", "monster_team", "win", "rounds", "len_p", "len_m", "HP_player", "HP_monster", "result"],)

    #print(df)

    df.to_sql("data_correct", index = False, con = con)
    
    print(df)


def create_monster_team(list_):
    arr = []
    a = 0
    for i in list_:
        a += 1
        if i == 1: arr += [cl.add_skul(a)]
        elif i == 2: arr += [cl.add_harpy(a)]
        elif i == 3: arr += [cl.add_warlock(a)]
        elif i == 4: arr += [cl.add_ghost(a)]
        elif i == 5: arr += [cl.add_shaman(a)]
        elif i == 6: arr += [cl.add_horse(a)]
        elif i == 7: arr+=[cl.add_bes(a)]
        elif i == 8: arr+=[cl.add_rat(a)]
        elif i == 9: arr+=[cl.add_alive(a)]
        elif i == 10: arr+=[cl.add_piksie(a)]
        elif i == 11: arr+=[cl.add_goblin(a)]

    return arr


def create_player_team(list_):
    arr = []
    a = 0
    for i in list_:
        a += 1
        if i == 1: arr += [cl.add_Warior("Вой"+str(a))]
        if i == 2: arr += [cl.add_Archer("Лук"+str(a))]
        if i == 3: arr += [cl.add_Monk("Мон"+str(a))]
        if i == 4: arr += [cl.add_Rog("Вор"+str(a))]
        if i == 5: arr += [cl.add_Paladin("Пал"+str(a))]
        if i == 6: arr += [cl.add_Magitian("Маг"+str(a))]
        arr[a-1].position = a
    
    return arr


list_player = [1, 1, 1, 1]
list_monster= [1, 1, 1, 0]

start = time.time()

player = cl.Player("Даня", 1)

print("C Богом")
a = 0
all_data = []

all_data = [[0,0, 0, 0, 0, 0, 0, 0, 0]]

df = pd.DataFrame(
all_data,
columns = ["player_team", "monster_team", "win", "rounds", "len_p", "len_m", "HP_player", "HP_monster", "result"],)

print(df)
all_data = [[1-1, 1-1, 1, 1, 4, 0, 100, 0, 200]]
df.to_excel("data.xlsx", index = False)

start = time.time()

sum_time = 0

while list_player != [6, 6, 6, 6]:
    
    while True:  
        
        if a%10000 == 0:

            clear()
            print(a,"/", (11**4)*(6**4))
            stop = time.time()
            sum_time += stop - start
            print(stop - start, sum_time)
            start = time.time()

        player.dung_team = create_player_team(list_player)
        a+=1

        player, monster_team, HP_monster_team, HP_player_team, round_ = battle.battle(player, create_monster_team(list_monster), a)
             
        win = 0
        
        if len(monster_team) == 0 and len(player.dung_team)!=0: 
            #print("Победа людей")
            win = -1
        elif len(monster_team) != 0 and len(player.dung_team)==0: 
            #print("Поражение людей")
            win = 1
        else:
            win = 0
        
        #stop = time.time()*10**6
        
        arr = [add_to_arr(list_player,list_monster, win,len(player.dung_team), len(monster_team), round_, HP_player_team, HP_monster_team)]
        if arr[0][0] != -7:
            all_data += arr
        

        if list_monster == [11, 11, 11, 11]:
            break
        list_monster = higer(list_monster, 11)
        
    #if list_player == [1, 1, 1, 6]:
     #   add_to_db(all_data)
      #  input("Глянь че там в бд")

    list_player = higer(list_player, 6)
    list_monster = [1, 1, 1, 0]

print("\nЗапись...\n")
add_to_db(all_data)
clear()
print("\nЗапись выполнена\nЗатраченое время = ", sum_time)
print()
input()
