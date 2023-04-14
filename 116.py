# Challenge 116

import csv

reader = csv.reader(open("Books.csv"))
book_list = list(reader)
for i, row in enumerate(book_list):
    print(f'{i}.', row)

selection = int(input("Which row to remove (enter a row number): "))
del book_list[selection]

for i, row in enumerate(book_list):
    print(f'{i}.', row)
selection = int(input("Which data to change (enter a row number): "))
del book_list[selection]

book = input("Enter a book name: ")
author = input("Enter an author name: ")
year = input("Enter a year released: ")
book_list.append([book, author, year])

with open("Books.csv", 'w') as file:
    for row in book_list:
        file.write(",".join(row) + '\n')