# Challenge 088

from array import *

nums = array('i', [])
for i in range(1, 6):
    num = int(input(f"Enter {i}-number: "))
    nums.append(num)

nums = sorted(nums)
nums.reverse()
print(nums)