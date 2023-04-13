# Challenge 109

menu = input("1) Create a new file\n" \
                "2) Display the file\n" \
                "3) Add a new item to the file\n" \
                "Make a selection 1, 2 or 3: "
            )
try:
    menu_num = int(menu)

    if menu_num == 1:
        with open("Subject.txt", 'w') as file:
            file.write(input("Enter a school subject: "))

    elif menu_num == 2:
        with open("Subject.txt", 'r') as file:
            print(file.read())

    elif menu_num == 3:
        with open("Subject.txt", 'a') as file:
            file.write('\n' + input("Enter a school subject: "))

        with open("Subject.txt", 'r') as file:
            print(file.read())

    else:
        print("Invalid option.")

except:
    print("Invalid input.")