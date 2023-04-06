# Challenge 041

name = input("Enter your name: ")
num = int(input("Enter a number: "))
if num < 10:
    for _ in range(num): print(name)
else:
    for _ in range(3): print("Too high.")