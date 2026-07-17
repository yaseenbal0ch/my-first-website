print("===== GUESS NUMBER =====")

secret = 7

guess = int(input("Guess a number: "))

if guess == secret:
    print("Correct!")
else:
        print("Wrong!")