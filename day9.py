print("===== Logical Operators =====")

age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no): ")

print("\n----- Results -----")

print("Can Vote (age >=18 and ID):", age >= 18 and has_id == "yes")
print("Can Enter (age >=18 or ID):", age >= 18 or has_id == "yes")
print("No ID:", not (has_id == "yes"))
