from turtle import Turtle, Screen
import random

benget = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        benget.forward(100)
        benget.right(angle)


for shape_side_n in range(1, 11):
    benget.color(random.choice(colours))
    draw_shape(shape_side_n)








my_screen = Screen()
my_screen.exitonclick()