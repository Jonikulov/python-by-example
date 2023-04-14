# Challenge 112

import csv

book = input("Enter a book name: ")
author = input("Enter an author name: ")
year = input("Enter a year released: ")

with open("Books.csv", 'a') as file:
    row = ",".join([book, author, year])
    file.write(row + '\n')

print()
reader = csv.reader(open("Books.csv", 'r'))
for row in reader:
    print(" | ".join(row))