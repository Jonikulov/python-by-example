# Challenge 098

list2d = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list2d)

row = int(input("Enter a row number to display: "))
print(list2d[row])

num = int(input("Enter a new value to the row: "))
list2d[row].append(num)
print(list2d[row])