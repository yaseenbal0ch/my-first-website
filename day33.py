print("===== NESTED IF =====")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an Adult.")

if age >= 60:
    print("You are a Senior Citizen.")
else:
    print("You are not a Senior Citizen.")

if age >= 18:
    if age < 60:
        print("You are a Young Adult.")
    else:
        print("You are a Senior Citizen.")
else:
    print("You are a Minor.")