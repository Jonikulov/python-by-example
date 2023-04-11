# Challenge 094

from array import *

nums = array('i', [10, 11, 13, 14, 17, 19])
print(nums)
num = int(input("Select a number: "))

while True:
    if num in nums:
        print(f"Position of {num} in the array: {nums.index(num)}")
        break
    else:
        num = int(input("Not in the array. Try again: "))