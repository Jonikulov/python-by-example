# Challenge 120

import random

def addition():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    user_ans = int(input(f"{num1} + {num2} = "))
    return user_ans, num1+num2

def subtraction():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    user_ans = int(input(f"{num1} - {num2} = "))
    return user_ans, num1-num2

def check_answer(user_ans, ans):
    if user_ans == ans:
        print("Correct.")
    else:
        print("Incorrect, the answer is", ans)

def main():
    option = int(input("1) Addition\n" \
                "2) Subtraction\n" \
                "Enter 1 or 2: "
            ))
    if option == 1:
        user_ans, ans = addition()
        check_answer(user_ans, ans)
    elif option == 2:
        user_ans, ans = subtraction()
        check_answer(user_ans, ans)
    else:
        print("Invalid option.")

main()