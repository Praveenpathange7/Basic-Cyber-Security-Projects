from PIL import Image

def encrypt_Image(input_image,output_image,key):
    try:
        image = Image.open(input_image).convert('RGB')
    except FileNotFoundError:
        print("Error: Image file not found.")
        return False
    pixel = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r,g,b = pixel[x,y]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixel[x,y] = r,g,b
    image.save(output_image)
    image.show()

def decrypt_Image(input_image, output_image, key):
    try:
        image = Image.open(input_image).convert('RGB')
    except FileNotFoundError:
        print("Error: Image file not found.")
        return False
    pixel = image.load()

    for y in range(image.height):
        for x in range(image.width):

            r, g, b = pixel[x, y]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixel[x, y] = r, g, b

    image.save(output_image)
    image.show()

image_path = input("Enter the image file path: ").strip('"')
try:
    key = int(input("Enter the encryption key: "))

    if key < 0:
        print("Error: Key cannot be negative.")
        exit()

except ValueError:
    print("Error: Please enter a valid integer key.")
    exit()

print("1.Encrypt_Image\n2.Decrypt_Image")
option = input("Enter the option : ")

if option == '1':
    encrypt_Image(image_path, "encrypted_image.png", key)
    print("Encryption completed")
elif option == '2':
    decrypt_Image(image_path,"decrypted_image.png",key)
    print("Decryption completed")
else:
    print("Not a valid option")
