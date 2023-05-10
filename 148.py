# Challenge 148: Passwords

import csv

menu = """
1) Create a new User ID
2) Change a password
3) Display all User IDs
4) Quit

Enter Selection: """

def enter_password():
    """Return strong password the user has entered."""

    while True:
        pwd = input("Enter a password: ")
        # Password Security Score
        pwd_score = 0
        # At least 8 characters
        if len(pwd) >= 8:
            pwd_score += 1
        # Includes uppercase letters
        if any(char.isupper() for char in pwd):
            pwd_score += 1
        # Includes lowercase letters
        if any(char.islower() for char in pwd):
            pwd_score += 1
        # Includes numbers
        if any(char.isdigit() for char in pwd):
            pwd_score += 1
        # Includes special characters
        spec_chars = "!@#$%^&*()_+=-;:'\"\\|?><`~"
        if any(char in spec_chars for char in pwd):
            pwd_score += 1

        if pwd_score <= 2:
            print("This password is weak.")
            continue
        elif pwd_score <= 4:
            change = input("This password could be improved.\n" \
                           "Do you want to try again? (y/n): ")
            if change == 'y':
                continue
            else:
                break
        if pwd_score == 5:
            print("This password is strong!")
            break

    return pwd


def create_user():
    """Create a new User ID and add it to csv file."""

    user_id_ist = [row[0] for row in csv.reader(open("users_passwords.csv"))]
    user_id = input("Enter a new User ID: ")
    while user_id in user_id_ist:
        user_id = input("This user ID already exists.\n" \
                        "Enter another User ID: ")

    pwd = enter_password()
    with open("users_passwords.csv", 'a') as file:
        file.write(f'{user_id},{pwd}\n')
        print("The new user has created.")


def change_pass():
    """Change the password and update the csv file."""

    data = list(csv.reader(open("users_passwords.csv")))
    user_id_ist = [row[0] for row in data]
    user_id = input("Enter the user ID to change a password: ")
    while user_id not in user_id_ist:
        user_id = input("This user ID does not exists. Try again: ")
    idx = user_id_ist.index(user_id)
    # update password
    data[idx][1] = enter_password()
    # update csv file
    with open("users_passwords.csv", 'w') as file:
        for row in data:
            file.write(",".join(row) + '\n')


def display_users():
    """Display all User IDs."""

    user_id_ist = [row[0] for row in csv.reader(open("users_passwords.csv"))]
    print("Here are all the User IDs:")
    for i in user_id_ist: print(i)    


def main():

    while True:
        selection = input(menu)

        try:
            sel = int(selection)
        except:
            print("Invalid input.")
            continue

        if sel == 1:
            create_user()
        elif sel == 2:
            change_pass()
        elif sel == 3:
            display_users()
        elif sel == 4:
            break
        else:
            print("Choose valid option.")


if __name__ == "__main__":
    main()