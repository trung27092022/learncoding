import turtle as t
import random

tim = t.Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 100, 270]
tim.pensize(15)
tim.speed("fastest")

for i in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(direction))
