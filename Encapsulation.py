from pyfiglet import *

class Bank:

    __balance = 500000

    def __init__(self,withrow):
        print(" I am Working")
        self.__amount = withrow
    
    def show(self):
        print(f"\n {figlet_format(f'Balance {self.__balance}')}\n \
               {figlet_format(f'Withrow {self.__amount}')}")


j = Bank(1000)
j.show()

try:
    j.__balance
except Exception as d:
    print(f"\t - {d} -")

try:
    j.__amount
except Exception as d:
    print(f"\t - {d} -")