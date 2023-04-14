# Challenge 115

import csv

reader = csv.reader(open("Books.csv"))
header = next(reader)

print(" | ".join(header))
for i, row in enumerate(reader):
    print(f"{i+1}.", " | ".join(row))