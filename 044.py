# Challenge 044

num = int(input("How many people do you want to invite: "))
if num < 10:
    for _ in range(num):
        name = input("Enter a name: ")
        print(name.title(), "has been invited.")
else:
    print("Too many people.")