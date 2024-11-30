import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2, dice1 + dice2

def play_7_up_7_down():
    print("Welcome to 7 Up 7 Down!")
    print("Rules:")
    print("1. Guess whether the sum of two dice will be:\n   - 'up' (greater than 7)\n   - 'down' (less than 7)\n   - 'exact' (exactly 7).")
    print("2. Type your guess and see if you're correct!\n")
    
    
    guess = input("Enter your guess (up, down, exact): ").strip().lower()
    if guess not in {"up", "down", "exact"}:
        print("Invalid input! Please choose from 'up', 'down', or 'exact'.")
        return
    
    dice1, dice2, total = roll_dice()
    print(f"\nThe dice rolls are: {dice1} and {dice2}. Total = {total}.")
    
  
    if total > 7 and guess == "up":
        print("You guessed right! It's 7 Up!")
    elif total < 7 and guess == "down":
        print("You guessed right! It's 7 Down!")
    elif total == 7 and guess == "exact":
        print("You guessed right! It's exactly 7!")
    else:
        print("Oops! Better luck next time!")
    
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_7_up_7_down()
    else:
        print("Thanks for playing! Goodbye!")

play_7_up_7_down()
