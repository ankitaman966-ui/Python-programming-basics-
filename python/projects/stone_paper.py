import random

print("\n\n")

print("---------WELCOME TO GAME WORLD OF STONE PAPER SCISSORS GAME-------------")
print("\n---Lets Plays-----")
print('''\nEnter 1 for "stone"\nEnter 2 for "paper"\nEnter 3 for "scissor"''')

def checker(you,opp):
    if(you=="stone" and opp=="scissor") or (you=="paper" and opp=="stone")or (you=="scissor" and opp=="paper"):
        print()
        print("opponent=",opp)
        print("you=",you)
        print("congrates you won the match")

    elif(you==opp):
        print()
        print("opponent=",opp)
        print("you=",you)
        print("match drawn")    

    else:
        print()
        print("opponent=",opp)
        print("you=",you)
        print("oppent won the match ! better luck next time")
        



while(True):
    print()
    computer=random.choice([1,2,3])
    options={1:"stone",2:"paper",3:"scissor"}
    opp=options[computer]
    yourmove=int(input("enter the your move :"))

    if yourmove not in [1,2,3]:
        print("please enter the valid move of the game ! re-enter the move")
        continue

    you=options[yourmove]

    checker(you,opp)

    ch=input("\nyou want to play more(Y/N) :")
    if(ch=="n" or ch=="N"):
        break

print()
print("thanks for playing good luck! come again")



