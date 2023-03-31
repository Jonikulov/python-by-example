# Challenge 011

larger = int(input("Enter a number over 100: "))
smaller = int(input("Enter a number under 10: "))

if larger > 100 and smaller < 10:
    result = larger // smaller
    print(f"{smaller} goes into the {larger} {result} times.")
else:
    print("Invalid input. Please try again.")