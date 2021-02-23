from turtle import Turtle, Screen
import  random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']




# # tim object
# tim = Turtle(shape='turtle')
# tim.penup()
# tim.color(user_bet)
# tim.goto(x=-230, y=0)
#
# # dom object
# dom = Turtle(shape='turtle')
# dom.penup()
# dom.color(colors[0])
# dom.goto(x=-230, y=100)
#
# # ram object
# ram = Turtle(shape='turtle')
# ram.penup()
# ram.color(colors[1])
# ram.goto(x=-230, y=180)
#
# # john object
# john = Turtle(shape='turtle')
# john.penup()
# john.color(colors[2])
# john.goto(x=-230, y=-100)
#
# # jay object
# jay = Turtle(shape='turtle')
# jay.penup()
# jay.color(colors[3])
# jay.goto(x=-230, y=-180)

# Smart way
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've loss! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()


