"""
Библиотека классов игры
"""

"""
dmg_type 
1 -- рубящий урон
2 -- колющий урон
3 -- огненный урон
4 -- дробящий урон
5 -- урон излучением

0 -- лечение 
"""

class Player(object):
    def __init__(self, name, difficulty):
        self.name = name
        self.gold = 100
        self.team = []
        self.dung_team = []
        self.difficulty = difficulty
        self.position = 0
    
    def sort_team(self):
        self.team.sort()

class Fighter(object):
    
    def __init__ (self, name, type, health, deffense, initiative_bonus, healer, weakness, attac1_name, attac1_reachable_positions, attac1_type, attac1_dmg, attac2_name, attac2_reachable_positions, attac2_type, attac2_dmg):
        self.monster = 0
        self.name = name
        self.type = type
        self.max_health = health
        self.health = health
        self.deffense = deffense
        self.position = 0
        self.initiative_bonus = initiative_bonus
        self.initiative = 0
        self.healer = healer
        self.weakness = weakness

        self.attac1_name = attac1_name
        self.attac1_reachable_positions = attac1_reachable_positions
        self.attac1_type = attac1_type
        self.attac1_dmg = attac1_dmg
        
        self.attac2_name = attac2_name
        self.attac2_reachable_positions = attac2_reachable_positions
        self.attac2_type = attac2_type
        self.attac2_dmg = attac2_dmg
    
    def attac_1(self, enemy):
        if enemy.weakness == self.attac1_type:
            return round(self.attac1_dmg*2*(1-enemy.deffense))  
        else:
            return round(self.attac1_dmg*(1-enemy.deffense))    

    def attac_2(self, enemy):
        if self.healer == 1:
            return self.attac2_dmg
        elif enemy.weakness == self.attac2_type:
            return round(self.attac2_dmg*2*(1-enemy.deffense))  
        else:
            return round(self.attac2_dmg*(1-enemy.deffense))  

class Monster(object):
    def __init__ (self, name, health, deffense, position, initiative_bonus, healer, weakness, loot, attac1_name, attac1_reachable_positions, attac1_type, attac1_dmg, attac2_name, attac2_reachable_positions, attac2_type, attac2_dmg):
        self.real_name = name 
        self.max_health = health
        self.health = health
        self.deffense = deffense
        self.position = position
        self.loot = loot
        self.monster = 1
        self.weakness = weakness
        self.initiative_bonus = initiative_bonus
        self.healer = healer
        self.initiative = 0
        self.name = name + str(self.position)

        self.attac1_name = attac1_name
        self.attac1_reachable_positions = attac1_reachable_positions
        self.attac1_type = attac1_type
        self.attac1_dmg = attac1_dmg


        self.attac2_name = attac2_name
        self.attac2_reachable_positions = attac2_reachable_positions
        self.attac2_type = attac2_type
        self.attac2_dmg = attac2_dmg

    def attac_1(self, enemy):
        if enemy.weakness == self.attac1_type:
            return round(self.attac1_dmg*2*(1-enemy.deffense))  
        else:
            return round(self.attac1_dmg*(1-enemy.deffense))    

    def attac_2(self, enemy):
        if self.healer == 1:
            return self.attac2_dmg
        elif enemy.weakness == self.attac2_type:
            return round(self.attac2_dmg*2*(1-enemy.deffense))  
        else:
            return round(self.attac2_dmg*(1-enemy.deffense))  


#Создание война
def add_Warior(name):
    warior =Fighter(name, "Воин", 54, 0.6,	1,	0,	3,	"Клинком плашмя",	[1, 2],	4,	8,	"Разрубание",	[1, 2, 3], 	1,	12)
    return warior

def add_Archer(name):
    Archer = Fighter(name, "Лучник",	31,	0.2,	5,	0,	1,		"Точный выстрел",	[2, 3, 4],	1,	13,	"Огненная стрела",	[2, 3, 4],	3,	9)
    return Archer

def add_Monk(name):
    Monk = Fighter(name, "Клирик",	34,	0.3,	3,	1,	4,		"Карающий Свет",	[2, 3],	5,	6,	"Молитва о здравии",	[1, 2, 3, 4],	0,	5)
    return Monk

def add_Rog(name):
    Rog = Fighter(name, "Плут",	48,	0.5,	4,	0,	2,		"Кинжал в больное место",	[1, 2, 3],	2,	10,	"Вспарывание с тыла",	[3, 4],	1,	9)
    return Rog

def add_Paladin(name):
    Paladin = Fighter (name, "Паладин",	60,	0.6,	2,	1,	5,	"Бросок пламенного молота",	[1, 2, 4],	3,	7,	"Возложение рук",	[1, 2, 3, 4],	0,	8)
    return Paladin

def add_Magitian(name):
    mag = Fighter(name, "Колдун",	25,	0.1,	6,	0,	1,		"Огненный шар",	[2, 3, 4],	3,	16,	"Ледяные клинки",	[1, 2, 3, 4],	2,	16)
    return mag


#Добавляем монстров
def add_skul(position):
    skul = Monster("Скелет",		27,	0.23, position, 0,	0,	4,	10,	"Ржавый меч",	[1, 2],	1,	8,	"Зубы нежити",	[2, 3],	4,	5)
    return skul

def add_harpy(position):
    harpy = Monster("Гарпия",		30,	0.3,	position,	3,	0,	3,	10,	"Вороньи когти",	[1, 2, 3, 4],	2,	12,	"Крылья-лезвия",	[1, 2, 3, 4],	1,	12)
    return harpy

def add_warlock(position):
    warlock = Monster("Чернокнижник",		44,	0.1,	position,	3,	1,	1,	15,	"Черный глаз",	[1, 2],	5,	10,	"Помощь Тьмы",	[1, 2, 3, 4],	0,	5)
    return warlock

def add_ghost(position):
    ghost = Monster("Призрак",		28,	0.4,	position,	2,	0,	5,	9,	"Вой усопшего",	[2, 3, 4],	5,	13,	"Дрож могилы",	[1, 4],	4,	10) 
    return ghost

def add_shaman(position):
    shaman =  Monster("Орк-Шаман",		38,	0.2,	position,	1,	1,	2,	20,	"Муки Жара",	[1, 2, 3, 4],	3,	8,	"Лечебный гриб",	[1, 2, 3, 4],	0,	5)
    return shaman

def add_horse(position):
    horse = Monster("Проклятая Лошадь", 68,	0.35,	position, 3,	0,	1,	50,	"Пламенные подковы",	[1,2],	3,	18,	"Адское ржание",	[1, 2, 3, 4],	5,	10)		
    return horse

def add_bes(position):
    bes = Monster("Смрадный Бес",		29,	0.3,	position,	2,	0,	4,	25,	"Темный шептун",	[1, 2, 3],	5,	13,	"Меазмы",	[3, 4],	3,	13)
    return bes

def add_rat(position):
    rat = Monster("Крысолов",		48,	0.4,	position,	0,	1,	3,	26,	"Бросок тифозной крысы",	[3, 4],	2,	20,	"Укус канализации",	[1, 2],	4,	12)
    return rat

def add_alive(position):
    alive = Monster("Живые Доспехи", 70,	0.5,	position,	0,	0,	5,	30,	"Навалиться весом",	[1],	4,	8,	"Выстрел перчатки",	[2, 3, 4],	2,	7)
    return alive

def add_piksie(position):
    piksie = Monster("Злобный Пикси",		20,	 0.3,	position,	4,	0,	2,	14,	"Вредность колющая",	[3, 4],	2,	16,	"Резкий удар",	[1, 2, 3],	4,	18)
    return piksie

def add_goblin(position):
    goblin = Monster("Подручный гоблин",		35,	0.2,	position,	2,	1,	5,	6,	"Бросок яблоком",	[1, 2],	4,	5,	"Целебная припарка",	[1, 2, 3, 4],	0,	8)
    return goblin