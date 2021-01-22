import turtle as t
import random

tim = t.Turtle()

direction = [0, 90, 180, 270]

t.colormode(255)


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    random_color = (r, g, b)
    return random_color


tim.speed("fastest")
tim.width(10)

for _ in range(200):
    num_r = random.choice(direction)
    # tim.color(random.choice(colors))
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(num_r)
