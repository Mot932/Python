import turtle as t
import random

t.speed(0)
t.colormode(255)

x = random.randint(-500, 300)
y = random.randint(-400 , 200)
sides = random.randint(3, 50)
red = random.randint(0, 255)
green = random.randint(0, 255)
blue = random.randint(0, 255)

t.penup()
t.goto(x, y)

t.pendown()
t.fillcolor(red, green, blue)
t.begin_fill()
for i in range(sides):
	t.fd(360 / sides)
	t.left(360 / sides)
t.end_fill()

t.done()