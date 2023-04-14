# Challenge 114

import csv

start = int(input("Starting year: "))
end = int(input("Ending year: "))

reader = csv.reader(open("Books.csv"))
for row in reader:
    try:
        year = int(row[2])
        if year in range(start, end+1):
            print(" | ".join(row))
    except:
        pass