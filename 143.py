# Challenge 143

import sqlite3

con = sqlite3.connect("BookInfo.db")
cur = con.cursor()

year = int(input("Enter year: "))
cur.execute("""SELECT * FROM Books WHERE year_published>=?
    ORDER BY year_published""", [year])
for x in cur.fetchall(): print(x)

con.close()