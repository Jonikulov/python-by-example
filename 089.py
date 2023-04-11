# Challenge 089

from array import *
import random

nums = array('i', [])
for _ in range(5):
    num = random.randint(-32_768, 32_767)
    nums.append(num)

for i in nums:
    print(i)