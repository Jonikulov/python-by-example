# Challenge 150: Art Gallery

import sqlite3
from tkinter import *

con = sqlite3.connect("ArtGallery.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS artists(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT,
        town TEXT,
        county TEXT,
        postcode TEXT);
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS arts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        artist_id INTEGER,
        title TEXT NOT NULL,
        medium TEXT NOT NULL,
        price INTEGER NOT NULL,
        FOREIGN KEY(artist_id) REFERENCES artists(id));
""")

def add_data():
    name = name_box.get()
    address = address_box.get()
    town = town_box.get()
    county = county_box.get()
    postcode = postcode_box.get()
    title = title_box.get()
    medium = medium_box.get()
    price = int(price_box.get())
    cur.execute("""INSERT INTO artists(name,address,town,county,postcode)
                    VALUES(?,?,?,?,?)""", (name,address,town,county,postcode))
    cur.execute("SELECT id FROM artists WHERE name=?", [name])
    artist_id = cur.fetchone()[0]
    cur.execute("""INSERT INTO arts(artist_id,title,medium,price)
                    VALUES(?,?,?,?)""", (artist_id,title,medium,price))
    con.commit()
    add_btn["bg"] = "orange"


def clear_entry():
    name_box.delete(0, END)
    address_box.delete(0, END)
    town_box.delete(0, END)
    county_box.delete(0, END)
    postcode_box.delete(0, END)
    title_box.delete(0, END)
    medium_box.delete(0, END)
    price_box.delete(0, END)
    name_box.focus()
    add_btn["bg"] = "SystemButtonFace"


root = Tk()
root.geometry("400x300")
root.title("Art Gallery")

name_label = Label(text="Artist:")
name_label.place(x=20, y=15)

name_box = Entry(width=30, justify='center')
name_box.place(x=90, y=15)
name_box.focus()

address_label = Label(text="Address:")
address_label.place(x=20, y=40)

address_box = Entry(width=30, justify='center')
address_box.place(x=90, y=40)

town_label = Label(text="Town:")
town_label.place(x=20, y=65)

town_box = Entry(width=30, justify='center')
town_box.place(x=90, y=65)

county_label = Label(text="County:")
county_label.place(x=20, y=90)

county_box = Entry(width=30, justify='center')
county_box.place(x=90, y=90)

postcode_label = Label(text="Postcode:")
postcode_label.place(x=20, y=115)

postcode_box = Entry(width=30, justify='center')
postcode_box.place(x=90, y=115)

title_label = Label(text="Title:")
title_label.place(x=20, y=140)

title_box = Entry(width=30, justify='center')
title_box.place(x=90, y=140)

medium_label = Label(text="Medium:")
medium_label.place(x=20, y=165)

medium_box = Entry(width=30, justify='center')
medium_box.place(x=90, y=165)

price_label = Label(text="Price:")
price_label.place(x=20, y=190)

price_box = Entry(width=30, justify='center')
price_box.place(x=90, y=190)

add_btn = Button(text="Add", command=add_data, width=10)
add_btn.place(x=100, y=230)

clear_btn = Button(text="Clear", command=clear_entry, width=10)
clear_btn.place(x=200, y=230)

root.mainloop()

cur.execute("SELECT * FROM artists")
for x in cur.fetchall(): print(x)
print()
cur.execute("SELECT * FROM arts")
for x in cur.fetchall(): print(x)

con.close()