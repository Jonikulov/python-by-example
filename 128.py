# Challenge 128

from tkinter import *

def convert():
    option = select_var.get()
    entry = float(entry_box.get())
    if option.startswith('km'):
        # convert km to mile
        out_msg['text'] = f'{entry * 0.6214:.3f}'
    else:
        # convert mile to km
        out_msg['text'] = f'{entry * 1.6093:.3f}'

window = Tk()
window.geometry("350x250")
window.title("Kilometer and Mile converter")

select_label = Label(text="Select an option:")
select_label.place(relx=0.30, y=50, anchor='center')

# Define options
options = ['km → mile', 'mile → km']
# Set the default option
select_var = StringVar(window)
select_var.set(options[0])

menu = OptionMenu(window, select_var, *options)
menu.place(relx=0.60, y=50, anchor='center')

entry_box = Entry(text=0, font=('', 15), bg='white')
entry_box.place(relx=0.3, y=120, anchor='center', width=120)
entry_box.focus()

out_msg = Message(text=0, font=('', 15), width=100)
out_msg.place(relx=0.75, y=120, anchor='center')

eq_label = Label(text='=', font=('', 20))
eq_label.place(relx=0.55, y=120, anchor='center')

convert = Button(text='CONVERT', command=convert, bg='orange')
convert.place(relx=0.5, y=180, anchor='center', width=100, height=30)

window.mainloop()