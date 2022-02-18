from turtle import Turtle, Screen, colormode
import random


t = Turtle()
c = colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple = (r, g, b)
    return tuple


direction = [0, 90, 180, 270]
t.pensize(10)
t.speed("fastest")

for _ in range(100):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(direction))



my_screen = Screen()
my_screen.exitonclick()