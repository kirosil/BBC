print("Введите 2 числа через Enter")
a=int(input())
b=int(input())
print("Введите команду (+ - * /)")
com=input()
if(com=="+"):
    print(a+b)
elif(com=="-"):
    print(a-b)
elif(com=="*"):
    print(a*b)
else:
    print(a/b)
    