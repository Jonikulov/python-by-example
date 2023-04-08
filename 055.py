# Challenge 055

import random

r_num = random.randint(1, 5)
user_num = int(input("Guess the number: "))

if user_num == r_num:
    print("Well done.")
elif user_num > r_num:
    print("Too high.")
    user_num = int(input("Second guess: "))
    if user_num == r_num:
        print("Correct.")
    else:
        print("You lose.")
else:
    print("Too low.")
    user_num = int(input("Second guess: "))
    if user_num == r_num:
        print("Correct.")
    else:
        print("You lose.")