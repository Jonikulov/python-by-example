# Challenge 065

import turtle

# Draw the number 1.
turtle.left(90)
turtle.forward(150)
turtle.right(90)

# Move the turtle forward.
turtle.penup()
turtle.forward(50)
turtle.pendown()

# Draw the number 2.
turtle.forward(100)
turtle.right(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(100)

# Move the turtle forward.
turtle.penup()
turtle.forward(50)
turtle.pendown()

# Draw the number 3.
turtle.forward(100)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.backward(75)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(100)

turtle.hideturtle()
turtle.exitonclick()