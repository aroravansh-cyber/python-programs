import random

print("""
        ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║  ███╗   ██╗ ██╗   ██╗ ███╗   ███╗ ██████╗  ███████╗ ██████╗                                                                           ║
        ║  ████╗  ██║ ██║   ██║ ████╗ ████║ ██╔══██╗ ██╔════╝ ██╔══██╗                                                                          ║
        ║  ██╔██╗ ██║ ██║   ██║ ██╔████╔██║ ██████╔╝ █████╗   ██████╔╝                                                                          ║
        ║  ██║╚██╗██║ ██║   ██║ ██║╚██╔╝██║ ██╔══██╗ ██╔══╝   ██╔══██╗                                                                          ║
        ║  ██║ ╚████║ ╚██████╔╝ ██║ ╚═╝ ██║ ██████╔╝ ███████╗ ██║  ██║                                                                          ║
        ║  ╚═╝  ╚═══╝  ╚═════╝  ╚═╝     ╚═╝ ╚═════╝  ╚══════╝ ╚═╝  ╚═╝                                                                          ║
        ║                                                                                                                                       ║
        ║                                                ██████╗   ██╗   ██╗ ███████╗ ███████╗ ███████╗                                         ║
        ║                                                ██╔════╝  ██║   ██║ ██╔════╝ ██╔════╝ ██╔════╝                                         ║          
        ║                                                ██║  ███╗ ██║   ██║ █████╗   ███████╗ ███████╗                                         ║
        ║                                                ██║   ██║ ██║   ██║ ██╔══╝   ╚════██║ ╚════██║                                         ║
        ║                                                ╚██████╔╝ ╚██████╔╝ ███████╗ ███████║ ███████║                                         ║
        ║                                                 ╚═════╝   ╚═════╝  ╚══════╝ ╚══════╝ ╚══════╝                                         ║
        ║                                                                                                                                       ║
        ║                                                                                       ██████╗   █████╗  ███╗   ███╗ ███████╗          ║
        ║                                                                                      ██╔════╝  ██╔══██╗ ████╗ ████║ ██╔════╝          ║
        ║                                                                                      ██║  ███╗ ███████║ ██╔████╔██║ █████╗            ║
        ║                                                                                      ██║   ██║ ██╔══██║ ██║╚██╔╝██║ ██╔══╝            ║
        ║                                                                                      ╚██████╔╝ ██║  ██║ ██║ ╚═╝ ██║ ███████╗          ║
        ║                                                                                       ╚═════╝  ╚═╝  ╚═╝ ╚═╝     ╚═╝ ╚══════╝          ║                          
        ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""")
print("""
        ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                                                                                                                                       ║
        ║        RULES: IN THIS GAME THREE LEVEL WILL BE THERE EACH LEVEL HAS DIFFICULTY AS PER THE LEVEL                                       ║
        ║               1. Easy level number range will be 0-50 and you have 15 attempts to guess the number                                    ║
        ║               2. Medium Level number range will be 0-70 and you have 12 attempts to guess the number                                  ║
        ║               3. Hard level number range will be 0-100 and you have only 10 attempts to guess the number                              ║
        ║               4. Legend level number range will be 0-100 and you have 5 attempts to guess the number                                  ║ 
        ║               5. Custom you are able to set attempts and number range according to you                                                ║
        ║                                                                                                                                       ║
        ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝                
     """)
while True:
        print("""YOU NEED TO SELECT ONE OPTION ACCORDING TO YOUR LEVEL
                1. EASY LEVEL
                2. MEDIUM LEVEL
                3. HARD LEVEL 
                4. LEGENDARY LEVEL
                5. CUSTOM LEVEL
                6. EXIT
              """)
        level_choice=int(input("ENTER YOUR LEVEL CHOICE:"))
        if level_choice==1:     #easy level
                random_number=random.randint(0,50)
                attempts=15
                while attempts > 0:
                        user_number=int(input("ENTER YOUR GUESSING NUMBER:  "))
                        if user_number==random_number:
                                print("CONGRATUTIONS YOU WIN NUMBER IS ",random_number)
                                print("*"*86)
                                break
                        elif user_number<random_number:
                                print("Too LOW!!")
                                print("")
                                print("*"*86)
                        elif user_number>random_number:
                                print("Too HIGH!!")
                                print("")
                                print("*"*86)
                        else:
                                print("YOU ENTER WRONG NUMBER")
                                print("")
                                print("*"*86)
                                continue
                        attempts=attempts-1
                        print("LEFT ATTEMPTS: ",attempts)
                if attempts==0 :
                        print("YOU LOST THE GAME THE CORRECT NUMBER IS ",random_number)        
        elif level_choice==2:   #medium level
                random_number=random.randint(0,70)
                attempts=12
                while attempts > 0:
                        user_number=int(input("ENTER YOUR GUESSING NUMBER:  "))
                        if user_number==random_number:
                                print("CONGRATUTIONS YOU WIN NUMBER IS ",random_number)
                                print("*"*86)
                                break
                        elif user_number<random_number:
                                print("Too LOW!!")
                                print("")
                                print("*"*86)
                        elif user_number>random_number:
                                print("Too HIGH!!")
                                print("")
                                print("*"*86)
                        else:
                                print("YOU ENTER WRONG NUMBER")
                                print("")
                                print("*"*86)
                                continue
                        attempts=attempts-1
                        print("LEFT ATTEMPTS: ",attempts)
                if attempts==0 :
                        print("YOU LOST THE GAME  THE CORRECT NUMBER IS ",random_number)    
        elif level_choice==3:   #hard level
                        random_number=random.randint(0,100)
                        attempts=10
                        while attempts > 0:
                                user_number=int(input("ENTER YOUR GUESSING NUMBER:  "))
                                if user_number==random_number:
                                        print("CONGRATUTIONS YOU WIN NUMBER IS ",random_number)
                                        print("*"*86)
                                        break
                                elif user_number<random_number:
                                        print("Too LOW!!")
                                        print("")
                                        print("*"*86)
                                elif user_number>random_number:
                                        print("Too HIGH!!")
                                        print("")
                                        print("*"*86)
                                else:
                                        print("YOU ENTER WRONG NUMBER")
                                        print("")
                                        print("*"*86)
                                        continue
                                attempts=attempts-1
                                print("LEFT ATTEMPTS: ",attempts)
                        if attempts==0 :
                                print("YOU LOST THE GAME  THE CORRECT NUMBER IS ",random_number)    
        elif level_choice==4:   #legendary level
                        random_number=random.randint(0,100)
                        attempts=5
                        while attempts > 0:
                                user_number=int(input("ENTER YOUR GUESSING NUMBER:  "))
                                if user_number==random_number:
                                        print("CONGRATUTIONS YOU WIN NUMBER IS ",random_number)
                                        print("*"*86)
                                        break
                                elif user_number<random_number:
                                        print("Too LOW!!")
                                        print("")
                                        print("*"*86)
                                elif user_number>random_number:
                                        print("Too HIGH!!")
                                        print("")
                                        print("*"*86)
                                else:
                                        print("YOU ENTER WRONG NUMBER")
                                        print("")
                                        print("*"*86)
                                        continue
                                attempts=attempts-1
                                print("LEFT ATTEMPTS: ",attempts)
                        if attempts==0 :
                                print("YOU LOST THE GAME THE CORRECT NUMBER IS ",random_number)    
        elif level_choice==5:   #custom level
                        starting_point=int(input("ENTER THE STARTING POINT OF NUMBER GUESSING GAME: "))         #taking starting point from the user
                        ending_point=int(input("ENTER THE ENDING POINT OF NUMBER GUESSING GAME: "))             #taking ending point from the user
                        random_number=random.randint(starting_point,ending_point)
                        attempts=int(input("ENTER THE ATTEMPTS IN NUMBER :"))
                        while attempts > 0:
                                user_number=int(input("ENTER YOUR GUESSING NUMBER:  "))
                                if user_number==random_number:
                                        print("CONGRATUTIONS YOU WIN NUMBER IS ",random_number)
                                        print("*"*86)
                                        break
                                elif user_number<random_number:
                                        print("Too LOW!!")
                                        print("")
                                        print("*"*86)
                                elif user_number>random_number:
                                        print("Too HIGH!!")
                                        print("")
                                        print("*"*86)
                                else:
                                        print("YOU ENTER WRONG NUMBER")
                                        print("")
                                        print("*"*86)
                                        continue
                                attempts=attempts-1
                                print("LEFT ATTEMPTS: ",attempts)
                        if attempts==0 :
                                print("YOU LOST THE GAME  THE CORRECT NUMBER IS ",random_number)    
        elif level_choice=="exit":
                print("YOU ARE EXIT FROM THE GAME!!")
                break