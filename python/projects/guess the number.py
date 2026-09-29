import random

print("\n------------welcome to guessing the number game-----------\n\n")
print("guess the number in between (1 to 100)\n")

n=random.randint(1,100)
guess=0
times=0
while(guess != n):
    times+=1
    guess=int(input("\nguess the number :"))
    if(guess==n):
        print(f"\nyou are correctly guessed the number in {times} moves")
    elif(guess>n):
        print("\nnumber is lower than the guessed number, please guess again")
    else:
        print("\nnumber is greater than the guessed number, please guess again")