def table() :
    n=int(input("ENTER A NO WHOSE TABLE IS TO BE PRINTED :"))
    for i in range(1,11) :
        value=n*i
        print(n,"X",i,"=",value)
table()