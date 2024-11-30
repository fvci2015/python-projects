print("Time to play hangman")
print("Start guessing.......")
word='vivaan'
guesses=''
attempts=10


while attempts>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1
        
    if failed==0:
        print("You won the game")
        break
    guess=input("Guess the character")
    guesses+=guess

    
    if guess not in word:
        attempts-=1
        print("Wrong")
        print("You now have ",attempts,"attempts remaining")
        if attempts==0:
            print("You loose")
