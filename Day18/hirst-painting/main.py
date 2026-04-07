# import colorgram
#
# colors = colorgram.extract('image.jpg', 1000)
# rgb_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_list.append(rgb_color)
# print(rgb_list)

from turtle import Turtle,Screen
from random import choice

karlu = Turtle()
screen = Screen()
screen.colormode(255)

color_list = [(235, 240, 246), (247, 240, 243), (240, 246, 243), (133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209), (65, 66, 56), (103, 140, 129), (164, 200, 214), (130, 129, 122)]
# Size 20, 10x10, space 50
karlu.speed("fastest")
karlu.penup()
karlu.setheading(225)
karlu.forward(250)
karlu.setheading(0)

for x in range(10):
    karlu.speed(2)
    for _ in range(10):
        if _ == 9:
            karlu.dot(20, choice(color_list))
            karlu.speed("fastest")
            karlu.setheading(90)
            karlu.forward(50)
            karlu.setheading(180)
            karlu.forward(450)
            karlu.setheading(360)
        else:
            karlu.dot(20, choice(color_list))
            karlu.forward(50)






screen.exitonclick()

