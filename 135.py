# Challenge 135

from tkinter import *

def change_color():
    color = sel_col.get()
    root.config(background=color)

root = Tk()
root.geometry("250x200")

sel_col = StringVar(root)
sel_col.set("Select Color")
colors = ['red', 'green', 'blue', 'orange', 'yellow', 'lime', 'cyan']
col_menu = OptionMenu(root, sel_col, *colors)
col_menu.place(relx=0.5, y=25, anchor='center')

btn = Button(text="Click me", command=change_color, width=15)
btn.place(relx=0.5, y=60, anchor='center')

root.mainloop()