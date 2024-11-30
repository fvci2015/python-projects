import random
low_value=1
high_value=100
MaxAttempts=10
random_number=random.randint(low_value,high_value)

def get_guess():
    while True:
        try:
            guess=int(input(f"Guess the number between {low_value} and {high_value}"))
            if low_value<=guess<=high_value:
                return guess
            else:
                print("Error, pls print a number within specified range")
        except ValueError:
            print("Invalid input. pls enter a valid input")


def check_guess(guess,random_number):
    if guess==random_number:
        return "correct"
    elif guess<random_number:
        return "Too low"
    else:
        return "Too high"

    
def PlayTheGame():
    attempts=0
    won=False
    while attempts<MaxAttempts:
        attempts+=1
        guess=get_guess()
        result=check_guess(guess,random_number)

        if result=="correct":
            print("Congrats, You have won the game")
            won=True
            break
        else:
            print(result,"Try again")
    if won==False:
        print("You've lost, You've run out of attempts")

if __name__=="__main__":
    print("-----------------")
    print("Welcome to the number guessing game")
    PlayTheGame()
