import turtle

import pandas as pd

TITLE = "U.S. States Game"
IMG = "blank_states_img.gif"
FILE_PATH = "50_states.csv"
REPORT_FILE_PATH = "states_to_learn.csv"


def get_guess(last_score):
    title = "Guess The State" if last_score == 0 else f"{last_score} / 50 State Correct"
    prompt = "What's another State's name (If you can't type \"Exit\")?"
    if last_score == 0:
        prompt = "What's State's name (If you can't type \"Exit\")?"
    return screen.textinput(title=title, prompt=prompt).title()


screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title(TITLE)
screen.addshape(IMG)

turtle.shape(IMG)

t = turtle.Turtle()
t.hideturtle()
t.penup()

data = pd.read_csv(FILE_PATH)
score = 0

while True:
    guess = get_guess(score)
    if guess == "Exit":
        data = data.drop(columns=["x", "y"])
        data.to_csv(REPORT_FILE_PATH)
        break

    answer = data[data.state == guess]
    if len(answer) == 1:
        t.goto(x=int(answer.x), y=int(answer.y))
        t.write(guess)
        data = data.drop(data[data.state == guess].index)
        score += 1
