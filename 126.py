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
entry_box.place(relx=0.5, rely=0.2, relwidth=0.4, anchor='center')
entry_box.focus()

add_button = Button(text='Add', command=add, bg='green')
add_button.place(relx=0.35, rely=0.45, relwidth=0.25, anchor='center')

reset_button = Button(text='Reset', command=reset, bg='red')
reset_button.place(relx=0.65, rely=0.45, relwidth=0.25, anchor='center')

result = Message(text=0, bg='#feffb8', font=("", 15))
result.place(relx=0.5, rely=0.75, width=100, anchor='center')

window.mainloop()