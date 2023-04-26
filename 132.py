# Challenge 132

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

def display_data():
    list_box = Listbox(font=('', 11))
    list_box.place(x=10, y=165, width=330)
    list_box.insert(END, ('Name', 'Age'))

    import csv
    reader = csv.reader(open("names_ages.csv"))
    for row in reader:
        list_box.insert(END, (row[0], row[1]))

window = Tk()
window.geometry("350x370")
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
add_button.place(x=120, y=95)

display_button = Button(text="Display", command=display_data,
                    width=15, bg='orange', fg='white')
display_button.place(x=120, y=130)

window.mainloop()