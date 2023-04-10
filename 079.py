# Challenge 079

nums = []
for _ in range(3):
    num = int(input("Enter a number: "))
    nums.append(num)
answer = input("Do you want the last number saved? (y/n) ")
if answer == 'n':
    del nums[-1]
print(nums)