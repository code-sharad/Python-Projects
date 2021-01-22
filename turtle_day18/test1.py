from turtle import Turtle
from random import choice

tim = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

num_sides = 15
def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.left(angle)

for shape_side_n in range(3, 10):
    tim.color(choice(colors))
    draw_shape(shape_side_n)