# Challenge 043

direction = input("Which direction do you want to count (up/down)? ")
if direction.lower() == "up":
    num = int(input("Enter the top number: "))
    for i in range(1, num+1):
        print(i)
elif direction.lower() == "down":
    num = int(input("Enter a number below 20: "))
    for i in range(20, num-1, -1): print(i)
else:
    print("I don't understand.")