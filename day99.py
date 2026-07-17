print("===== STUDENT MANAGEMENT SYSTEM =====")

students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student Name: ")
        age = input("Student Age: ")
        city = input("Student City: ")

        students[name] = {
            "Age": age,
            "City": city
        }

        print("Student Added Successfully!")

    elif choice == "2":
        if students:
            print("\nStudent List:")
            for name, info in students.items():
                print(f"{name} -> Age: {info['Age']}, City: {info['City']}")
        else:
            print("No students found.")

    elif choice == "3":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice!")