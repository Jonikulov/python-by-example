# Challenge 119

import random

def generate_number():
    low = int(input("Enter a low number: "))
    high = int(input("Enter a high number: "))
    return random.randint(low, high)

def user_guess():
    print("I am thinking of a number...")
    return int(input("Guess the number: "))

def check_answer(comp_num, user_num):
    while True:
        if user_num == comp_num:
            print("Correct, you win.")
            break
        elif user_num > comp_num:
            user_num = int(input("Too high. Try again: "))
        else:
            user_num = int(input("Too low. Try again: "))

comp_num = generate_number()
user_num = user_guess()
check_answer(comp_num, user_num)