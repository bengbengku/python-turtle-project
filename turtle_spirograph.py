from turtle import Turtle, Screen, colormode
import random
t = Turtle()

c = colormode(255)

t.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_gap):
    for _ in range(int(360/size_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_gap)

draw_spirograph(5)

my_screen = Screen()
my_screen.exitonclick()