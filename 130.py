# Challenge 130

from tkinter import *

def add_number():
    num = entry_box.get()
    if num.isdigit():
        entry_box.delete(0, END)
        num_list.insert(END, num)
    else:
        entry_box.delete(0, END)

def clear_list():
    num_list.delete(0, END)

def save_list():
    tmp_list = num_list.get(0, END)
    numbers = ",".join(tmp_list)
    with open("numbers.csv", 'w', encoding="utf-8") as file:
        file.write(numbers)

window = Tk()
window.geometry("400x250")
window.title("Number List")

entry_box = Entry(font=('', 15), justify='center')
entry_box.place(relx=0.5, y=25, anchor='center')
entry_box.focus()

add_buttton = Button(text='Add', command=add_number, width=10, font=('', 11),
                    bg='green', fg='white')
add_buttton.place(relx=0.25, y=60, anchor='center')

clear_button = Button(text='Clear', command=clear_list, width=10, font=('', 11),
                    bg='red', fg='white')
clear_button.place(relx=0.55, y=60, anchor='center')

save_button = Button(text='Save List', command=save_list, width=10,
                    font=('', 11), bg='orange', fg='white')
save_button.place(relx=0.85, y=60, anchor='center')

num_list = Listbox()
num_list.place(relx=0.5, y=160, relwidth=0.7, relheight=0.6, anchor='center')

window.mainloop()