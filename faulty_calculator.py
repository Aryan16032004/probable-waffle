#Faulty Calculator
# 45*3=555 , 56+7=77 ,56/6=4 design a calculator which do correct calculations except these three
print("enter value of a")
a=int(input())
print("enter value of b")
b=int(input())
print("Enter your choice(+-*/)")
opp=input()
if opp=='+':
    if a==56 and b==7:
        print(77)
    else:
        print(a+b)
elif opp=='-':
    print(a-b)
elif opp=='*':
    if a==45 and b==3:
        print(555)
    else:
        print(a*b)
elif opp=='/':
    if a==56 and b==6:
        print(4)
else :
    print(a/b)
