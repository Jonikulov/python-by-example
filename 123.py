# Challenge 123

import csv

def choose_menu():
    option = input("1) Add to file\n" \
                "2) View all records\n" \
                "3) Delete a record\n" \
                "4) Quit program\n" \
                "Enter the number of your selection: "
                )
    return int(option)

def add_to_file():
    with open("Salaries.csv", 'a') as file:
        name = input("Name: ")
        salary = input("Salary: ")
        file.write(f'{name},{salary}\n')

def view_all_records():
    reader = csv.reader(open("Salaries.csv"))
    for row in reader:
        print(" | ".join(row))

def delete_record():
    names_list = list(csv.reader(open("Salaries.csv")))
    # Find the record to delete.
    name = input("Enter a name to delete record: ")
    is_available = False
    for idx, row in enumerate(names_list):
        if name.lower() == row[0].lower():
            is_available = True
            break
    # Check if record in the file.
    if not is_available:
        print("This name is not available.")
    else:
        # Delete the selection and write remaining records.
        del names_list[idx]
        with open("Salaries.csv", 'w') as file:
            for row in names_list:
                file.write(",".join(row) + '\n')

option = choose_menu()
while option != 4:
    if option == 1:
        add_to_file()
    elif option == 2:
        view_all_records()
    elif option == 3:
        delete_record()
    else:
        print("Invalid option.")
    print()
    option = choose_menu()