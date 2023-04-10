# Challenge 075

numbers = [123, 456, 789]
for i in numbers: print(i)
num = int(input("Enter a number from the list: "))
if num in numbers:
    print(numbers.index(num))
else:
    print("That is not in the list.")