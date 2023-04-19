# Challenge 127

from tkinter import *

def add():
    name = entry_box.get()
    if name:
        name_list.insert(END, name)
        entry_box.delete(0, END)

def clear():
    name_list.delete(0, END)
    entry_box.focus()

window = Tk()
window.geometry("500x300")
window.title("Names List")

label = Label(text='Enter your name:', font=('', 13), justify='center')
label.place(y=10, relwidth=1)

entry_box = Entry(font=('', 13), justify='center')
entry_box.place(relx=0.5, y=50, relwidth=0.7, anchor='center')
entry_box.focus()

add_button = Button(text='Add', command=add, bg='green')
add_button.place(relx=0.7, y=90, relwidth=0.3, anchor='center')

clear_button = Button(text='Clear', command=clear, bg='red')
clear_button.place(relx=0.3, y=90, relwidth=0.3, anchor='center')

name_list = Listbox(font=('', 12))
name_list.place(relx=0.5, y=190, relwidth=0.7, height=150, anchor='center')

window.mainloop()