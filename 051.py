# Challenge 051

num = 10
while num > 0:
    print(f"There are {num} green bottles hanging on the wall,")
    print(f"{num} green bottles hanging on the wall,")
    print("And if 1 green bottle should accidentally fall,")
    answer = int(input("How many green bottles will be hanging on the wall? "))
    num -= 1
    if answer == num:
        print(f"There will be {num} green bottles hanging on the wall.")
    else:
        while answer != num:
            answer = int(input("No, try again: "))
print("There are no more green bottles hanging on the wall.")