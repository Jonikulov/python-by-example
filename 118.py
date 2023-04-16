# Challenge 118

def get_num():
    return int(input("Enter a number: "))

def count(num):
    for i in range(1, num+1):
        print(i)

num = get_num()
count(num)