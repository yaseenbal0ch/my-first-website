print("===== WITH OPEN =====")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

    print("File closed automatically.")