# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# list_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tuple = (r, g, b)
#     list_color.append(new_tuple)
# print(list_color)

import turtle as t_module
import random

t = t_module.Turtle()
t_module.colormode(255)
t.speed("fastest")
t.hideturtle()
t.penup()

color_convert = [
    (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46),
    (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165),
    (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43),
    (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202),
    (52, 234, 243), (3, 67, 40)
]

t.setheading(225)
t.forward(300)
t.setheading(0)

number_dots = 100
for dot_count in range(1, number_dots + 1):
    t.dot(20, random.choice(color_convert))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)





my_screen = t_module.Screen()
my_screen.exitonclick()
