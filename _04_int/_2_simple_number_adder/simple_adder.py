"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk
import tkinter as tk
window = Tk()
window.withdraw()

number_1=simpledialog.askinteger(title='Task',prompt='Enter a number')
number_2=simpledialog.askinteger(title='Task',prompt='Enter another number')
sum=number_1+number_2
print(sum)
messagebox.showinfo(title='Sum',message=sum)
