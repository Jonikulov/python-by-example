# Challenge 149: Times Tables (GUI)

from tkinter import *

def display_times_table():
    table_box.delete(0, END)
    num = int(num_box.get())
    for i in range(1, 16):
        expr = f"{i} x {num} = {i*num}"
        table_box.insert(END, expr)
    num_box.focus()

def clear_all():
    num_box.delete(0, END)
    table_box.delete(0, END)
    num_box.focus()

root = Tk()
root.geometry("500x400")
root.title("Times Table")

enter_label = Label(text="Enter a number:", font=('', 12))
enter_label.place(x=30, y=25)

num_box = Entry(font=('', 12), justify='center', width=18)
num_box.place(x=150, y=27)
num_box.focus()

view_btn = Button(text="View Times Table",
                  command=display_times_table,
                  width=18,
                  bg='white')
view_btn.place(x=335, y=25)

clear_btn = Button(text="Clear",
                  command=clear_all,
                  width=18,
                  bg='white')
clear_btn.place(x=335, y=65)

table_box = Listbox(font=('', 12), width=18, height=15)
table_box.place(x=150, y=60)

root.mainloop()