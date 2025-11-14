def summer(chis1:int,chis2:int)->int:
    return chis1+chis2
def minuser(chis1:int,chis2:int)->int:
    return chis1-chis2
def umnozher(chis1:int,chis2:int)->int:
    return chis1*chis2
def delener(chis1:int,chis2:int)->float:
    return chis1/chis2
print("Введите 2 числа через Enter")
a=int(input())
b=int(input())
print("Введите команду (+ - * /)")
com=input()
if(com=="+"):
    print(summer(a,b))
elif(com=="-"):
    print(minuser(a,b))
elif(com=="*"):
    print(umnozher(a,b))
else:
    print(delener(a,b))
