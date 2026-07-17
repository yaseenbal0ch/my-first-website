print("===== APPEND FILE =====")

file = open("data.txt", "a")

file.write("\nI live in Dera Ghazi Khan.")
file.write("\nI want to become a Software Engineer.")

file.close()

print("New Data Added Successfully!")