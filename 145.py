# Challenge 145

import sqlite3
from tkinter import *

con = sqlite3.connect("TestScores.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS test_scores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    grade INTEGER NOT NULL);
""")

def add_data():
    name = name_box.get()
    grade = int(grade_box.get())
    cur.execute("INSERT INTO test_scores(name, grade) VALUES(?,?)",
                (name, grade))
    con.commit()
    add_btn["bg"] = "yellow"

def clear_window():
    name_box.delete(0, END)
    grade_box.delete(0, END)
    add_btn["bg"] = "SystemButtonFace"
    name_box.focus()

window = Tk()
window.geometry("350x200")
window.title("Test Scores")

name_label = Label(text="Enter student's name:")
name_label.place(x=15, y=30)

name_box = Entry(justify="center", width=30)
name_box.place(x=150, y=30)
name_box.focus()

grade_label = Label(text="Enter student's grade:")
grade_label.place(x=15, y=70)

grade_box = Entry(justify="center", width=30)
grade_box.place(x=150, y=70)

add_btn = Button(text="Add", command=add_data, width=10)
add_btn.place(x=90, y=110)

clear_btn = Button(text="Clear", command=clear_window, width=10)
clear_btn.place(x=200, y=110)

window.mainloop()

con.close()