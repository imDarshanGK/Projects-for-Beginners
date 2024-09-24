import random

guess = random.randint(1,100)
while True:
    try:
        choice = int(input("Guess the number between 1 and 100 : "))
        if choice< guess:
            print("Too low!.")
        elif choice> guess:
            print("Too high!.")
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print("Please enter a valid number")
