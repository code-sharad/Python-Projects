from turtle import Screen, Turtle
from paddle import *

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up ")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
