# Challenge 063

import turtle

for c in ['red', 'black', 'green']:
    turtle.begin_fill()
    turtle.color(c)
    for _ in range(4):
        # Draw a square and fill it.
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    # Draw the gap.
    turtle.penup()
    turtle.forward(120)
    turtle.pendown()

turtle.exitonclick()