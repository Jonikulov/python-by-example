# Challenge 093

from array import *

nums = array('i', [])
for i in range(1, 6):
    num = int(input(f"Enter {i}-number: "))
    nums.append(num)

print(sorted(nums))
num = int(input("Choose a number to remove: "))
if num in nums:
    nums.remove(num)
    nums1 = array('i', [num])
    print(nums)
    print(nums1)
else:
    print("This value is not in the array.")