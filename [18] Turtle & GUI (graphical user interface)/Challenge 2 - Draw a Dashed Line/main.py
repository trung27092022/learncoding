import turtle as t
from turtle import Screen

tim = t.Turtle()
tim.shape("turtle")
tim.color("black")

def adashedline():
    for i in range(20):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

adashedline()

screen = Screen()
screen.exitonclick()
########### Challenge 2 - Draw a Dashed Line ########