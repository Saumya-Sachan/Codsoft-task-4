import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_choice(choice):
    """Display the choice in the form of hands."""
    if choice == '1':
        return """You chose:
    Rock:
                ____
              .'    `.
             /  _  _  \\
            |   o  o   |
            |    __    |
             \  `--'  /
              `------'
        """
    elif choice == "2":
        return """You chose:
    Paper:
                ____
              .'    `.
             /  _  _  \\
            |   o  o   |
            |   \__/   |
             \        /
              `------'
        """
    elif choice == '3':
        return """You chose:
    Scissors:
                ____
              .'     `.
             /  _  _   \\
            |   o  o    |
            |    __     |
             \  /  \   /
              `------'
        """
    else:
        return ""

def main():
    """Main function to run the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("""Instructions: 
          Choose:
          1 for rock
          2 for paper
          3 for scissors""")

    while True:
        user_choice = input("Enter your choice (1,2,3): ")

        # Handle invalid input
        if user_choice not in ['1','2','3']:
            print("Invalid choice! Please choose 1,2 or 3.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Display choices
        print(display_choice(user_choice))
        print(display_choice(computer_choice))

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Score tracking
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")

        if play_again == 'no':
            break

    print("Thank you for playing! Goodbye!")

if __name__ == "__main__":
    main()