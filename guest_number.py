import random

num = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I`m think of a number between 1 and 100")
difficult = input("Choouse a difficult . easy or hard ")

def game(difficult):
    attempts = 0
    if difficult=='hard':
        print(f"You have {attempts} attempts")
        attempts=5
    elif difficult=='easy':
        attempts=10
        print(f"You have {attempts} attempts")

    for i in range(attempts):
        guess = int(input("Enter your guess: "))

        if guess < num:
            print("Too low! Try again.")
        elif guess > num:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {num} correctly in {attempts - i} attempts.")
            break
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {num}.")

game(difficult)