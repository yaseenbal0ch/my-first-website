print("===== DICTIONARY UPDATE & DELETE =====")

student = {
    "name": "Yaseen",
        "age": 20,
            "city": "DG Khan"
            }

print("Before:")
print(student)

            # Update age
student["age"] = 21

            # Add new key
student["country"] = "Pakistan"

            # Delete city
student.pop("city")

print("\nAfter:")
print(student)