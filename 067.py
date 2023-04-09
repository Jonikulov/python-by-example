# Challenge 067

import turtle

turtle.speed(0)

for _ in range(10):
    turtle.right(36)
    for _ in range(8):
        turtle.forward(100)
        turtle.right(45)

turtle.hideturtle()
turtle.exitonclick()