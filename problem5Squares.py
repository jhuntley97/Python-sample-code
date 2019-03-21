# Jwaun Huntley
# 2/28/19

# Draws a set of concentric squares

import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

jwaun = turtle.Turtle()
jwaun.color("blue")

drawSquare(jwaun, 100)

wn.exitonclick()
