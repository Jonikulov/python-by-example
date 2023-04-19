# Challenge 125

import random
from tkinter import *

def roll_die():
    num = random.randint(1, 6)
    output['text'] = num

window = Tk()
window.geometry("250x150")
window.title("Roll a Die.")

label = Label(text='Roll a 6 sided die.', font=("", 15))
label.place(y=20, relwidth=1)

button = Button(text='Roll!', command=roll_die)
button.place(relx=0.5, y=65, anchor='center', width=50)

output = Message(text="", bg='white', font=("", 15))
output.place(relx=0.5, y=100, width=30, anchor='center')

window.mainloop()