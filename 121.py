# Challenge 121

def add_name():
    name = input("Enter a name: ")
    names_list.append(name)
    
    return names_list

def change_name():
    name = input("Enter a name you want to change in the list: ")
    if name in names_list:
        idx = names_list.index(name)
        name = input("Enter a new name: ")
        names_list[idx] = name
    else:
        print("This name is not available.")
    
    return names_list

def delete_name():
    name = input("Enter a name you want to delete from the list: ")
    if name in names_list:
        names_list.remove(name)
    else:
        print("This name is not available.")
    
    return names_list

def view_names():
    from pprint import pprint
    pprint(names_list)

def choose_menu():
    option = input("1) Add a name.\n" \
                "2) Change a name.\n" \
                "3) Delete a name.\n" \
                "4) View all names.\n" \
                "5) End the program.\n" \
                "Choose a menu number: "
            )
    return int(option)

def main():
    option = choose_menu()
    while option != 5:
        if option == 1:
            names_list = add_name()
        elif option == 2:
            names_list = change_name()
        elif option == 3:
            names_list = delete_name()
        elif option == 4:
            view_names()
        else:
            print("Invalid option.")
        print()
        option = choose_menu()

names_list = []
main()