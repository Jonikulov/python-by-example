# Challenge 042

total = 0
for i in range(1, 6):
    num = int(input(f"Enter {i}-number: "))
    including = input("Do you want this number included? (y/n) ")
    if including.lower() in ['y', 'yes']:
        total += num
print("\nTotal:", total)