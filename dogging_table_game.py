import random

print(''' LEVELs  :
1. EASY 
2. MEDIUM
3. HARD 
4. CUSTOM
5. LEGENDARY
6. EXIT''')
choice=int(input("Enter your choice :"))
if choice==1 :
    score=0
    print("** YOU ARE IN EASY LEVEL **")
    for i in range(1,11) :
        print("ROUND ",i)
        no1=random.randint(1,4)
        no2=random.randint(1,10)
        product=no1*no2
        print("what is ",no1,"X",no2,"=")
        user=int(input("ANSWER :"))
        if product==user :
            score+=5
        else :
            score-=1
    print("Your Score is ",score)
    percentage=score*2
    print("your winning percentage is :",percentage,"%")
elif choice==2 :
    score=0
    print("** YOU ARE IN MEDIUM LEVEL **")
    for i in range(1,21) :
        print("ROUND ",i)
        no1=random.randint(1,10)
        no2=random.randint(1,10)
        product=no1*no2
        print("what is ",no1,"X",no2,"=")
        user=int(input("ANSWER :"))
        if product==user :
            score+=5
        else :
            score-=2
    print("Your Score is ",score)
    percentage=score
    print("your winning percentage is :",percentage,"%")
elif choice==3 :
    score=0
    print("** YOU ARE IN HARD LEVEL **")
    for i in range(1,31) :
        print("ROUND ",i)
        no1=random.randint(1,20)
        no2=random.randint(1,10)
        product=no1*no2
        print("what is ",no1,"X",no2,"=")
        user=int(input("ANSWER :"))
        if product==user :
            score+=5
        else :
            score-=3
    print("Your Score is ",score)
    percentage=(score*2)/3
    print("your winning percentage is :",percentage,"%")
elif choice==4 :
    score=0
    print("** YOU ARE IN CUSTOM LEVEL **")
    round=int(input("ENTER NUMBER OF ROUND YOU WANT TO PLAY :"))
    start=int(input("ENTER A STARTING POINT OF THE LEVEL :"))
    end=int(input("ENTER A ENDING POINT OF THE LEVEL :"))
    mark1=int(input("ENTER A NUMBER WHICH WILL USED POSITIVE MARKING :"))
    mark2=int(input("ENTER A NUMBER WHICH WILL USED NEGATIVE MARKING :"))
    for i in range(1,round+1) :
        print("ROUND ",i)
        no1=random.randint(start,end)
        no2=random.randint(start,end)
        product=no1*no2
        print("what is ",no1,"X",no2,"=")
        user=int(input("ANSWER :"))
        if product==user :
            score+=mark1
        else :
            score-=mark2
    print("Your Score is ",score)
    total=mark1*round
    percentage=(score/total)*100
    print("your winning percentage is :",percentage,"%")
elif choice==5 :
    score=0
    print("** YOU ARE IN LEGENDARY LEVEL **")
    for i in range(1,51) :
        print("ROUND ",i)
        no1=random.randint(1,50)
        no2=random.randint(1,10)
        product=no1*no2
        print("what is ",no1,"X",no2,"=")
        user=int(input("ANSWER :"))
        if product==user :
            score+=5
        else :
            score-=5
    print("Your Score is ",score)
    percentage=(score*2)/5
    print("your winning percentage is :",percentage,"%")
elif choice==6 :
    print("** YOU ARE EXIT FROM THE GAME **")
else :
    print("INVALID CHOICE")
