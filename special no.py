def fact(n):

    if n==1 or n==0:

        return 1
    else:

        return n*fact(n-1)
a=int(input("Enter the number: "))
n=a
s=0
while n>0:
    r=n%10
    s=s+(fact(r))
    n=n//10
if s==a:
    print("Special Number")
else:
    print("Not a special number")




