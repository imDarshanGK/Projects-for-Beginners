import random
emojis = { 'r': '🪨', 'p': '📝', 's': '✂️'}
choices = ['r', 'p', 's']

def get_choice():
    while True:
        user_choice = input("Rock, paper, or scissor? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice! Please try again.")
def display_choices(choice, computer_choice):
     print(f'You chose {emojis[choice]}')
     print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(choice, computer_choice):
    if choice == computer_choice:
        print("It's a tie!")
    elif (
        (choice == 'r' and computer_choice == 's') or 
        (choice == 'p' and computer_choice == 'r') or
        (choice == 's' and computer_choice == 'p')):
        print("You win!")
    else:
        print("You lose!")

def play_again():
    while True:
        user_choice = get_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        shut_down = input("Do you want to play again? (y/n): ").lower()

        if shut_down == 'n':
            print("Thanks for playing!!")
            break
        elif shut_down == 'y':
            continue
        else:
            print("Invalid choice!")
            break
play_again()