# Challenge 050

while True:
    num = int(input("Enter a number between 10 and 20: "))
    if num > 20:
        print("Too high.")
    elif num < 10:
        print("Too low.")
    else:
        print("Thank you.")
        break