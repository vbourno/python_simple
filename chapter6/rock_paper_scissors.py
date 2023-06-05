import random

options = ["rock", "paper", "scissors"]
game_num = 0
player_wins = 0
computer_wins = 0
draws = 0

while game_num in range(0, 10):
    # Get input and normalize in order to compare.
    player_input = input("Enter your choice (rock/paper/scissors): ").lower()

    if (player_input != "rock") & (player_input != "paper") & (player_input != "scissors"):
        print("Invalid choice, please try again.")
        player_input = input("Enter your choice (rock/paper/scissors): ").lower()

    print("You chose:", player_input)
        
    computer_str = random.choice(options)
    print("Computer chose:", computer_str)

    # Comparison - result
    while player_input != computer_str:
        if (player_input == "rock") & (computer_str == "paper"):
            print("Computer wins!")
            print()
            computer_wins += 1
            break
        elif (player_input == "rock") & (computer_str == "scissors"):
            print("You win!")
            print()
            player_wins += 1
            break
        elif (player_input == "paper") & (computer_str == "rock"):
            print("You win!")
            print()
            player_wins += 1
            break
        elif (player_input == "paper") & (computer_str == "scissors"):
            print("Computer wins!")
            print()
            computer_wins += 1
            break
        elif (player_input == "scissors") & (computer_str == "rock"):
            print("Computer wins!")
            print()
            computer_wins += 1
            break
        elif (player_input == "scissors") & (computer_str == "paper"):
            print("You win!")
            print()
            player_wins += 1
    else:
        print("It 's a draw.")
        print()
        draws += 1
    game_num += 1

print(f"Games played: {game_num}")
print(f"You won: {player_wins} games!")
print(f"Computer won: {computer_wins} games!")
print(f"Draw games: {draws}")
if (player_wins > computer_wins):
    print("You won!")
elif(player_wins == computer_wins):
    print("It 's a draw.")
elif(player_wins < computer_wins):
    print("Computer won!")