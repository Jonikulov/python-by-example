# Challenge 048

count = 0
response = "y"
while response == "y":
    name = input("Enter a name: ")
    print(name, "has now been invited.")
    count += 1
    response = input("Do you want to invite somebody else? (y/n) ")
print(count, "people coming to the party.")