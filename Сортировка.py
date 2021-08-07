import pandas as pd
import os
import sqlite3 

dat = sqlite3.connect('data.db')
query = dat.execute("SELECT * FROM data_c_without_30")

arr = []

arr_0 = []
arr_lose = []
a = 0
print("Start")
 
a = 0
for row in query:
        a+=1
        if a%100000 == 0:
                print(a)
        arr_add =[]

        for elem in row:
                arr_add +=[elem]
        arr+=[arr_add]
        #print(arr)
        #input()

query  = []

new_arr= []



a = 0

for row in arr:
        a+=1
        if a%100000 == 0:
                print(a)
        if row[8]> 70:
                new_arr+=[row]

arr = new_arr
new_arr =[]

df = pd.DataFrame(
arr,
columns = ["player_team", "monster_team", "win", "rounds", "len_p", "len_m", "HP_player", "HP_monster", "result"],)

df.to_sql("data_c_diff_3", index = False, con = dat)

print("stop")

print(arr[len(arr)-1])

