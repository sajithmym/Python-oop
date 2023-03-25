class MyClass:

    var = 100

    def __init__(self,name):
        self.Name = name

    def greet(self):
        print("Welcome",self.Name)

obj = MyClass("sajith")
obj.greet()

print(obj.var)