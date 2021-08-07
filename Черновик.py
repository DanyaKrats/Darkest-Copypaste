from battle import battle
import classes as cl
import battle
import time
import pandas as pd
import os 
#clear = lambda: os.system('cls')


#i = 0

#arr=[[]]

#start = time.time()

#while i <29000000:
 #   i+=1
  #  if i % 10000 == 0:
#
 #       clear()
  #      print(i)
   # arr+=["Олег", "Макет",2,3,4]

#stop = time.time()

#print("done. time = ", start-stop,)



























"""

def add_to_excel(player_team, monster_team, win, len_p, len_m, rounds, HP_player, HP_monster):
    
    player_team_str = []
    monster_team_str = []

    for i in player_team:
        player_team_str += [str(i)]

    for i in monster_team:
        monster_team_str += [str(i)]

    #print('-'.join(player_team_str))

    player_team = '-'.join(player_team_str)
    monster_team = '-'.join(monster_team_str)

    if win == -1:
        result = win*(len_p*25 + HP_player*100/len_p) # (-200; -25)
    else:
        result = win*(len_m*25 + HP_monster*100/len_m) #(25; 200)

    return [player_team, monster_team, win, rounds, len_p, len_m, HP_player, HP_monster, result]

def add_to_excel_2(all_data):
    #print(player_team, monster_team, win, rounds, len_p, len_m, HP_player, HP_monster, result)
    #all_data = [[player_team, monster_team, win, rounds, len_p, len_m, HP_player, HP_monster, result]]

    df_new = pd.DataFrame(
    all_data,  
    columns = ["player_team", "monster_team", "win", "rounds", "len_p", "len_m", "HP_player", "HP_monster", "result"],)

    df = pd.read_excel('data.xlsx')

    print("Таблица")
    

    df = df.append(df_new, ignore_index= True)
    #print(df)
    df.to_excel("data.xlsx", index = False)
    clear()


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

def list_p_p_1(list_player):
    if list_player[3]<6:
        list_player[3] +=1
    elif list_player[3] == 6 and list_player[2]<6:
        list_player[3] = 1
        list_player[2] +=1
    elif list_player[2] == 6 and list_player[1]<6:
        list_player[2] = 1 
        list_player[1] += 1
    elif list_player[1] == 6 and list_player[0]<6:
        list_player[1] = 1 
        list_player[0] += 1   

    return list_player 

def list_m_p_1(list_player):
    if list_player[3]<11:
        list_player[3] +=1
    elif list_player[3] == 11 and list_player[2]<11:
        list_player[3] = 1
        list_player[2] +=1
    elif list_player[2] == 11 and list_player[1]<11:
        list_player[2] = 1 
        list_player[1] += 1
    elif list_player[1] == 11 and list_player[0]<11:
        list_player[1] = 1 
        list_player[0] += 1   

    return list_player 

list_player = [1, 1, 1, 1]
list_monster= [1, 1, 1, 1]



print("C Богом")
a = 0


while list_player != [6, 6, 6, 6]:
    
    while list_monster != True:  
        
        print(list_monster, "\t", list_player)
        
        if list_monster == [11, 11, 11, 11]:
            break 
        list_monster = list_m_p_1(list_monster)

        #input()

    print("\nЗапись\n")
    input()
    list_player = list_p_p_1(list_player)
    list_monster = [1, 1, 1, 1]
"""

