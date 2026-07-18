print("===== DAY 100 =====")

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

student1 = Student("Muhammad Yaseen", 20)

student1.show()
