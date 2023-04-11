# Challenge 086

password = input("Enter a password: ")
password_ = input("Enter it again: ")
if password == password_:
    print("Thank you.")
elif password.lower() == password_.lower():
    print("They must be in the same case.")
else:
    print("Incorrect.")