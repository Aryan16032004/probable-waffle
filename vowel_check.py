list=['a','o','i','e','u','A','E','I','O','U']
i=1
while i!=0:
    x=input("input an alpahabet or 9 for exit: ")
    if x=='9':
        break
    elif x  in list:
        print("vowel")
    elif x not in list:
        print("not a vowel")
    else:
        print("wrong input")

