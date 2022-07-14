# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

import turtle
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':


    window=Tk()
    window.withdraw()

    radius=simpledialog.askinteger(title='Task',prompt='Enter a radius')

    answer=simpledialog.askstring(title='circumference or area', prompt='Would you like to see the area or circumference of the circle')

    turtle_2=turtle.Turtle()

    turtle_2.circle(radius)

    turtle_2.penup()

    turtle_2.goto(0,0)

    area=math.pi*radius*radius

    circumference=math.pi*(radius+radius)

    if answer == ('area'):
        turtle_2.write(arg="area = " + str(area), move=True, align='left', font=('Arial',20,'normal'))
    elif answer == ('circumference'):
        turtle_2.write(arg="circumference = " + str(circumference), move=True, align='left', font=('Arial',20,'normal'))

    turtle_2.hideturtle()

    turtle.done()
