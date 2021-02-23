from turtle import Turtle, Screen
from food import Food
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

food = Food()
# TODO: Create snake body

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# TODO: Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)

    for seg_num in range(start=2, stop=0, step=-1):
        segments[seg_num].goto()
# TODO: Create snake food

screen.exitonclick()
