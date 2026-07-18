print("=== Simple Calculator ===")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    result = num1 + num2
    print("Addition =", result)

elif choice == "2":
    result = num1 - num2
    print("Subtraction =", result)

elif choice == "3":
    result = num1 * num2
    print("Multiplication =", result)

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("Division =", result)
    else:
        print("Error: Cannot divide by zero!")

else:
    print("Invalid choice! Please select 1, 2, 3, or 4.")
