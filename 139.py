# Challenge 139

import sqlite3

con = sqlite3.connect("PhoneBook.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS names(
    id integer PRIMARY KEY,
    first_name text NOT NULL,
    surname text,
    phone_number text NOT NULL);
""")

for i in range(1, 6):
    name = input("First Name: ")
    surname = input("Surname: ")
    phone = input("Phone Number: ")
    cur.execute("INSERT INTO names VALUES(?,?,?,?)", (i,name,surname,phone))
    print()

for x in cur.execute("SELECT * FROM names"):
    print(x)

con.commit()
con.close()