# Challenge 076

people = []
response = 'y'
while response == 'y':
    guest = input("Enter a guest name: ")
    people.append(guest)
    if len(people) >= 3:
        response = input("Do you want to invite another guess?(y/n) ")
print(f"You have invited {len(people)} people to the party.")