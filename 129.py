# Challenge 129

from tkinter import *

def add():
    num = entry_box.get()
    if num.isdigit():
        entry_box.delete(0, END)
        num_list.insert(END, num)
    else:
        entry_box.delete(0, END)

def clear():
    num_list.delete(0, END)

window = Tk()
window.geometry("300x250")

entry_box = Entry(font=('', 15), justify='center')
entry_box.place(relx=0.5, y=25, anchor='center')
entry_box.focus()

add_buttton = Button(text='Add', command=add, width=10, font=('', 11),
                    bg='green', fg='white')
add_buttton.place(relx=0.3, y=60, anchor='center')

clear_button = Button(text='Clear', command=clear, width=10, font=('', 11),
                    bg='red', fg='white')
clear_button.place(relx=0.7, y=60, anchor='center')

num_list = Listbox()
num_list.place(relx=0.5, y=160, relwidth=0.7, relheight=0.6, anchor='center')

window.mainloop()