1import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Number Guessing Game")
print("I'm thinking of a number from 1 to 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You got it in {attempts} attempts.")
        break