def level1():
    print("Какой метод хочешь использовать? (U/L/C)")
    command = str(input())
    print("Введите строку")
    string = str(input())
    if (command == "U"):
        string = string.upper()
    elif (command == "L"):
        string = string.lower()
    elif (command == "C"):
        string = string.capitalize()
    print(string)
    level2()
def level2():
    print("Какой метод хочешь использовать? (F/R/C)")
    command = str(input())
    print("Введите строку")
    string = str(input())
    counter = int(0)
    if (command == "F"):
        print("Введите строку, которую хочешь найти")
        find_str = str(input())
        print(string.find(find_str))
    elif (command == "R"):
        print("Введите строку, которую хочешь заменить")
        replace_str = str(input())
        print("Введите строку, на которую хочешь заменить")
        replace2_str = str(input())
        print(string.replace(replace_str, replace2_str))
    elif (command == "C"):
        print("Введите строку, количество которой хочешь найти")
        print(string.count("о"))
    level3()
def level3():
    print("Какой метод хочешь использовать? (S/J)")
    command = str(input())
    print("Введите строку")
    string = str(input())
    if (command == "S"):
        print("Введите строку,по которой хочешь разбить")
        split_str = str(input())
        print(string.split(split_str))
    elif (command == "J"):
        print("Введите строку,по которую хочешь добавить")
        join_str = str(input())
        print(string.join(join_str))
    level4()
def level4():
    print("Какой метод хочешь использовать? (ID/IA/S/F)")
    command = str(input())
    print("Введите строку")
    string = str(input())
    if (command == "ID"):
        print(string.isdigit())
    elif (command == "IA"):
        print(string.isalpha())
    elif (command=="S"):
        print("Введите символы,которые хочешь убрать")
        strip_str=str(input())
        print(string.strip(strip_str))
    elif(command=="F"):
        print("Введите символы,которые хочешь добавить")
        strip_str = str(input())
        string = f"{strip_str}"+string
        print(string.format({strip_str}))
    level5()
def level5():
    print("Введите строку")
    string = str(input())
    string=string.strip(" ").capitalize().replace(";"," ")
    print(string)

level5()