# Challenge 054
import random

r_choice = random.choice(['h', 't'])
user_choice = input("Choose heads or tail (h/t): ")
if r_choice == user_choice:
    print("You win!")
else:
    print("Bad luck.")