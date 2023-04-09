# Challenge 066

import random
import turtle

colors = ['red', 'green', 'blue', 'black', 'orange', 'lime']
turtle.width(5)

for _ in range(8):
    turtle.color(random.choice(colors))
    turtle.forward(100)
    turtle.right(45)

turtle.hideturtle()
turtle.exitonclick()