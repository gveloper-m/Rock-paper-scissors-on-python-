from tkinter import *

import random

def winner():
    winning = random.randint(1,3)
    print(winning)
    if winning == 1:
        text.delete(0,END)
        text.insert(0, "Rock beats scissors. Next time!")
    if winning == 2:
        text.delete(0,END)
        text.insert(0, "Paper loses from scissors. You won!")
    if winning == 3:
        text.delete(0,END)
        text.insert(0, "It's a tie")

def winner2():
    winning = random.randint(1,3)
    print(winning)
    if winning == 2:
        text.delete(0,END)
        text.insert(0, "Paper beats rock. Haha!")
    if winning == 3:
        text.delete(0,END)
        text.insert(0, "Rock beats scissors. You won!")
    if winning == 1:
        text.delete(0,END)
        text.insert(0, "It's a tie")

def winner3():
    winning = random.randint(1,3)
    print(winning)
    if winning == 1:
        text.delete(0,END)
        text.insert(0, "Paper beats rock.You won!")
    if winning == 2:
        text.delete(0,END)
        text.insert(0, "It's a tie!")
    if winning == 3:
        text.delete(0,END)
        text.insert(0, "Scissors beats paper. You lose!")




win=Tk()

sci=Button(win,text="scissors",fg='blue', command = winner)
sci.place(x=80, y=100)

rock=Button(win,text="rock",fg='blue',command= winner2)
rock.place(x=80, y=70)

paper=Button(win,text='paper',fg='blue',command = winner3)
paper.place(x=80, y=40)

text=Entry(win, text="Can you win?", fg='red', font=("Helvetica", 16))
text.place(x=245, y=50)



win.title('Rock,Paper,Scissors')
win.geometry("500x200+10+20")
win.mainloop()









