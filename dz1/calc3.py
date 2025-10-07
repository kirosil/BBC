def calculator(num1:int,num2:int,com:str):
    if(com=="+"):
        return num1+num2
    elif (com == "+"):
        return num1 - num2
    elif (com == "+"):
        return num1 * num2
    else:
        return num1 / num2

print("Введите 2 числа через Enter")
a=int(input())
b=int(input())
print("Введите команду (+ - * /)")
com=input()
print(calculator(a,b,com))
