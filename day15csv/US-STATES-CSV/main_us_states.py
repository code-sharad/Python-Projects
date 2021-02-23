import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# print(states_50)
screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 the State",
                                    prompt="What's another state's name? ".title())
    if answer_state == "Exit":
        missed_state = []
        for state in all_states:
            if state not in guess_states:
                missed_state.append(state)

        new_data = pandas.DataFrame(missed_state)
        new_data.to_csv("new_state_to_learn.csv")

        break
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)





screen.exitonclick()
