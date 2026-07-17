print("===== SIMPLE CALCULATOR =====")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter (+, -, *, /): ")

if choice == "+":
    print("Answer:", num1 + num2)
elif choice == "-":
        print("Answer:", num1 - num2)
elif choice == "*":
            print("Answer:", num1 * num2)
elif choice == "/":
                print("Answer:", num1 / num2)
else:
                    print("Invalid Operator!")