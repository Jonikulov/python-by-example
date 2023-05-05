from tkinter import *

root = Tk()
root.geometry("550x500")
root.title("Application")
root.wm_iconbitmap("robot.ico")
root.config(background="light green")

photo = PhotoImage(file="main-image.png")
logoimage = Label(image=photo)
logoimage.place(x=15, y=15)

select_name = StringVar(root)
select_name.set("Select Name")
name_list = OptionMenu(root, select_name, "Bob", "Sue", "Tim")
name_list.place(x=400, y=100)

def clicked():
    sel = select_name.get()
    msg_label["text"] = "Hello " + sel
    if sel == "Bob":
        photo = PhotoImage(file="ai-robot.png")
        logoimage.image = photo
    elif sel == "Sue":
        photo = PhotoImage(file="copilot-header.png")
        logoimage.image = photo
    elif sel == "Tim":
        photo = PhotoImage(file="robot-ico.png")
        logoimage.image = photo
    else:
        photo = PhotoImage(file="main-image.png")
        logoimage.image = photo

    logoimage["image"] = photo
    # logoimage.update()

click_btn = Button(text="Click", command=clicked)
click_btn.place(x=400, y=150)

msg_label = Label(text="Hello")
msg_label.place(x=400, y=200)

root.mainloop()