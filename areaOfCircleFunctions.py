import math

#Jwaun Huntley
#2/28/19

#Calculates the area of a circle

#Function receieves radius and calculates area of a circle
def areaOfCircle(radius):
    area = (radius**2) * math.pi
    return area

#x = areaOfCircle(10)

print("The area of the circle is", areaOfCircle(10))

print("The area of the circle is", areaOfCircle(30))

print("The area of the circle is", areaOfCircle(40))
