# Challenge 140

import sqlite3

con = sqlite3.connect("PhoneBook.db")
cur = con.cursor()

menu = """
Main Menu:

1) View phone book
2) Add to phone book
3) Search for surname
4) Delete person from phone book
5) Quit

Enter your selection: """

selection = int(input(menu))
while selection != 5:

    if selection == 1:
        cur.execute("SELECT * FROM names")
        for x in cur.fetchall(): print(x)

    elif selection == 2:
        id_ = int(input("Enter ID: "))
        name = input("Enter first name: ")
        surname = input("Enter surname: ")
        phone_number = input("Enter phone number: ")
        cur.execute("INSERT INTO names VALUES(?,?,?,?)",
                    (id_,name,surname,phone_number))

    elif selection == 3:
        surname = input("Enter surname to search: ")
        cur.execute("SELECT * FROM names WHERE surname=?", [surname])
        for x in cur.fetchall(): print(x)

    elif selection == 4:
        id_ = int(input("Enter ID to delete: "))
        cur.execute("DELETE FROM names WHERE id=?", [id_])
    
    selection = int(input(menu))

con.commit()
con.close()