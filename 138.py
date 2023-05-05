# Challenge 138

from tkinter import *

def display_img():
    num = int(text_box.get())
    text_box.delete(0, END)
    img_dict = {0:"main-image.png",
                1:"ai-robot.png",
                2:"copilot-header.png",
                3:"robot-ico.png"
            }
    photo = PhotoImage(file=img_dict[num])
    img_label.image = photo
    img_label["image"] = photo

root = Tk()
root.geometry("360x550")

pic = PhotoImage(file="main-image.png")
img_label = Label(image=pic)
img_label.pack()

text_label = Label(text="Enter a number:")
text_label.pack()

text_box = Entry(justify='center')
text_box.pack()
text_box.focus()

btn = Button(text="Display", command=display_img)
btn.pack()

root.mainloop()