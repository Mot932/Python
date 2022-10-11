import random
import os

name = input("Как зовут персонажа? ")
if not name: name = "Ботик "

os.system("cls")

name_razb = input("Как зовут разбойника? ")
if not name_razb: name_razb = "разбойник"

way_1 = True
way_2 = True
way_3 = True
way_4 = True
game = True
player_hp = 100
razb_hp = 100

key = ""


while game:

    if (way_1 or way_2 or way_3 or way_4) and key == "":
        key = ""
        os.system("cls")        
        print(f"Подъезжает {name} к четырём дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть, кто влево поедет - тому богатым быть, кто прямо поедет - тому женатым быть, тот кто на запад поедит - могучим быть, тот кто на восток пойдет -(запись стёрта) »")
        if way_1:
            print("убитому быть.1")
        if way_2:
            print("женатым быть.2")
        if way_3:
            print("богатым быть.3")
        if way_4:
            print("могучим быть.4")

        user_choice = input("какой вариант? ")     
        if user_choice == "1" or user_choice == "2" or user_choice == "3" or user_choice == "4":
            key += user_choice
        

    if key == "1" and way_1:
       os.system("cls")
       print("Дорога 1")
       print("1 вариант")
       user_choice = input("Какой вариант? ")
       if user_choice == "1":
            key += user_choice
       

            if key == "11" and way_1:
               os.system("cls")

               
               print(f" {name} увидел {name_razb}")
               print(f" {name_razb} увидел {name} ")
               input("ENTER - продолжить" )

            os.system("cls")

                           

            attack_player = random.randint(50, 100)
            attack_razb = random.randint(50, 100)



            while player_hp > 0 and razb_hp > 0:
                    os.system("cls")

                    attack_player = random.randint(1, 50)
                    razb_hp -= attack_player
                    print(f"вы снесли разбойнику", attack_player)
                    print(f"у {name_razb} осталось", razb_hp)

                    attack_razb = random.randint(1, 50)    
                    player_hp -= attack_razb
                    print("разбойник снес", attack_razb)
                    print(f"у {name} осталось", player_hp)

                    if attack_player > attack_razb:
                        print("разбойник снёс больше")
                    elif attack_player < attack_razb:
                        print("вы снесли больше")
                        

                    input("ENTER")

                    if player_hp > 0 or razb_hp <= 0:
                        
                        way_1 = False
                        key = ""
                        print("Ты победил")

                    elif player_hp <= 0 or razb_hp > 0:
                        game = False
                        print("Разбойник победил")
                                    
                        input("ENTER - продолжить")        

        

    if key == "12" and way_1:
        os.system("cls")
        print("Дорога 1 - Плохой выбор")
        game = False

    if key == "2":
        os.system("cls")
        print("Дорога 2")
        print("1 вариант")
        user_choice = input("Какой вариант? ")
        if user_choice == "1":
        
            key += user_choice
        
    if key == "21" and way_2:
        secret = random.randint(1, 10)
        print("Княжна загадала число от 1 до 10")

        attemps = 4
        while attemps:
            print(f"у вас {attemps} попыток")
            
            user_choice = int(input("Введите число: "))
            
            
            if user_choice == secret:
                print("Угадал!")
                key = ""
                way_2 = False       
                break
            elif user_choice > secret:
                print("Многовато!")
                attemps -= 1
            else:
                print("Маловато!")
                attemps -= 1 

        else:
            print("Проиграл! Кончились попытки!")
            game = False 


    if key == "3":
        os.system("cls")
        print("Дорога 3")
        print("1 вариант")
        print("2 вариант")

        user_choice = input("Какой вариант? ")
        if user_choice == "1" or user_choice == "2" or user_choice == "3":
        
            key += user_choice

    if key == "31" and way_3:
        os.system("cls")
        print("Дорога 3 - хороший выбор ")
        way_3 = False
        key = ""
        input("ENTER - дальше")

    if key == "32" and way_3:
        os.system("cls")
        print("Дорога 3 - Плохой выбор")
        game = False


    if key == "4":
       os.system("cls")
       print("Дорога 4")
       print("1 вариант")
       print("2 вариант")
       user_choice = input("Какой вариант? ")
       if user_choice == "1" or user_choice == "2":
        
            key += user_choice

    if key == "41" and way_4:
       os.system("cls")
       print("Дорога 4 - хороший выбор ")
       way_4 = False
       key = ""
       input("ENTER - дальше")


    if key == "42" and way_4:
        os.system("cls")
        print("Дорога 4 - Плохой выбор")
        game = False


    if way_1 == way_2 == way_3 == way_4 == False:
        
        os.system("cls")
        print("Все дороги пройдены!")
        print("Конец")