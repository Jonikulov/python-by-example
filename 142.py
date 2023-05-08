# Challenge 142

import sqlite3

con = sqlite3.connect("BookInfo.db")
cur = con.cursor()

cur.execute("SELECT * FROM authors")
for x in cur.fetchall(): print(x)

place = input("\nEnter a place of birth: ")
cur.execute("SELECT name FROM Authors WHERE birth_place=?", [place])
authors = [author[0] for author in cur.fetchall()]
print()

if len(authors) == 1:
    cur.execute(f"""SELECT title, year_published, author
        FROM books WHERE author='{authors[0]}'""")
    for x in cur.fetchall(): print(x)
elif len(authors) > 1:
    cur.execute(f"""SELECT title, year_published, author
        FROM books WHERE author IN {tuple(authors)}""")
    for x in cur.fetchall(): print(x)

con.close()