#####Turtle Intro######

import turtle as t
from turtle import Screen

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("black")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)

# ------------------------------------------

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# ------------------------------------------

# ==> because we're programmers and we're lazy and we don't like looking at repeated code, a much simpler way of doing this is to simply create a for loop.

for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()




