def square(s):  #function of square pattern choice 1
    for i in range(s):
        print("*"*s)
def righttriangle(s):   #function of right triangle pattern choice 2
    for i in range(1,s+1):
        print("*"*i)
def inverttriangle(s):  #function of inverted triangle pattern choice 3
    for i in range(s,0,-1):
        print("*"*i)
def pyramid(s): #function of pyramid pattern choice 4
    for i in range(1,s+1):
        print(" "*(s-i),"*"*(2*i-1))
def diamond(s): #function of diamond pattern choice 5
    for i in range(1,s+1):
        print(" "*(s-i),"*"*(2*i-1))
    for i in range(s-1,0,-1):
        print(" "*(s-i),"*"*(2*i-1))
      
while True:
    print(""" ENTER PATTERN TYPE
                1. Square Pattern
                2. Right Triangle Pattern
                3. Left Angle Triangle Pattern
                3. Inverted Triangle Pattern
                4. Pyramid Pattern
                5. Diamond Pattern
                6. Number Pattern
                7. Floyd's Triangle Pattern
                8. Pascal's Triangle Pattern
                9. X pattern
                10. Heart Pattern
                11. Zig Zag Pattern
                12. Spiral Pattern
                13. Alphabet Pyramid Pattern
                14. Aplphabet Triangle Pattern
                15. Alphabet Square Pattern
                16. Hollow Diamond Pattern
                17. Butterfly Pattern
                18. Hourglass Pattern
                19. Right Pascal
                20. Inverted Pyramid
    """)
    choice=int(input("ENTER YOUR CHOICE"))
    if choice == 1:
        s=int(input("enter the size of square:"))
        square(s)
    elif choice == 2:
        s=int(input("enter the size of right triangle:"))
        righttriangle(s)
    elif choice == 3:
        s=int(input("enter the size of inverted tiangle:"))
        inverttriangle(s)
    elif choice == 4:
        s=int(input("ENTER THE SIZE OF PYRAMID:"))
        pyramid(s)
    elif choice == 5:
        s=int(input("ENTER THE SIZE OF DIAMOND:"))
        diamond(s)
    elif choice == 6:
            s=int(input("ENTER THE SIZE OF PYRAMID:"))
            pyramid(s)
    elif choice == 7:
            s=int(input("ENTER THE SIZE OF PYRAMID:"))
            pyramid(s)
    elif choice == 8:
            s=int(input("ENTER THE SIZE OF PYRAMID:"))
            pyramid(s)
    elif choice == 9:
            s=int(input("ENTER THE SIZE OF PYRAMID:"))
            pyramid(s)
    elif choice == 10:
            s=int(input("ENTER THE SIZE OF PYRAMID:"))
            pyramid(s)
    elif choice == 11:
            s=int(input("ENTER THE SIZE OF PYRAMID:"))
            pyramid(s)
    elif choice == 12:
            s=int(input("ENTER THE SIZE OF PYRAMID:"))
            pyramid(s)
    elif choice == 13:
            s=int(input("ENTER THE SIZE OF PYRAMID:"))
            pyramid(s)
    elif choice == 14:
            s=int(input("ENTER THE SIZE OF PYRAMID:"))
            pyramid(s)
    elif choice == 15:
            s=int(input("ENTER THE SIZE OF PYRAMID:"))
            pyramid(s)
    elif choice == 16:
            s=int(input("ENTER THE SIZE OF PYRAMID:"))
            pyramid(s)
    elif choice == 17:
            s=int(input("ENTER THE SIZE OF PYRAMID:"))
            pyramid(s)
    elif choice == 18:
                s=int(input("ENTER THE SIZE OF PYRAMID:"))
                pyramid(s)
    elif choice == 19:
                s=int(input("ENTER THE SIZE OF PYRAMID:"))
                pyramid(s)
    elif choice == 20:
                s=int(input("ENTER THE SIZE OF PYRAMID:"))
                pyramid(s)
    elif choice == "exit":
        break
    else:
        print("INVALID OPTION")
        print("")
        print("_"*87)
        continue
