"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk
import tkinter as tk
window = Tk()
window.withdraw()

number_1=simpledialog.askinteger(title='Task',prompt='Enter a number')
number_2=simpledialog.askinteger(title='Task',prompt='Enter another number')
choice=simpledialog.askstring(title='Choice',prompt='Would you like to add, subtract, multiply, or divide these numbers')
if choice==('add'):
    sum=number_1+number_2
    messagebox.showinfo(title='Answer',message=sum)
elif choice==('subtract'):
    difference=number_1-number_2
    messagebox.showinfo(title='Answer',message=difference)
elif choice==('multiply'):
    product=number_1*number_2
    messagebox.showinfo(title='Answer', message=product)
elif choice==('divide'):
    division_answer=number_1/number_2
    messagebox.showinfo(title='Answer',message=division_answer)


