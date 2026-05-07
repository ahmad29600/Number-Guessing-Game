# Number Guessing Game

import random
random_number = random.randint(1, 100)

guess = 0

while guess != random_number:
    guess = int(input("Guess the number: "))
    if guess < random_number:
        print("Too Low! Guess Again...")
    elif guess > random_number:
        print("Too High! Guess Again...")
    else:
        print("Congratulations! You have guessed correct number.")

# Program will updated by time 