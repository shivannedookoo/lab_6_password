# Author: Shivanne Dookoo

def encode(password):  # shifts an 8 digit password by 3 numbers
    encoded_password = ""
    for digit in password:
        encoded = str((int(digit) + 3) % 10)  # shifts each digit up by 3 and keeps remainder for numbers more than 10
        encoded_password += encoded
    return encoded_password

def decode(encode):
    Ddata = ''
    num = 0 #initializes value for num to be used 
    for i in encode:
        if i.isdigit():
            num = int(i) - 3 
            if num < 0: # ensures values that become negative are always positive 
                num +=10
            Ddata += str(num)
    return Ddata



if __name__ == "__main__":
    while True:
        print("Menu")  # prints menu
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option = int(input("Please enter an option: "))  # prompts user to choose a menu option

        if option == 3:  # quits
            break
        if option == 1:  # encodes password
            password = str(input("Please enter your password to encode: "))
            encode = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:  # decodes password
            print(f"The encoded password is {encode}, and the original password is {decode(encode)}.\n")

