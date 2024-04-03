from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_input = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "darkblue", "firebrick",
          "gray", "brown"]

turtle_pack = []
x = -230
y = -130
anonymous_start = [-230, -220, -210, -200]
anonymous_speed = ["slowest", "slow", "normal"]


def make_turtle(y_component):
    # Assigns new turtle and its position
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(random.choice(colors))
    new_turtle.penup()
    new_turtle.goto(x=random.choice(anonymous_start), y=y_component)
    new_turtle.speed(random.choice(anonymous_speed))
    turtle_pack.append(new_turtle)
    return y_component


for _ in range(6):
    y = make_turtle(y)+60

if user_input:
    is_race_on = True
else:
    is_race_on = False
    print("Program crashed due to invalid input, thus race can't be started")

while is_race_on:
    for turtle in turtle_pack:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_input:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winner_color} turtle is the winner! ")
            break
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


screen.exitonclick()
