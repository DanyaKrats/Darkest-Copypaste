
from time import sleep


def heal_aim(teamates):
    needheal = [0.7, 0]
    heal_flag = 0
    for teamate in teamates:
        if (teamate.health / teamate.max_health) <= needheal[0]:
            heal_flag = 1
            needheal = [teamate.health / teamate.max_health, teamate.position]

    return needheal[1] , heal_flag 


def damage_aim(fighter, enemys):

    aims_1 = []
    aims_2 = []

    for enemy in enemys:

        if fighter.healer == 0:

            if enemy.position in fighter.attac1_reachable_positions:

                aims_1 += [enemy]
            if enemy.position in fighter.attac2_reachable_positions:

                aims_2 += [enemy]
        
        else:
            if enemy.position in fighter.attac1_reachable_positions:
                aims_1 += [enemy]

    
    if len(aims_1) == 0 and len(aims_2) == 0:
        return 0, 0

    weak_aim_1 = []
    for enemy in aims_1:
        if enemy.weakness == fighter.attac1_type:
            weak_aim_1 += [enemy]


    weak_aim_2 = []
    for enemy in aims_2:
        if enemy.weakness == fighter.attac2_type:
            weak_aim_2 += [enemy]


    if len(weak_aim_2)!=0 or len(weak_aim_1)!=0:
        
        if len(weak_aim_1) != 0:
            #print("313131313131313131")
            doomed = []
            k = 2
            for enemy in weak_aim_1:
                if enemy.health/enemy.max_health < k:
              #      print("321321321")
                    k = enemy.health/enemy.max_health
                    doomed = [enemy]
            weak_aim_1 = doomed 
            if len(weak_aim_2) == 0 and len(weak_aim_1)!=0:

                return weak_aim_1[0].position , 1

        if len(weak_aim_2) != 0:
            #print("323223232323232323232")
            doomed = []
            k = 2
            #print("__________________",)
            for enemy in weak_aim_2:
               # print("__________________", enemy)
                if enemy.health/enemy.max_health < k:
                    k = enemy.health/enemy.max_health
                    doomed = [enemy]
            weak_aim_2 = doomed
            if len(weak_aim_1) == 0 and len(weak_aim_2)!=0:
                return weak_aim_2[0].position , 2


    #print("44444444444444444444444444444")
    if len(weak_aim_2)!=0 and len(weak_aim_1)!=0:
        if weak_aim_2[0].health <= weak_aim_1[0].health:
            return weak_aim_2[0].position, 2
        else:
            return weak_aim_1[0].position, 1


    #поиск цели с наимеьшим здоровьем
    if len(aims_1)!= 0 :
        doomed = []
        k = 2
        for enemy in aims_1:
            if enemy.health/enemy.max_health< k:
                k = enemy.health/enemy.max_health
                doomed =[enemy]
        aims_1 = doomed
        if len(aims_2) == 0 and len(aims_1)!= 0:
            return aims_1[0].position, 1
    

    if len(aims_2)!= 0 :
        doomed = []
        k = 2
        for enemy in aims_2:
            if enemy.health/enemy.max_health< k:
                k = enemy.health/enemy.max_health
                doomed =[enemy]
        aims_2 = doomed
        if len(aims_1) == 0 and len(aims_2)!= 0:
            return aims_2[0].position, 2


    if len(aims_2)!=0 and len(aims_1)!=0:
        if aims_2[0].health <= aims_1[0].health:
            return aims_2[0].position, 2
        else:
            return aims_1[0].position, 1



    

