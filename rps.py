import random
print("Made by Shobhit")
def main():
    user_s=0
    comp_s=0
    i=0
    round=rounds()
    while i<round:
        options=['ROCK','PAPER','SCISSORS']
        user=input("Enter Rock,Paper or Scissors: ").upper().strip()
        comp=random.choice(options)
        if user=='STOP':
            break
        elif user not in options:
            print("Enter a valid option")
            continue
        
        
        #user wins
        print(f"You chose {user}")
        print(f"The computer chose {comp}")
        if user=="PAPER" and comp=="ROCK":
            print("paper covers the rock,You win this round!")
            user_s+=1
        elif user=="SCISSORS" and comp=="PAPER":
            print("scissors cuts paper,You win this round!")
            user_s+=1
        elif user=="ROCK" and comp=="SCISSORS":
            print("Rock breaks the scissors,You win this round!")
            user_s+=1
        #comp wins
        elif comp=="PAPER" and user=="ROCK":
            print("paper covers the rock,You lose this round!")
            comp_s+=1
        elif comp=="SCISSORS" and user=="PAPER":
            print("scissors cuts paper,You lose this round!")
            comp_s+=1
        elif comp=="ROCK" and user=="SCISSORS":
            print("Rock breaks the scissors,You lose this round!")
            comp_s+=1
        else:
            print("It's a draw.")
        i+=1
    print(f"Your final Score is {user_s}\nComp's final score is {comp_s}")


def rounds():
    while True:
        try:
            round=int(input("How many rounds of RPS do you want to play? "))
        except:
            print("Enter a valid number")
            continue
        else:
            return round

main()
