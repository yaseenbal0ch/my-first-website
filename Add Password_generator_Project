import random
import string

print("=================================")
print("     PASSWORD GENERATOR")
print("=================================")

length = int(input("Enter password length: "))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\n=================================")
print("Your Generated Password is:")
print(password)
print("=================================")

again = input("\nDo you want another password? (yes/no): ")

if again.lower() == "yes":
    length = int(input("Enter password length: "))

    password = ""

    for i in range(length):
        password += random.choice(all_characters)

    print("\nYour New Password is:")
    print(password)

else:
    print("\nThank you for using Password Generator!")
