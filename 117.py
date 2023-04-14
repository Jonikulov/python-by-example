# Challenge 117

"""Create a simple maths quiz that will ask the user for their name and then generate two
random questions. Store their name, the questions they were asked, their answers and
their final score in a .csv file. Whenever the program is run it should add to the .csv file
and not overwrite anything."""

import random

score = 0
name = input("Enter your name: ")
file = open("math_quiz.csv", 'a')
file.write(name + ',')

for i in range(1, 3):
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    quiz = f"{num1} * {num2} = "
    answer = input(f"{i}) {quiz}")
    if int(answer) == num1 * num2:
        score += 1
    file.write(quiz + ',' + answer + ',')

file.write(str(score) + '\n')
file.close()