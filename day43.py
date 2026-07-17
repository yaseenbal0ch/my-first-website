print("===== RANDOM PASSWORD =====")

import random

letters = "abcdefghijklmnopqrstuvwxyz"

password = ""

for i in range(8):
    password += random.choice(letters)

    print("Password:", password)