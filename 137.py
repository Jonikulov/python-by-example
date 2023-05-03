# Challenge 137

from tkinter import *

def add_name():
    data = name_box.get() + ", " + gen_sel.get()
    name_list.insert(END, data)
    name_box.delete(0, END)

    with open("names_genders.txt", 'a') as file:
        file.write(data + '\n')

def display_file():
    with open("names_genders.txt") as file:
        data = file.read().split('\n')
    for i in data: print(i)

root = Tk()
root.geometry("350x300")
root.title("Name & Gender List")

name_label = Label(text="Enter your name:")
name_label.place(x=15, y=15)

name_box = Entry(justify='center', width=30)
name_box.place(x=130, y=15)
name_box.focus()

gen_sel = StringVar(root)
gen_sel.set("Select Gender")
gender_menu = OptionMenu(root, gen_sel, "Male", "Female")
gender_menu.place(x=117, y=50)

add_btn = Button(text="Add", command=add_name, width=15)
add_btn.place(x=50, y=90)

name_list = Listbox()
name_list.place(x=15, y=130, relwidth=0.9, height=150)

display_btn = Button(text="Display", command=display_file, width=15)
display_btn.place(x=180, y=90)

root.mainloop()