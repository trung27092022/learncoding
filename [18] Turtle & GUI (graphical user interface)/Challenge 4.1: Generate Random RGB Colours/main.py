import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # create the/a tuple:
    random_color = (r, g, b)
    return random_color

direction = [0, 90, 100, 270]
tim.pensize(15)
tim.speed("fastest")

for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()