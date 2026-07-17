print("===== ERROR HANDLING =====")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Answer:", result)

except ZeroDivisionError:
                    print("Error: You cannot divide by zero!")

except ValueError:
                        print("Error: Please enter only numbers!")