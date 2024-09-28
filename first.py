import random
target=random.randint(1,100)

while True:
    userChoice=input("Guess the target or Quit(Q):")
    if(userChoice=="Q"):
        break

    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success,Correct Guess!!!")
        break
    elif(userChoice>target):
        print("Too Big,Guess a Smaller number...")
    else:
        print("Too Small,Guess a Bigger number...")

print("---GAME OVER---")