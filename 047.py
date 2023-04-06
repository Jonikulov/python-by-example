# Challenge 047

num = int(input("Enter a number: "))
total = num
response = "y"
while response == "y":
    num = int(input("Enter another number: "))
    total += num
    response = input("Do you want to add another number? (y/n) ")
print("Total:", total)