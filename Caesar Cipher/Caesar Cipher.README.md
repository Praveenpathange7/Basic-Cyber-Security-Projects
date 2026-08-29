# 🔐 Caesar Cipher — Text Encryption & Decryption

A simple Python-based cryptography tool that encrypts and decrypts text using the Caesar Cipher algorithm. The program allows users to enter a message and a shift value, then performs encryption or decryption based on their choice.

This project was developed as part of my **Cybersecurity Internship at SkillCraft Technology**.

## 📌 Task Objective

Create a program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

## 🧠 What is Caesar Cipher?

The Caesar Cipher is a basic substitution cipher in which each letter of the plaintext is shifted by a fixed number of positions in the alphabet.

For example, with a shift of `3`:

```text
Plaintext:  HELLO
Ciphertext: KHOOR

The transformation is:

H → K
E → H
L → O
L → O
O → R

For decryption:

KHOOR → HELLO

⚠️ Note: Caesar Cipher is intended for educational purposes and should not be used to protect sensitive or confidential information.

✨ Features
🔒 Encrypt text using Caesar Cipher
🔓 Decrypt encrypted text
🔢 Supports user-defined shift values
🔤 Supports uppercase and lowercase letters
📝 Preserves spaces and special characters
🔄 Handles shift values greater than 26
🖥️ Simple user-driven interface
❌ Includes input validation

🛠️ Technologies Used
Python 
Python Standard Library

No external packages are required.

📂 Project Structure
SCT_CS_1/
│
├── caesar_cipher.py
└── README.md

💻 How to Use

Run the program and select an operation:

===== Caesar Cipher =====

1. Encrypt
2. Decrypt
3. Exit

Enter your choice:
🔒 Encryption Example
Enter your choice: 1
Enter message: Hello World
Enter shift value: 3

Encrypted message: Khoor Zruog
🔓 Decryption Example
Enter your choice: 2
Enter message: Khoor Zruog
Enter shift value: 3

Decrypted message: Hello World
🔍 How the Algorithm Works

The Caesar Cipher uses modular arithmetic to shift characters within the alphabet.

Encryption
C = (P + K) mod 26
Decryption
P = (C - K) mod 26

Where:

P = Position of the original character
C = Position of the encrypted character
K = Shift value
26 = Number of letters in the English alphabet

The modulo operation allows the alphabet to wrap around.

For example, with a shift of 3:

X → A
Y → B
Z → C

🎯 Learning Outcomes

Through this project, I gained practical knowledge of:

🔐 Basic cryptography concepts
🔄 Encryption and decryption
🔢 Modular arithmetic
🐍 Python programming
🔤 String manipulation
🧑‍💻 User input and validation
🛡️ Fundamental cybersecurity concepts

⚠️ Disclaimer

This project was created for educational purposes as part of my Cybersecurity Internship at SkillCraft Technology.

The Caesar Cipher is not secure for modern cybersecurity applications because it has a very small key space and can be easily broken using brute-force or frequency-analysis techniques.
