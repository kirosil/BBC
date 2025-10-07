import math


class BigCalculator:
    def __init__(self,num1:int,num2:int,com:str):
        self.num1 = num1
        self.num2 = num2
        self.com=com

    def norm_calculator(self):
        if (self.com == "+"):
            return self.num1 + self.num2
        elif (self.com == "+"):
            return self.num1 - self.num2
        elif (self.com == "+"):
            return self.num1 * self.num2
        else:
            return self.num1 / self.num2

    def inzh_calculator(self):
        if(self.com == "sin"):
            return math.sin(self.num1)
        else:
            return math.cos(self.num1)



print( "Введите 2 числа через Enter" )
a = int(input())
b = int(input())


print("Введите калькулятор И/О")
calculator=input()
if(calculator=="И"):
    print("Введите команду sin,cos")
    com = input()
    bigs = BigCalculator(a, b, com)
    print(bigs.inzh_calculator())
else:
    print("Введите команду (+ - * /)")
    com = input()
    bigs = BigCalculator(a, b, com)
    print(bigs.norm_calculator())

