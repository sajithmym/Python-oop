class Now:

    def __init__(self):
        print("\n - I am Working First Class...")
    
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        elif a!=None:
            print(a)
        else:
            print("\t No Argument Found...")

i = Now()
i.add()
i.add(10)
i.add(10,15)
i.add(10,25,35)


class Sec:
    def __init__(self):
        print("\n - I am Working 2nd Class...")

    def add(self,*args):
        tot = 0
        for i in args:
            tot+=i
        print(f"Totel is {tot}")

i = Sec()
i.add()
i.add(10)
i.add(10,15)
i.add(10,25,35)
