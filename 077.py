# Challenge 077

people = []
response = 'y'
while response == 'y':
    guest = input("Enter a guest name: ").lower()
    people.append(guest)
    if len(people) >= 3:
        response = input("Do you want to invite another guess?(y/n) ")
print(f"You have invited {len(people)} people to the party.")
print(people)
person = input("Enter a name from the list: ").lower()
idx = people.index(person)
print(idx)
answer = input("Do you still want this person to come to the party? (y/n) ")
if answer == 'n':
    del people[idx]
    print(people)