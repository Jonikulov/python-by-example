# Challenge 124

from tkinter import *

def hello_name():
    name = entry_box.get()
    out_box['text'] = f"Hello {name}!"

window = Tk()
window.geometry("300x220")
window.title("Hello!")

label = Label(text="Enter your name:", font=("", 13))
label.place(x=70, y=30)

entry_box = Entry(font=("", 14), justify='center')
entry_box.place(x=50, y=55, width=200)
entry_box.focus()

button = Button(text='Submit', command=hello_name)
button.place(x=100, y=90, width=100)

out_box = Label(text="", font=("Georgia", 15), bg='white', fg='blue')
out_box.place(x=50, y=130, width=200)

window.mainloop()