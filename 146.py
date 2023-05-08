# Challenge 146: Shift Code

menu = """
1) Make a code
2) Decode a message
3) Quit

Enter your selection: """

def encode(msg, key):
    enc_msg = ""
    for char in msg:
        if char.isalpha():
            if char.isupper():
                enc_msg += chr( (ord(char) + key - 65) % 26 + 65 )
            else:
                enc_msg += chr( (ord(char) + key - 97) % 26 + 97 )
        else:
            enc_msg += char

    return enc_msg

def decode(msg, key):
    dec_msg = ""
    for char in msg:
        if char.isalpha():
            if char.isupper():
                dec_msg += chr( (ord(char) - key - 65) % 26 + 65 )
            else:
                dec_msg += chr( (ord(char) - key - 97) % 26 + 97 )
        else:
            dec_msg += char

    return dec_msg

while True:
    selection = input(menu)

    try:
        menu_opt = int(selection)
    except:
        print("Invalid input.")
        continue

    if menu_opt == 1:
        message = input("Message to encode: ")
        code = int(input("Shift code: "))
        print(encode(message, code))
        continue
    elif menu_opt == 2:
        message = input("Message to decode: ")
        code = int(input("Shift code: "))
        print(decode(message, code))
        continue
    elif menu_opt == 3:
        break
    else:
        print("Choose valid option.")
        continue