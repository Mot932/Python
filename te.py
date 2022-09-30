import os

name = input("Как зовут персонажа? ")
if not name: name = "Ботик "

way_1 = True
way_2 = True
way_3 = True
way_4 = True
way_5 = True
game = True
user_hp = 100
key = ""


while game:

    if (way_1 or way_2 or way_3 or way_4 or way_5) and key == "":
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
        if way_5:
            print("Альтернативный вариант.5")

        user_choice = input("какой вариант? ")     
        if user_choice == "1" or user_choice == "2" or user_choice == "3" or user_choice == "4" or user_choice == "5":
            key += user_choice
        

    if key == "1" and way_1:
       os.system("cls")
       print("Дорога 1")
       print("1 вариант")
       print("2 вариант")
       user_choice = input("Какой вариант? ")
       if user_choice == "1" or user_choice == "2":
            key += user_choice
       

    if key == "11" and way_1:
       os.system("cls")
       print("Дорога 1 - хороший выбор ")
       way_1 = False
       key = ""
       input("ENTER - дальше")

    if key == "12" and way_1:
        os.system("cls")
        print("Дорога 1 - Плохой выбор")
        game = False

    if key == "2":
        os.system("cls")
        print("Дорога 2")
        print("1 вариант")
        print("2 вариант")
        user_choice = input("Какой вариант? ")
        if user_choice == "1" or user_choice == "2":
        
            key += user_choice
        
    if key == "21" and way_2:
        os.system("cls")
        print("Дорога 2 - хороший выбор ")
        way_2 = False
        key = ""
        input("ENTER - дальше")

    if key == "22" and way_2:
        os.system("cls")
        print("Дорога 2 - Плохой выбор")
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


    if key == "5":
       os.system("cls")
       print("Дорога 5")
       print("1 вариант")
       print("2 вариант")
       user_choice = input("Какой вариант? ")
       if user_choice == "1" or user_choice == "2":
        
            key += user_choice

    if key == "51" and way_5:
       os.system("cls")
       print("Дорога 5 - хороший выбор ")
       way_4 = False
       key = ""
       input("ENTER - дальше")


    if key == "52" and way_5:
        os.system("cls")
        print("Дорога 5 - Плохой выбор")
        game = False
        


    if way_1 == way_2 == way_3 == way_4 == way_5 == False:
        
        os.system("cls")
        print("Все дороги пройдены!")
        print("Конец")