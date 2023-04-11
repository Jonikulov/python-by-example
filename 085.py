# Challenge 085

VOWELS = {'a', 'e', 'i', 'o', 'u'}
name = input("Enter your name: ")
count = 0
for letter in name:
    if letter in VOWELS:
        count += 1
print(f"There {count} vowels in your name.")