print("===== READLINE & READLINES =====")

file = open("data.txt", "r")

print("First Line:")
print(file.readline())

print("Second Line:")
print(file.readline())

file.close()

print("\n===== READLINES =====")

file = open("data.txt", "r")

lines = file.readlines()

print(lines)

file.close()