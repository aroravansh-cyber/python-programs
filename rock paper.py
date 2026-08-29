import random
print("""TO PLAY THE GAME YOU NEED TO ENTER ONE NUMBER
        RULES: 1. Minimum 1 round you need to play
               2. Maximum 13 rounds you need to play
""")
rounds=int(input("ENTER THE ROUNDS:"))
print("""


""")
print("*"*76)

if rounds < 1 or rounds > 13:
    print("ENTER ROUND BETWEEN 1 AND 13")
    exit()
if (rounds%2!=0):
    print("You Have selected ",rounds," Rounds")
elif (rounds%2==0):
    rounds-=1
    print("YOU ENTERED THE EVEN NUMBER IT HAS BEEN CHANGED TO MAKING GAME FAIR NOW ROUNDS WILL BE", rounds,"rounds")
else:
    print("please enter valid number to continue the game")
user_win=0
computer_win=0
current_round=1
while current_round <= rounds:
    print("ROUND",current_round)
    print("*"*76)
    print("""
    enter r for Rock
    enter p for paper
    enter s for scissor
""")
    user_choice=input("SELECT ONE OPTION TO CONTINUE GAME: ")
    computer_choice=random.choice(["r","p","s"])
    name={
        "r":"Rock",
        "p":"Paper",
        "s":"Scissor",
    }
    print("COMPUTER CHOICE IS:",computer_choice)
    if user_choice == computer_choice:
        print("Round Draw!")
    elif (user_choice == "r" and computer_choice == "s") or (user_choice == "p" and computer_choice == "r") or (user_choice == "s" and computer_choice == "per"):
        user_win += 1
        print("")
        print("")
        print("You win this round!")
        print("")
    elif (computer_choice == "r" and user_choice == "s") or (computer_choice == "p" and user_choice == "r") or (computer_choice == "s" and user_choice == "p"):
        computer_win += 1
        print("")
        print("")
        print("Computer win this round!")
        print("")
    else:
        print("YOU ENTER WRONG OPTION")
        continue
    print("_"*86)
    current_round += 1
print("="*86)
print("""                                         SCORE CARD                                      """)
print("YOUR SCORE IS:",user_win)
print("COMPUTER SCORE IS:",computer_win)
if user_win > computer_win:
    print("""
                                         ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
                                         ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
                                          ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
                                           ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
                                            ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
                                            ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
""")
elif computer_win > user_win:
    print("""
                                        ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗████████╗
                                        ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝╚══██╔══╝
                                         ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗   ██║
                                          ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║   ██║
                                           ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║   ██║
                                           ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝
""") 
else:
    print("""
                                        ██████╗ ██████╗  █████╗ ██╗    ██╗
                                        ██╔══██╗██╔══██╗██╔══██╗██║    ██║
                                        ██║  ██║██████╔╝███████║██║ █╗ ██║
                                        ██║  ██║██╔══██╗██╔══██║██║███╗██║
                                        ██████╔╝██║  ██║██║  ██║╚███╔███╔╝
                                        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝
""")