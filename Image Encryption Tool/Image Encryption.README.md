# Image Encryption Tool

### SkillCraft Technology Internship — Task 02

A simple Python-based **Image Encryption and Decryption Tool** that uses pixel manipulation to transform an image.
Each RGB value of every pixel is modified using a user-provided encryption key.

> **Note:** This project is intended for educational purposes to demonstrate basic image processing, pixel manipulation, 
and reversible encryption concepts. It is not intended for secure real-world data protection.

---

## Features

- 🔐 Encrypt images using RGB pixel manipulation
- 🔓 Decrypt images using the same encryption key
- 📂 Accept image file paths from the user
- 🔑 Use a user-defined encryption key
- 🎨 Convert images to RGB format for consistent pixel processing
- 💾 Save encrypted and decrypted images as PNG files
- 🖼️ Display the processed image
- ⚠️ Basic error handling for invalid image paths and keys

---

## Technologies Used

- **Python 3**
- **Pillow (PIL)**

---

## How It Works

An RGB image consists of pixels represented by three values:

```text
(R, G, B)

Each value normally ranges from 0 to 255.

Encryption

The encryption key is added to each RGB component:

R = (R + key) % 256
G = (G + key) % 256
B = (B + key) % 256

For example, with a key of 50:

Original Pixel:
(9, 14, 10)

Encrypted Pixel:
(59, 64, 60)

This operation is performed on every pixel in the image.

Decryption

Decryption reverses the encryption operation:

R = (R - key) % 256
G = (G - key) % 256
B = (B - key) % 256

Example:

Encrypted Pixel:
(59, 64, 60)

Decrypted Pixel:
(9, 14, 10)

Why % 256?

RGB values must remain between 0 and 255.

## Why `% 256`?

The modulo operation ensures that the calculated value stays within the valid RGB range of 0 to 255.

For example:

230 + 50 = 280
280 % 256 = 24

So, the resulting RGB value remains valid.

---

## Installation

Make sure Python is installed on your system.

Install the required Pillow library:

```bash
pip install Pillow

Or install all dependencies using:

pip install -r requirements.txt
Usage

Run the program:

python Image_Encryption.py

The program asks for the image path:

Enter the image file path:

Example:

C:\Users\Username\Pictures\image.jpg

Enter the encryption key:

Enter the encryption key: 50

Choose an operation:

1. Encrypt_Image
2. Decrypt_Image
Enter the option: 1
Encrypt an Image

Select option 1.

The program modifies the RGB values of every pixel and creates:

encrypted_image.png
Decrypt an Image

Run the program again and provide the path of the encrypted image.

Select option 2 and enter the same key that was used for encryption.

The program creates:
      decrypted_image.png

Example : 
Encryption
Enter the image file path: C:\Pictures\image.jpg
Enter the encryption key: 50

1. Encrypt_Image
2. Decrypt_Image
Enter the option: 1

Encryption completed

Output:

encrypted_image.png
Decryption
Enter the image file path: C:\Pictures\encrypted_image.png
Enter the encryption key: 50

1. Encrypt_Image
2. Decrypt_Image
Enter the option: 2

Decryption completed

Output:
    decrypted_image.png

Error Handling:

  The program provides basic handling for:
      Image files that cannot be found
      Invalid encryption keys
      Negative encryption keys
      Invalid operation choices
      Concepts Learned

Through this project, I learned:

      Image processing using Python
      RGB color representation
      Pixel-level image manipulation
      Python functions
      for loops
      Conditional statements
      Modular arithmetic
      File handling
      Basic encryption and decryption concepts
      Exception handling using try and except
      Limitations

This project uses a simple mathematical transformation of pixel values.

It demonstrates the concept of reversible encryption, but it is not cryptographically secure and 
should not be used to protect sensitive or confidential images.
