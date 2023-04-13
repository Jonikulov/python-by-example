# Challenge 108

name = input("Enter a new name: ")

with open("Names.txt", 'a') as file:
    file.write('\n' + name)

with open("Names.txt", 'r') as file:
    print(file.read())