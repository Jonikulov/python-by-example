# Challenge 113

import csv

records = int(input("How many records do you want to add: "))
# Adding new records.
with open("Books.csv", 'a') as file:
    for _ in range(records):
        book = input("Enter a book name: ")
        author = input("Enter an author name: ")
        year = input("Enter a year released: ")
        print()
        row = ",".join([book, author, year])
        file.write(row + '\n')

# Displaying author books.
author = input("Which author's books do you want: ")
reader = csv.reader(open("Books.csv"))
author_available = False
for row in reader:
    if author in row[1]:
        print(" | ".join(row))
        author_available = True

# Tell this author is not available.
if not author_available:
    print("This author is not available in the list.")