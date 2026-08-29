import pyttsx3

engine=pyttsx3.init()
print("__"*62)
print("PROGRAM TO GENERTATE TRUTH TABLE USING LOGIC OPERATOR IN PYTHON")
print("__"*62)
engine.say("PROGRAM TO GENERTATE TRUTH TABLE USING LOGIC OPERATOR IN PYTHON")
engine.runAndWait()
#taking input from user to give table according to the user
while True:
    operator=input("Enter the logic operator AND, OR, NOT, NAND, NOR & exit to quit:")
    operator=operator.lower()
    a = True
    b = False
#applying condition to give proper data to user
    if operator=="exit":
        print("YOU ARE EXITED FROM GIVEN LOGICAL GATE TRUTH TABLE PROGRAM")
        break
    elif(operator=="and"):
        print("|","A","|","B","|","A.B","|")
        print("|",int(b),"|",int(b),"|",int(b) and int(b),"  |")
        print("|",int(b),"|",int(a),"|",int(b) and int(a),"  |")
        print("|",int(a),"|",int(b),"|",int(a) and int(b),"  |")
        print("|",int(a),"|",int(a),"|",int(a) and int(a),"  |")
    elif(operator=="or"):
        print("|","A","|","B","|","A+B","|")
        print("|",int(b),"|",int(b),"|",int(b) or int(b),"  |")
        print("|",int(b),"|",int(a),"|",int(b) or int(a),"  |")
        print("|",int(a),"|",int(b),"|",int(a) or int(b),"  |")
        print("|",int(a),"|",int(a),"|",int(a) or int(a),"  |")
    elif(operator=="not"):
        print("|","A","|","A'","|")
        print("|",int(b),"|",int(not(b))," |")
        print("|",int(a),"|",int(not(a))," |")
    elif(operator=="nand"):
        print("|","A","|","B","|","A`.B`","|")
        print("|",int(b),"|",int(b),"|",int(not(b and b)),"    |")
        print("|",int(b),"|",int(a),"|",int(not(b and a)),"    |")
        print("|",int(a),"|",int(b),"|",int(not(a and b)),"    |")
        print("|",int(a),"|",int(a),"|",int(not(a and a)),"    |")
    elif(operator=="nor"):
        print("|","A","|","B","|","A`+B`","|")
        print("|",int(b),"|",int(b),"|",int(not(b or b)),"    |")
        print("|",int(b),"|",int(a),"|",int(not(b or a)),"    |")
        print("|",int(a),"|",int(b),"|",int(not(a or b)),"    |")
        print("|",int(a),"|",int(a),"|",int(not(a or a)),"    |")
    else:
        print("ERROR!! you enter wrong keyword")
