# Challenge 088

from array import *

nums_array = array('i', [])
for i in range(1, 6):
    num = int(input(f"Enter {i}-number: "))
    nums_array.append(num)
nums_array = sorted(nums_array)
nums_array.reverse()
print(nums_array)