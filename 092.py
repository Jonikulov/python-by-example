# Challenge 092

from array import *
import random

u_nums = array('i', [])
for i in range(1, 4):
    num = int(input(f"Enter {i}-number: "))
    u_nums.append(num)

r_nums = array('i', [])
for _ in range(5):
    num = random.randint(-32_768, 32_767)
    u_nums.append(num)

u_nums.extend(r_nums)
for i in sorted(u_nums):
    print(i)