from turtle import Turtle, Screen
from random import random
turt = Turtle()


def make_spirograph(difference_angle):
    for i in range(int(360/difference_angle)):
        turt.pencolor((random(), random(), random()))
        turt.circle(150)
        turt.setheading(turt.heading()+difference_angle)


turt.speed("fastest")
turt.hideturtle()
make_spirograph(5)
screen = Screen()
screen.exitonclick()