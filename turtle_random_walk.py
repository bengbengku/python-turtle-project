from turtle import Turtle, Screen
import random


t = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]
t.pensize(10)
t.speed("fastest")

for _ in range(100):
    t.color(random.choice(colours))
    t.forward(30)
    t.setheading(random.choice(direction))




my_screen = Screen()
my_screen.exitonclick()