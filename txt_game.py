from random import random
import time
print("Для начала игры напишите начать игру")
luck = int()
luck = (random()*50)
delete_flag = bool()
life_status = bool()
def enemy():
    walk_flag = bool()
    while walk_flag < 1 :
        print("Впереди враг! Что будем делать?")
        time.sleep(0.1)
        print("Доступные варианты:")
        time.sleep(0.1)
        print("убить прыжком")
        time.sleep(0.1)
        print("убить вращающейся атакой")
        time.sleep(0.1)
        print("информация о враге")
        doing_select = input()
        if doing_select == "информация о враге" :
            print("Инфорация будет скоро добавлена!")
        elif doing_select == "убить прыжком":
            life_status = 1
            walk_flag = 1
            print("вы прыгнули, а над вами были шипы. ВЫ ПОГИБЛИ!!")
        elif doing_select == "убить вращающейся атакой" :
            print("Враг был успешно уничтожен!")
            life_status = 0
            walk_flag = 1
        elif doing_select == "1" : #debug
            walk_flag = 1
            life_status = 1
            print(life_status)
        elif doing_select == "0" : #debug
            walk_flag = 1
            life_status = 0
            print(life_status)
def monologs ():
    time.sleep(0.5)
    print("Green hill zone, act 1")
    enemy()
    print(life_status)
    if life_status == 0 :
        print("Спасибо за прохождение демо-версии игры!")
    elif life_status == 1 :
        print("Игра окончена! Вы проиграли!")
def select():
    mode_select = input()
    if mode_select == "blue spheres" :
        while b < 100 :
            b += 3.125
            time.sleep(0.1)
            print("Процент пройденных уровней:", b, "%")
    elif mode_select == "mean bean" :
        time.sleep(1)
        if luck > 30 :
            print("Сражение выиграно!")
        else :
            print("Вы проиграли")
    elif mode_select == "time attack":
        print ("Уровень пройден за", luck*10//60, "минут!")
    elif mode_select == "encore mode" :
        monologs()
while 1 :
    #print (luck) #debug
    a = input()
    b = int()
    if a == "debug" :
        monologs()
    if a == "начать игру" and delete_flag == 0 :
        print("Игра успешно начата!")
        time.sleep(0.1)
        print("Далее выберите режим игры:")
        time.sleep(0.1)
        print("Mania mode")
        time.sleep(0.1)
        print("Encore mode")
        time.sleep(0.1)
        print("Time attack")
        time.sleep(0.1)
        print("Blue spheres")
        time.sleep(0.1)
        print("Mean bean")
        select()
    elif a == "начать игру" and delete_flag == 1 :
        print("Вы не можете начать игру, т.к. вы удалили наиважнейшую папку во вселенной!!!>:( ")
    elif a == "удалить system32" :
        print("У вас нет прав для удаления этой папки. Если вы администратор этого компьютера, введите пароль!")
        password = input()
        a = "1"
        if password == "48015829" :
            delete_flag = 1
            print("Папка system32 успешно удалена :)")
        else :
            print("Введен неверный пароль!")
    elif a == "список команд" :
        print("Вот полный список исполняемых команд:")
        time.sleep(0.10)
        print("удалить system32")
        time.sleep(0.10)
        print("начать игру")
        time.sleep(0.10)
        print("список команд")
