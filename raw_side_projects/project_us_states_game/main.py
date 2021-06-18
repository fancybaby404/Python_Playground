import turtle
import pandas
import datetime


# ---------- Functions ---------- #
def get_x(state):
    values = data[data["state"] == state]
    x = values.x.item()
    return x


def get_y(state):
    values = data[data["state"] == state]
    y = values.y.item()
    return y


def state_exist(state):
    listed_states = data.state.to_list()
    if state in listed_states:
        return True
    else:
        return False


# ---------- Initialization ---------- #
FONT = "Times New Roman", 7, "normal"

screen = turtle.Screen()
screen.title("U.S States?")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

# ---------- Main Game ---------- #
today = datetime.date.today()
score = 0

game_data = {
    "Date": [today],
    "Score": [score],
}
answered_states = []
while not len(answered_states) == 49:
    answer_state = screen.textinput(title=f"{game_data['Score'][0]}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # Normal Style:
        # with open("states_to_learn.csv", mode="w") as learn:
        #     for states in data.state:
        #         if states not in answered_states:
        #             learn.write(f"{states}\n")

        # Pandas Style (states to learn):
        missing_states = [state for state in data.state if state not in answered_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if state_exist(answer_state) and answer_state not in answered_states:
        game_data['Score'][0] += 1
        answered_states.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.ht()
        new_turtle.penup()
        new_turtle.goto(get_x(answer_state), get_y(answer_state))
        new_turtle.color("black")
        new_turtle.write(arg=answer_state, move=False, font=FONT)
        continue

# Save Scores (save scores):
import os.path

file_exist = os.path.isfile("history_scores.csv")

if not file_exist:
    print(f"File does not exist\n Creating...")
    pandas.DataFrame(game_data).to_csv("history_scores.csv", index=False)
else:
    df1 = pandas.read_csv("history_scores.csv")
    df2 = pandas.DataFrame(game_data)

    final = [df1, df2]
    pandas.concat(final, ignore_index=True).to_csv("history_scores.csv", index=False)
