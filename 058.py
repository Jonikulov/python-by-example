# Challenge 058

import random

questions = 5
score = 0
for _ in range(questions):
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    answer = int(input(f"{num1} + {num2} = "))
    if answer == num1+num2:
        score += 1
print(f"You've got {score} correct out of {questions}.")