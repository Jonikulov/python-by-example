# Challenge 034

selection = int(input("1) Square\n" \
              "2) Triangle\n\n" \
              "Enter a number: "
              ))
if selection == 1:
    side = float(input("Enter the side length of the square: "))
    print("Area:", side**2)
elif selection == 2:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print("Area:", base * height * 1/2)
else:
    print("Error input.")