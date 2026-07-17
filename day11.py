print("===== Nested IF =====")

age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no): ")

if age >= 18:
    if has_id == "yes":
        print("You can vote.")
    else:
                print("You need an ID card.")
else:
    print("You are under 18. You cannot vote.")
