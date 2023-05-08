# Challenge 144

import sqlite3

con = sqlite3.connect("BookInfo.db")
cur = con.cursor()

author = input("Enter author name: ")

cur.execute("SELECT * FROM Books WHERE author=?", [author])

with open("books.txt", 'w') as file:
    for row in cur.fetchall():
        row = " - ".join([str(i) for i in row])
        file.write(row + '\n')
    print("Saved to books.txt file.")

con.close()