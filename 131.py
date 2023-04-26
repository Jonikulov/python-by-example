# Challenge 131

from tkinter import *

def add_data():
    name = name_box.get()
    age = age_box.get()
    
    if name and age:
        name_box.delete(0, END)
        age_box.delete(0, END)

        data = name + ',' + age
        with open("names_ages.csv", 'a') as file:
            file.write(data + '\n')

        name_box.focus()

window = Tk()
window.geometry("350x200")
window.title("Enter Data")

name_label = Label(text="Enter a name:", font=('', 12))
name_label.place(x=20, y=20)

age_label = Label(text="Enter an age:", font=('', 12))
age_label.place(x=20, y=50)

name_box = Entry(font=('', 12), justify='center')
name_box.place(x=140, y=20)
name_box.focus()

age_box = Entry(font=('', 12), justify='center')
age_box.place(x=140, y=50)

add_button = Button(text="Add", command=add_data,
                    width=15, bg='green', fg='white')
add_button.place(x=120, y=100)

window.mainloop()