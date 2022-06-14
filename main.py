import random, time

import main

print(f'Добро пожаловать в Русскую рулетку, Амиго! Как тебя зовут?')
name = input()
ai_names = ["Генри", "Стэтхэм", "Дрейк", "Барбосса", "Хитмен", "Робокоп", "Томми Шелби", "Винсент Вега", "Косматый геолог", "Мандалорец", "Бобба Фетт", "Терминатор"]

"""перемешиваем список имён, чтобы играть каждый раз с новыми оппонентами"""
random.shuffle(ai_names)

players_names = [name, ai_names[0], ai_names[1]]

"""статусы игроков по умолчанию (жив/мёртв)"""
players_status = ["жив", "жив", "жив"]

print(
    f'Отлично {name}!\n__________________\nПравила игры просты, перед тобой заряженный револьвер, в нём есть 6 ячеек и один патрон,\nкаждый по очереди приставляет пистолет к виску'
    f' и поочередно спускает курок, кто выживет в этой перестрелке, тот и победил!\nС тобой играют двое опасных парней: {ai_names[0]} и {ai_names[1]}.'
    f'\n__________________\nТы готов? Нажми Y!')


"""модуль старта игры"""

start_flag = False

while start_flag == False:
    print(f'Нажми Y для старта')
    start = input()
    if start == "y" or start == "Y":
        start_flag = True
    else:
        continue

"""количество ячеек под патроны в револьвере"""
catridge = [1, 2, 3, 4, 5, 6]

"""функция перезаряда патрона"""
def restart_catridge():
    return random.randint(1, 6)

real_catridge = restart_catridge()

"""функция стрельбы игрока"""
def shoot_player():
    flag_x = True
    while flag_x == True:
        print(f'Стреляешь ты! {players_names[0]} Нажми Y или N')
        shoot_pl = input()
        if shoot_pl == "y" or shoot_pl == "Y":
            x = random.randint(1, len(catridge))
            if x == real_catridge:
                time.sleep(3)
                print(f'Ты убит! Игра окончена!')
                raise SystemExit
            else:
                time.sleep(3)
                print(f'Повезло, продолжаем играть!\n__________________')
                break
        elif shoot_pl == "n" or shoot_pl == "N":
            print(f'Игра окончена, спасибо что сыграл!')
            raise SystemExit

"""функция стрельбы компьютера №1"""
def shoot_ai_1():
    time.sleep(5)
    print(f'Стреляет {ai_names[0]}!')
    time.sleep(2)
    x = random.randint(1, len(catridge))
    if x == real_catridge:
        print(f'{ai_names[0]} убит! Играем дальше!\n__________________')
        print(f'Перезаряжаем барабан..')
        players_status[1] = "мёртв"
        time.sleep(2)
        restart_catridge()
    else:
        time.sleep(3)
        print(f'{ai_names[0]}, тебе повезло, продолжаем играть!\n__________________')
        restart_catridge()

"""функция стрельбы компьютера №2"""

def shoot_ai_2():
    time.sleep(5)
    print(f'Стреляет {ai_names[1]}!')
    time.sleep(2)
    x = random.randint(1, len(catridge))
    if x == real_catridge:
        print(f'{ai_names[1]} убит! Заряжаем еще один патрон и играем дальше!\n__________________')
        print(f'Перезаряжаем барабан..')
        players_status[2] = "мёртв"
        time.sleep(5)
        restart_catridge()
    else:
        time.sleep(2)
        print(f'{ai_names[1]}, тебе повезло, продолжаем играть!\n__________________')
        restart_catridge()

"""модуль игры, после каждой попытки, пистолет перезаряжается,
как только игрок погибает или остается один среди оппонентов - игра заканчивается. 
Так же, есть возможность выхода из игры через букву N/n"""

while start_flag == True:
    if players_status[0] == "жив":
        shoot_player()
        real_catridge = restart_catridge()
    if players_status[1] == "жив":
        shoot_ai_1()
        real_catridge = restart_catridge()
    if players_status[2] == "жив":
        shoot_ai_2()
        real_catridge = restart_catridge()
    elif players_status[1] == "мёртв" and players_names[2] == "мёртв":
        print(f'Вы победили, оппонентов нет!')
        raise SystemExit

