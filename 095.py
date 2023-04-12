# Challenge 095

from array import *

nums = array('f', [13.98, 43.77, 90.02, 28.56, 15.88])
print([round(n, 2) for n in nums])

num = int(input("Enter an integer [2-5]: "))
while num < 2 or num > 5:
    num = int(input("Outside range. Try again: "))

result_arr = [round(n / num, 2) for n in nums]
print(result_arr)