import turtle as t
import math
t.speed(0)

def draw_house(
    walls_x, 
    walls_y, 
    walls_width, 
    walls_height, 
    walls_color, 
    door_width, 
    door_hight, 
    door_color,
    roof_hight,
    roof_color
    ):
    """
    
    x - левый нижней угол стены
    y - левый нижний угол стены
    walls_width ширина стены
    walls_height высота стены
    walls_color цвет заливки
    door_width
    door_hight
    door_color
    door_x
    door_y 
    roof_hight
    roof_color
    """
    door_x = walls_x + (walls_width / 2) - (door_hight / 2)
    door_y = walls_y
    draw_walls(walls_x, walls_y, walls_width, walls_height, walls_color)
    draw_door(door_x, door_y, door_width, door_hight, door_color)
    draw_roof(roof_hight, roof_hight)
    roof_x = walls_x
    roof_y = walls_y + walls_height
    roof_side = math.sqrt(roof_hight ** 2 + (walls_width / 2) ** 2)
    roof_angle = math.degrees(math.atan(roof_hight / (walls_width / 2)))

def draw_walls(walls_x, walls_y, walls_width, walls_height, walls_color):
    t.penup()
    t.goto(walls_x, walls_y)
    t.pendown()
    t.fillcolor(walls_color)
    t.begin_fill()
    for i in range(2):
        t.fd(walls_width)
        t.left(90)
        t.fd(walls_height)
        t.left(90)
    t.end_fill()


def draw_door(door_x, door_y, door_hight, door_width, door_color):
    t.penup()
    t.goto(door_x, door_y)
    t.pendown()
    t.fillcolor(door_color)
    t.begin_fill()
    for i in range(2):
        t.fd(door_width)
        t.left(90)
        t.fd(door_hight)
        t.left(90)
    t.end_fill()

def draw_roof():
    t.penup()
    t.goto(roof_x, roof_y)
    t.pendown()
    t.fillcolor(roof_color)
    t.begin_fill()
    t.left(roof_angle * 2)
    t.fd(roof_side)
    t.right(roof_angle * 2)
    t.fd(roof_angle)
    t.end_fill()


draw_house(-100, 0, 200, 150, "#00ffff", 70, 50, "#ffff00", 100, "#ff00ff")
t.done()