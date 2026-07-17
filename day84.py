print("===== NESTED DICTIONARY =====")

students = {
    "student1": {
            "name": "Yaseen",
                    "age": 20
                        },
                            "student2": {
                                    "name": "Ali",
                                            "age": 22
                                                }
                                                }

print("Student 1 Name:", students["student1"]["name"])
print("Student 1 Age:", students["student1"]["age"])

print("Student 2 Name:", students["student2"]["name"])
print("Student 2 Age:", students["student2"]["age"])