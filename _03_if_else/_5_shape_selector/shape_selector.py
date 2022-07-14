import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    turtle_draw=turtle.Turtle()
    turtle_draw.hideturtle()
    # Ask the user what shape they want to draw and store it in a variable
    answer=simpledialog.askstring(title='Which shape?', prompt='triangle, square, or circle')
    # Draw the shape requested by the user using if-elif-else statements
    if answer==('triangle'):
        for i in range(3):
            turtle_draw.forward(100)
            turtle_draw.left(360/3)
    elif answer==('square'):
        for i in range(4):
            turtle_draw.forward(100)
            turtle_draw.left(360/4)
    elif answer==('circle'):
        turtle_draw.circle(75)
    # Call the turtle .done() method
    turtle.done()
