n=int(input("Enter the no. of rows you want to print: "))
a=int(input("Enter 1 or 0: "))
b=bool(a)
if b== True:
    i=1
    while(i<=n):
        print(i*"*")
        i=i+1
elif a== False:
    i = n
    while (i >= 1):
        print(i * "*")
        i = i - 1
