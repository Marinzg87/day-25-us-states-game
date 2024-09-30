import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create the data frame
data = pandas.read_csv("50_states.csv")
# Create series and change it to list
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    gues_state = screen.textinput(title=f"{len(guessed_states)}/50 "
                                  f"Guess the State",
                                  prompt="What's another State's name?").title()

    if gues_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if gues_state in all_states:
        guessed_states.append(gues_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == gues_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

screen.mainloop()
