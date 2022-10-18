import turtle as t
import random 

t.speed(0)
t.colormode(255)

while True:

	x = random.randint(-200 , 200)
	y = random.randint(-200 , 100)
	circles = random.randint(3 , 6) # количество комков
	radius = random.randint(30 , 60) # радиус первого комка
	red = random.randint(0 , 255)
	green = random.randint(0 , 255)
	blue = random.randint(0 , 255)

	t.penup()
	t.setpos(x , y)

	for i in range(circles):
		t.pendown()
		t.fillcolor(red , green , blue)
		t.begin_fill() 
		t.circle(radius)
		t.penup()
		t.setheading(90)
		t.fd(radius * 2)
		t.setheading(0)
		t.end_fill()
		radius /= 2


t.done()