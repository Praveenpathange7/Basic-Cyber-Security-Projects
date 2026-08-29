# Encrpt and Decrypt the text using Caser Cipher

def change(option,message,shift):
    result = ""
    for char in message:
        if char.isalpha():
            position = ord(char) - ord('A')

            if option == 1:
                new_position = (position + shift) % 26
            elif option == 2:
                new_position = (position - shift) % 26
            else:
                return "Invalid option"

            new_char = chr(new_position + ord('A'))
            result += new_char

        else:
            result += char

    return result

message = input("Enter the message:").upper()
shift = int(input("Enter shift value:"))
print('1.Encrypt\n2.Decrypt')
option = int(input("Enter the option:"))
changed = change(option,message,shift)

if option == 1:
    print("Encrypted message :",changed)
elif option == 2:
    print("Decrypted message :",changed)
else:
    print('Enter the valid option')
