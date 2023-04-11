# Challenge 090

from array import *

nums = array('i', [])
while len(nums) < 5:
    num = int(input("Enter an integer [10-20]: "))
    if 10 <= num <= 20:
        nums.append(num)
    else:
        print("Outside the range.")

print("Thank you.")
for n in nums: print(n)