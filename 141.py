# Challenge 141

import sqlite3

con = sqlite3.connect("BookInfo.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Authors(
    name text NOT NULL,
    birth_place TEXT NOT NULL);
""")

for _ in range(4):
    name = input("Name: ")
    place = input("Place of birth: ")
    cur.execute("INSERT INTO Authors VALUES(?,?)", (name, place))

cur.execute("""CREATE TABLE IF NOT EXISTS Books(
    id INTEGER PRIMARY KEY,
    title text NOT NULL,
    author text NOT NULL,
    year_published integer);
""")

for i in range(1, 13):
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year published: "))
    cur.execute("INSERT INTO Books VALUES(?,?,?,?)", (i,title,author,year))

cur.execute("SELECT * FROM Authors;")
for i in cur.fetchall(): print(i)
print()
cur.execute("SELECT * FROM Books;")
for i in cur.fetchall(): print(i)

con.commit()
con.close()