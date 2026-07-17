print("===== SET METHODS =====")

numbers = {10, 20, 30, 40}

print(numbers)

numbers.add(50)
print("After Add:", numbers)

numbers.discard(20)
print("After Discard:", numbers)

print("Is 30 in Set?", 30 in numbers)

print("Length:", len(numbers))