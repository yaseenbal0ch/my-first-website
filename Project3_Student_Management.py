students = {}

while True:
    print("\n==============================")
    print(" STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student already exists!")
        else:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            city = input("Enter City: ")

            students[roll] = {
                "Name": name,
                "Age": age,
                "City": city
            }

            print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\n----- Student List -----")
            for roll, info in students.items():
                print(f"Roll No : {roll}")
                print(f"Name    : {info['Name']}")
                print(f"Age     : {info['Age']}")
                print(f"City    : {info['City']}")
                print("------------------------")

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")

        if roll in students:
            info = students[roll]
            print("\nStudent Found")
            print(f"Name : {info['Name']}")
            print(f"Age  : {info['Age']}")
            print(f"City : {info['City']}")
        else:
            print("Student not found!")

    elif choice == "4":
        roll = input("Enter Roll Number to Update: ")

        if roll in students:
            name = input("Enter New Name: ")
            age = input("Enter New Age: ")
            city = input("Enter New City: ")

            students[roll]["Name"] = name
            students[roll]["Age"] = age
            students[roll]["City"] = city

            print("Student updated successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        roll = input("Enter Roll Number to Delete: ")

        if roll in students:
            del students[roll]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "6":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
