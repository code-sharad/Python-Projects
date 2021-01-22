import turtle as t

import random

t.colormode(255)
# from test2 import random_color

tim = t.Turtle()

tim.speed("fastest")

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(100):
    tim.pencolor(random_color())
    tim.left(angle=5)
    tim.circle(100)


screen = t.Screen()
screen.exitonclick()












