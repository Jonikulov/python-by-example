# Challenge 068

import random
import turtle

lines = random.randint(10, 30)
for _ in range(lines):
    length = random.randint(10, 50)
    angle = random.randint(-175, 175)
    turtle.forward(length)
    turtle.right(angle)

turtle.hideturtle()
turtle.exitonclick()