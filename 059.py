# Challenge 059

import random

colors = {"red":"You're seeing RED right now!",
          "yellow":"You're YELLOW-bellied!",
          "green":"I bet you are GREEN with envy!",
          "blue":"You are probably feeling BLUE right now!",
          "white":"Are you WHITE as a sheet, as you didn't guess correctly?"
          }
color = random.choice(list(colors))
while True:
    guess = input(f"Guess the color: {', '.join(colors)}\n>>> ")
    if guess.lower() == color:
        print("Well done.")
        break
    else:
        print(colors[color])