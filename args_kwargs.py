# args and kwargs are used to make easy for us to add a name or anything easily
def function(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key ,value in kwargs.items():
        print(f"{key} have {value}")


ary=["Aryan","Sakshi","Eshan","Ram","Archit","Aman","Siddhu"]
normal="I am Not smart"
kw={"Aryan":"Engineer", "Eshan":"Doctor"}
function(normal, *ary, **kw)