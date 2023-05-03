# Challenge 136

from tkinter import *

def add_name():
    data = name_box.get() + ", " + gen_sel.get()
    name_list.insert(END, data)
    name_box.delete(0, END)

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

btn = Button(text="Add", command=add_name, width=15)
btn.place(x=117, y=90)

name_list = Listbox()
name_list.place(x=15, y=130, relwidth=0.9, height=150)

root.mainloop()