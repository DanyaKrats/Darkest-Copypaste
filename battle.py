import choose

def death(dead, deads_team):

    dead_pos = dead.position
    deads_team.remove(dead)
    for fighter in deads_team:
        if fighter.position > dead_pos:
            fighter.position -= 1
    return deads_team


def showme(player, monster_team):
    print("\n")
    for human in player.dung_team:
        print(human.name, round(human.health), human.position, end = "\t")
    print("\n\n")
    for monster in monster_team:
        print(monster.name, round(monster.health), monster.position, end = "\t")
    #input("\n||")

def battle(player, monster_team , a):
    #print("}{уй")
    HP_monster_team = 0
    HP_player_team = 0
    end_HP_monster_team = 0
    end_HP_player_team = 0

    skip_counter = 0
    # input()
    # Определение последовательности ходов

    init_list = []

    for i in player.dung_team:
        i.initiative = i.initiative_bonus # + рандом после обучения от 1 до 10
        init_list += [i]
        HP_monster_team += i.max_health

    for i in monster_team:
        i.initiative = i.initiative_bonus # + рандом после обучения от 1 до 10    
        init_list += [i]
        HP_player_team += i.max_health

    init_list = sorted(init_list, key=lambda x: x.initiative, reverse = True)

    round_ = 0
    while len(player.dung_team) != 0 and len(monster_team) != 0:
        
        if round_ == 30:
            break
        
        round_ += 1
        if a == 415:
           print(round_)
          #  showme(player, monster_team)
           # input()
        #input(skip_counter)
        skip_counter = 0
        #раунд
        
        for fighter in init_list:
            #if a == 50:
                #print("бой")
                #showme(player, monster_team)

            if fighter.monster == 0:
                #Действие моба
                #Проверка необходимости и осуществления лечения союзника
                heal = 0

                if fighter.healer == 1: 
                    attac_pos, heal = choose.heal_aim(player.dung_team)

                if heal == 1:
                    damage = fighter.attac2_dmg
                    for human in player.dung_team:
                        if human.position == attac_pos:
                            human.health += damage

                #Проверка наличия и выбор цели если не было совершено действие
                elif heal == 0:
                    
                    attac_pos, attac= choose.damage_aim(fighter, monster_team)
                    if attac_pos == 0 and attac == 0:
                        
                        skip_counter += 1
                        #print("________________________________________\nskip", skip_counter, len(init_list))

                        if skip_counter == len(init_list) :
                            return  player, monster_team, end_HP_monster_team/(HP_monster_team), end_HP_player_team/(HP_player_team), round_
                        break
                    for monster in monster_team:
                        damage = 0
                        if monster.position == attac_pos:
                            if attac == 1:
                                damage = fighter.attac_1(monster)

                            if attac == 2:
                                damage = fighter.attac_2(monster)
                            
                            monster.health -= damage
                            
                            if monster.health <= 0:
                                monster_team = death(monster, monster_team)
                                init_list.remove(monster)
                                break
                            else:
                                break
            
            #Текущий боец -- монстр
            elif fighter.monster == 1:

                #Действие моба
                #Проверка необходимости и осуществления лечения союзника
                heal = 0

                if fighter.healer == 1: 
                    attac_pos, heal = choose.heal_aim(monster_team)

                if heal == 1:
                    damage = fighter.attac2_dmg
                    for monster in monster_team:
                        if monster.position == attac_pos:
                            monster.health += damage
                            if monster.health>monster.max_health:
                                monster.health = monster.max_health
               
                if heal == 0:
                    
                    attac_pos, attac = choose.damage_aim(fighter, player.dung_team)


                    if attac_pos == 0 and attac == 0:
                        
                        skip_counter += 1
                        #print("________________________________________\nskip", skip_counter, len(init_list))

                        if skip_counter == len(init_list) :
                            return  player, monster_team, end_HP_monster_team/(HP_monster_team), end_HP_player_team/(HP_player_team), round_
                        break
                    
                    for human in player.dung_team:
                        damage = 0
                        if human.position == attac_pos:
                            if attac == 1:
                                damage = fighter.attac_1(human)

                            if attac == 2:
                                damage = fighter.attac_2(human)
                            
                            human.health -= damage
                            
                            if human.health <= 0:
                                player.dung_team = death(human, player.dung_team)
                                init_list.remove(human)
                                break
                            else:
                                break  
    
    end_HP_monster_team = 0
    end_HP_player_team = 0

    for i in player.dung_team:
        end_HP_player_team += i.health
    for i in monster_team:
        end_HP_monster_team += i.health

    return player, monster_team, end_HP_monster_team/(HP_monster_team), end_HP_player_team/(HP_player_team), round_                       

