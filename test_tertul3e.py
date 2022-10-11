import turtle as t 
import math

t.color("red")
t.shape("turtle")
t.speed(0)

walls_width = 200
walls_hight = 100
door_width = 40
door_hight = 70
roof_hight = 80
roof_side = math.sqrt(roof_hight ** 2 + (walls_width / 2) ** 2)
roof_angle = math.degrees(math.atan(roof_hight / (walls_width / 2)))

for i in range(2):
    t.fd(walls_width)
    t.left(90)
    t.forward(walls_hight)
    t.left(90)

t.fd(walls_width / 2 - door_width / 2)

for i in range(2):
    t.fd(door_width)
    t.left(90)
    t.fd(door_hight)
    t.left(90)

t.left(180)
t.fd(walls_width / 2 - door_width / 2)
t.right(90)
t.fd(walls_hight)
t.right(90)
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle * 2)
t.fd(roof_side)






t.done()
