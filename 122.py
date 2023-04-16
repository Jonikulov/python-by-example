# Challenge 122

def choose_menu():
    option = input("1) Add to file\n" \
                "2) View all records\n" \
                "3) Quit program\n" \
                "Enter the number of your selection: "
                )
    return int(option)

def add_to_file():
    with open("Salaries.csv", 'a') as file:
        name = input("Name: ")
        salary = input("Salary: ")
        file.write(f'{name},{salary}\n')

def view_all_records():
    import csv
    reader = csv.reader(open("Salaries.csv"))
    for row in reader:
        print(" | ".join(row))

option = choose_menu()
while option != 3:
    if option == 1:
        add_to_file()
    elif option == 2:
        view_all_records()
    else:
        print("Invalid option.")
    print()
    option = choose_menu()