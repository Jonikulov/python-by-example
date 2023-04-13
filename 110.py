# Challenge 110

with open("Names.txt", 'r') as file:
    names = file.read().split()
print(names)

name = input("Enter a name from the list: ")
names.remove(name)
data = "\n".join(names)

with open("Names2.txt", 'w') as file:
    file.write(data)