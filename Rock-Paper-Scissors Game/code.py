import random


user_score = 0
computer_score = 0

while True:
    
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    print(result)
    print(f"User Score: {user_score}, Computer Score: {computer_score}")

    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")
