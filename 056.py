# Challenge 056

import random

number = random.randint(1, 10)
while True:
    guess = int(input("Guess the number: "))
    if guess == number:
        break