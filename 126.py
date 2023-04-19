# Challenge 126

from tkinter import *

def add():
    num = int(entry_box.get())
    answer = int(result['text'])
    result['text'] = num + answer

def reset():
    entry_box.delete(0, END)
    result['text'] = 0

window = Tk()
window.geometry('250x150')
window.title('Addition')

entry_box = Entry(font=('', 16), justify='center')
entry_box.place(relwidth=0.4, relx=0.5, rely=0.2, anchor='center')
entry_box.focus()

add_button = Button(text='Add', command=add, bg='#40eb34')
add_button.place(relwidth=0.25, relx=0.35, rely=0.45, anchor='center')

reset_button = Button(text='Reset', command=reset, bg='#eb3434')
reset_button.place(relwidth=0.25, relx=0.65, rely=0.45, anchor='center')

result = Message(text=0, bg='#feffb8', font=("", 15))
result.place(width=100, relx=0.5, rely=0.75, anchor=CENTER)

window.mainloop()