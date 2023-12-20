import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def print_choices(user_choice, computer_choice):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

def print_score(user_score, computer_score):
    print(f"\nScore - You: {user_score} | Computer: {computer_score}")

def main():
    print("Welcome to Rock-Paper-Scissors Game!")

    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = input("Enter the number of your choice (1-4): ")

        if user_choice == "4":
            print("\nThanks for playing! Final Score:")
            print_score(user_score, computer_score)
            break

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice in ["1", "2", "3"]:
            user_choice = choices[int(user_choice) - 1]
            result = determine_winner(user_choice, computer_choice)
            print_choices(user_choice, computer_choice)
            print(result)

            if result == "You win!":
                user_score += 1
            elif result == "Computer wins!":
                computer_score += 1

            print_score(user_score, computer_score)

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
