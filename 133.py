# Challenge 133

from tkinter import *

def display_msg():
    name = name_box.get()
    name_box.delete(0, END)
    msg_box['text'] = "Hello " + name

root = Tk()
root.geometry("400x350")
root.title("Names")
root.iconbitmap("robot.ico")
root.config(background="black")

photo = PhotoImage(file="main-image.png")
main_image = Label(image=photo)
main_image.place(x=20, y=10)

name_label = Label(text="Enter your name:", bg='black', fg='white')
name_label.place(x=35, y=270)

name_box = Entry(width=35, justify='center')
name_box.place(x=135, y=270)
name_box.focus()

button = Button(text="Press me", command=display_msg, bg='grey', width=12)
button.place(x=35, y=305)

msg_box = Label(width=30)
msg_box.place(x=135, y=305)

root.mainloop()