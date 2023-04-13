# Challenge 101

data_set = {'John':{'N':3056, 'S':8463, 'E':8441, 'W':2694},
            'Tom':{'N':4832, 'S':6786, 'E':4737, 'W':3612},
            'Anne':{'N':5239, 'S':4802, 'E':5820, 'W':1859},
            'Fiona':{'N':3904, 'S':3645, 'E':8821, 'W':2451}
            }

name = input("Enter a name: ")
region = input("Enter a region: ")
print(data_set[name][region])

value = int(input("Enter a new value: "))
data_set[name][region] = value
print(f"{name}: {data_set[name]}")