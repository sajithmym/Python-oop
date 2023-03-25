class MyClass:

    var = 100

    def __init__(self,name):
        self.Name = name
        self.var2 = 200

    def greet(self):
        print("Welcome",self.Name)

obj = MyClass("sajith")
obj.greet()

print(f"\n Var Value is {obj.var}  \t Var2 Value is {obj.var2}")

fun = lambda a,b : a*b+10
print(fun(10,9))