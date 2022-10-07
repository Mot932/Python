import random

secret = random.randint(1, 100)
print(secret)
print("Княжна загадала число от 1 до 100")

attemps = 7
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


