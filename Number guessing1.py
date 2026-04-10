#using some hints
import random

secret_number = random.randint(1, 100)

print("Welcome to Advanced Number Guessing Game!")
print("Guess a number between 1 and 100")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("🎉 Correct! You guessed the number.")
        print("Total attempts:", attempts)
        break
    else:
        print("Wrong guess!")

        # Hint 1: Square
        print("Hint: Square of the number is", secret_number ** 2)

        # Hint 2: Cube
        print("Hint: Cube of the number is", secret_number ** 3)

        # Hint 3: Even/Odd
        if secret_number % 2 == 0:
            print("Hint: It is an EVEN number")
        else:
            print("Hint: It is an ODD number")

        # Hint 4: Greater or smaller
        if guess < secret_number:
            print("Try a bigger number ⬆️")
        else:
            print("Try a smaller number ⬇️")

        print("-" * 30)
