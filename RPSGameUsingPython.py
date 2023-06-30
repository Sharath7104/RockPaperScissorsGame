import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def print_score(user_wins, computer_wins, draws):
    print("Score:")
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Draws: {draws}")
    print()

choices = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0
draws = 0

print("Rock, Paper, Scissors Game!")
print("Enter 'quit' to exit the game.")

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice == "quit":
        break

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "user":
        print("You win!")
        user_wins += 1
    elif winner == "computer":
        print("Computer wins!")
        computer_wins += 1
    else:
        print("It's a draw!")
        draws += 1

    print_score(user_wins, computer_wins, draws)

print("Thank you for playing!")
