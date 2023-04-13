# Challenge 102

people = {}
for i in range(1, 5):
    name = input(f"Enter {i}-person's name: ")
    age = int(input(f"Enter {i}-person's age: "))
    shoe = int(input(f"Enter {i}-person's shoe size: "))
    print()
    people[name] = {'Age':age, 'Shoe_Size':shoe}

name = input("\nEnter a name in the list: ")
print(people[name])