import turtle as t 
import math
import time

t.color("blue")
t.shape("turtle")
t.speed(10)

walls_width = int(input("Высота стен "))
walls_hight = int(input("Ширина стен "))

walls_color = input("цвет стен(hex) ")
door_width = int(input("Ширина двери "))
door_hight = int(input("Высота двери "))
door_color = input("цвет двери(hex) ")
roof_hight = int(input("высота крыши "))
roof_color = input("цвет крыши(hex) ")
roof_side = math.sqrt(roof_hight ** 2 + (walls_width / 2) ** 2)
roof_angle = math.degrees(math.atan(roof_hight / (walls_width / 2)))

x = (walls_width / 2) * -1
y = (walls_hight + roof_hight) / 2 * -1
t.setposition(x,y)

t.fillcolor(walls_color)
t.begin_fill()
for i in range(2):
    t.fd(walls_width)
    t.left(90)
    t.forward(walls_hight)
    t.left(90)
t.end_fill()



t.fd(walls_width / 2 - door_width / 2)
t.fillcolor(door_color)
t.begin_fill()
for i in range(2):
    t.fd(door_width)
    t.left(90)
    t.fd(door_hight)
    t.left(90)
t.end_fill()


t.left(180)
t.fd(walls_width / 2 - door_width / 2)
t.right(90)
t.fd(walls_hight)
t.fillcolor(roof_color)
t.begin_fill()
t.right(90)
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle * 2)
t.fd(roof_side)
t.setheading(180)
t.fd(walls_width)
t.end_fill()

t.done()