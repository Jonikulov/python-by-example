# Challenge 073

foods_dict = {}
for i in range(1, 4):
    food = input(f"Enter {i}-food: ")
    foods_dict[i] = food
print(foods_dict)
idx = int(input("Enter an index of the food to be removed: "))
del foods_dict[idx]
print(sorted(foods_dict.values()))