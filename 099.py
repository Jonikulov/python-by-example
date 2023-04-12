# Challenge 099

list2d = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list2d)

row = int(input("Enter a row number to display: "))
print(list2d[row])

column = int(input("Enter a column number in the row to display: "))
print(list2d[row][column])

change = input("Do you want to change the value? (y/n): ")
if change == 'y':
    num = int(input("Enter a new value: "))
    list2d[row][column] = num
    print(list2d[row])