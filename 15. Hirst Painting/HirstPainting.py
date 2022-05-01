# ----------------------------
# For extracting colors from an image
#import random

#import colorgram

# colors = colorgram.extract("image.jpeg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)
# ----------------------------

from turtle import Turtle, Screen
from random import choice
color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]
painter = Turtle()
screen = Screen()
screen.colormode(255)
painter.penup()
painter.speed("fastest")
painter.setposition(-225, -200)
for y in range(10):
    for x in range(10):
        painter.pendown()
        painter.pencolor(choice(color_list))
        painter.dot(15, choice(color_list))
        painter.penup()
        painter.forward(50)
    painter.setposition(-225, painter.ycor()+50)
screen.exitonclick()
