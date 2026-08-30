n=input("Enter a number : ")
l=list(n)
ln=l[::-1]
if l==ln :
    print(n,"is a palindrome")
else :
    print(n,"is not a palindrome")