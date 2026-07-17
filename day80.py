print("===== USER INPUT DICTIONARY =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

student = {
    "name": name,
        "age": age,
            "city": city
            }

print("\n===== STUDENT DATA =====")
print("Name:", student["name"])
print("Age:", student["age"])
print("City:", student["city"])