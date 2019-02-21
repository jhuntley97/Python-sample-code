import turtle       #set up jwaun
wn = turtle.Screen()
jwaun = turtle.Turtle()

sideNumber = int(input("How many side?"))

sideLength = int(input("How long length"))

angle = 360 / sideNumber


for x in range (sideNumber):
    jwaun.forward(sideLength)
    jwaun.left(angle)

wn.exitonclick()   
