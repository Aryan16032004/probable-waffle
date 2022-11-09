def getdate():
    import datetime
    return datetime.datetime.now()
print("Press 1 for lock and 2 for retrieve")
n=int(input())
if n==1:
    print("Press 1 for food and 2 for excersise")
    n3 = int(input())
    if n3 == 1:
        print("Press 1 for Aryan,2 for Archit,  3 for Eshan ")
        n1 = int(input())
        if n1 == 1:
            R = open("aryan_food.txt", "a")
            R.write(str([str(getdate())])+":")
            R.write(input())
            R.write("\n")
            print("sumbit sucessfully")
        elif n1 == 2:
            R = open("archit_food.txt", "a")
            R.write(str([str(getdate())]) + ":")
            R.write(input())
            R.write("\n")
        elif n1 == 3:
            R = open("eshan_food.txt", "a")
            R.write(str([str(getdate())]) + ":")
            R.write(input())
            R.write("\n")
    elif n==2:
        print("Press 1 for Aryan,2 for Archit,  3 for Eshan ")
        n1 = int(input())
        if n1 == 1:
            R = open("aryan_excersice.txt", "a")
            R.write(str([str(getdate())]) + ":")
            R.write(input())
            R.write("\n")
        elif n1 == 2:
            R = open("archit_excersice.txt", "a")
            R.write(str([str(getdate())]) + ":")
            R.write(input())
            R.write("\n")
        elif n1 == 3:
            R = open("eshan_excersice.txt", "a")
            R.write(str([str(getdate())]) + ":")
            R.write(input())
            R.write("\n")
elif n==2:
    print("Press 1 for food and 2 for excersise")
    n3 = int(input())
    if n3 == 1:
        print("Press 1 for Aryan,2 for Archit,  3 for Eshan ")
        n1 = int(input())
        if n1 == 1:
            R = open("aryan_food.txt")
            content=R.read()
            print(content)
        elif n1 == 2:
            R = open("archit_food.txt", "a")
            content = R.read()
            print(content)
        elif n1 == 3:
            R = open("eshan_food.txt", "a")
            content = R.read()
            print(content)
    elif n3 == 2:
        print("Press 1 for Aryan,2 for Archit,  3 for Eshan ")
        n1 = int(input())
        if n1 == 1:
            R = open("aryan_excersice.txt")
            content = R.read()
            print(content)
        elif n1 == 2:
            R = open("archit_excersice.txt")
            content = R.read()
            print(content)
        elif n1 == 3:
            R = open("eshan_excersice.txt")
            content=R.read()
            print(content)






