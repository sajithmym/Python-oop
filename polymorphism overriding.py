class person1:
    def __init__(self):
        print("\n - This in person 1 class -")

    def project(self):
        print("python project")

class person2(person1):
    def __init__(self):
        print("\n - This in person 2 class -")

    def project(self):
        super().project()
        print("Django project")

class person3(person2):
    def __init__(self):
        print("\n - This in person 3 class -")

    def project(self):
        super().project()
        print("Flask project")

j = person3()
j.project()