print("===== WHILE LOOP WITH USER INPUT =====")

number = int(input("Enter a number: "))

count = 1

while count <= 10:
    print(f"{number} x {count} = {number * count}")
    count += 1