import random
emojis = { 'r': '🪨', 'p': '📝', 's': '✂️'}
choices = ['r', 'p', 's']
while True:
    choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if choice not in choices:
        print("Invalid choice!")
        continue

    computer_choice = random.choice(choices)
    print(f'You chose {emojis[choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if choice == computer_choice:
        print("It's a tie!")
    elif (
        (choice == 'r' and computer_choice == 's') or 
        (choice == 'p' and computer_choice == 'r') or
        (choice == 's' and computer_choice == 'p')):
        print("You win!")
    else:
        print("You lose!")

    shut_down = input("Do you want to play again? (y/n): ").lower()

    if shut_down == 'n':
        print("Thanks for playing!!")
        break
    elif shut_down == 'y':
        continue
    else:
        print("Invalid choice!")
        break
