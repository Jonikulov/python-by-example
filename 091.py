# Challenge 091

from array import *

nums = array('i', [10, 15, 12, 15, 19])
print(nums)
num = int(input("Enter a number from the list: "))
print(f"{num} repeats {nums.count(num)} times in the array.")