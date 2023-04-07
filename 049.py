# Challenge 049

compnum = 50
attempt = 0
while True:
    guess = int(input("Guess the number: "))
    attempt += 1
    if guess > compnum:
        print("Too high.")
    elif guess < compnum:
        print("Too low.")
    else:
        print(f"Well done, you took {attempt} attempts.")
        break