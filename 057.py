# Challenge 057

import random

number = random.randint(1, 10)
while True:
    guess = int(input("Guess the number: "))
    if guess == number:
        break
    elif guess > number:
        print("Too high.")
    else:
        print("Too low.")