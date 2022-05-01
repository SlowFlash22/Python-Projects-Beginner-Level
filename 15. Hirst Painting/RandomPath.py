from turtle import Turtle, Screen
from random import random, choice

tim_the_turtle = Turtle()
tim_the_turtle.shape("turtle")


def draw(angles):
    for x in range(100):
        tim_the_turtle.color((random(), random(), random()))
        tim_the_turtle.forward(20)
        choice(angles)(90)


tim_the_turtle.pensize(8)
tim_the_turtle.speed(0)
tim_the_turtle.pendown()
tim_the_turtle.ht()
u = [tim_the_turtle.left, tim_the_turtle.right]
draw(u)
screen = Screen()
screen.exitonclick()
