"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk
import tkinter as tk
window = Tk()
window.withdraw()
score=0

answer_1=simpledialog.askstring(title='Riddle 1',prompt='What room do ghosts avoid?')
if (answer_1==('the living room') or answer_1==('The living room')):
    score=(score+1)
else:
    score=(score+0)
answer_2=simpledialog.askstring(title='Riddle 2',prompt='What has many keys, but can\'t even open a single door?')
if (answer_2==('a piano') or answer_2==('piano')):
    score=(score+1)
else:
    score=(score+0)
answer_3=simpledialog.askstring(title='Riddle 3', prompt='I am not alive, but I grow; I don\'t have lungs, but I need air; I don\'t have a mouth, but water kills me. What am I?')
if (answer_3==('fire') or answer_3==('Fire')):
    score=(score+1)
else:
    score=(score+0)
print(score)
messagebox.showinfo(title='answers', message='1, the living room 2, a piano 3, fire')






