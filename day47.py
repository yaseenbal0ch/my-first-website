print("===== READ LINE BY LINE =====")

file = open("data.txt", "r")

for line in file:
    print(line, end="")

file.close()