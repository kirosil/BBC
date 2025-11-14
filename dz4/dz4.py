import random

global inventar
global health
global key_found
global objects
global monster_damage
global visor
global is_proklyat
inventar = []
health = 100
key_found = False

monster_damage = 20
is_proklyat = False
visor = [-1, -1]
portal = [random.randint(0, 5), random.randint(0, 5)]
chests = [[random.randint(0, 5), random.randint(0, 5)] for i in range(0, 6)]
monsters = [[random.randint(0, 5), random.randint(0, 5)] for i in range(0, 8)]
key = [random.randint(0, 5), random.randint(0, 5)]
objects = ["Маузер", "Священный грааль", "Пивная банка", "Проклятье"]



def step(xpos, ypos, vectorx, vectory):
    print(f"Текущая позиция: {xpos}, {ypos}")

    if (xpos + vectorx in range(0, 6)) and (ypos + vectory in range(0, 6)):
        return xpos + vectorx, ypos + vectory
    else:
        print("Ударился в стену")
        return xpos, ypos


def checkroom(xpos, ypos, hp, inventar, key_found):
    global portal, chests, key, monsters, monster_damage, visor, is_proklyat, health

    if [xpos, ypos] == portal:
        if key_found:
            print("Вы нашли портал и у вас есть ключ! Победа!")
            return hp, inventar, key_found, True
        else:
            print("Вы нашли портал, но вам нужен ключ")
            return hp, inventar, key_found, False

    if [xpos, ypos] in chests:
        print("Вы нашли сундук!")
        if len(inventar) > 2:
            print(
                "Инвентарь переполнен. Если вы хотите подобрать предмет, то должны выбросить один из инвентаря (хочу/не хочу)")
            imagine = input()
            if imagine == "хочу":
                inventar = removeobject(inventar)


        if objects:
            rand_item = random.randint(0, len(objects) - 1)
            addeffect(rand_item)
            inventar = appendobject(inventar, objects[rand_item])
            objects.pop(rand_item)
            chests.remove([xpos, ypos])

    if [xpos, ypos] == key:
        print("Вы нашли ключ!")
        key_found = True
        key = [-1, -1]

    if [xpos, ypos] in monsters:
        print("Вы встретили монстра! -20 здоровья")
        health -= monster_damage
        monsters.remove([xpos, ypos])
        if hp <= 0:
            print("Вы погибли!")
            return hp, inventar, key_found, True
    hp = health
    return hp, inventar, key_found, False


def addeffect(item_index):
    global monster_damage, visor, is_proklyat
    global health

    item_name = objects[item_index]
    print(f"Вы нашли {item_name}!")

    if item_name == "Маузер":
        print("Теперь монстры вам не представят особых проблем.")
        monster_damage = 15
    elif item_name == "Священный грааль":
        print("Святой дух наградил вас конским здоровьем.")
        health += 15
    elif item_name == "Пивная банка":
        print("Вам стало видно место нахождения портала.")
        visor = portal.copy()
    elif item_name == "Проклятье":
        print("Не все то золото, что блестит, теперь проклятье будет забирать у вас силу")
        is_proklyat = True


def appendobject(inventar, object):
    if object != "Проклятье":
        inventar.append(object)
        print(f"Добавлен предмет: {object}. Инвентарь: {inventar}")
    return inventar


def removeobject(inventar):
    print(f"Текущий инвентарь: {inventar}")
    if inventar:
        print("Выберите номер ячейки для удаления объекта (0 - первый предмет)")
        try:
            inventa_index = int(input())
            if 0 <= inventa_index < len(inventar):
                removed_item = inventar.pop(inventa_index)
                print(f"Удален предмет: {removed_item}")
            else:
                print("Неверный номер ячейки")
        except ValueError:
            print("Введите число")
    else:
        print("Инвентарь пуст")
    return inventar


def sortinventar(inventar):
    inventar.sort()
    print(f"Инвентарь отсортирован: {inventar}")
    return inventar


def reverseinventar(inventar):
    inventar.reverse()
    print(f"Инвентарь развернут: {inventar}")
    return inventar


cols = 6
rows = 6
matrix = [["*" for j in range(cols)] for i in range(rows)]
xpos = 0
ypos = 0

hp = health
in_labirint = True

print("Добро пожаловать в лабиринт!")
print("Управление: вверх, вниз, влево, вправо, сортировать, развернуть")

while in_labirint:
    print(f"\nЗдоровье: {hp}, Ключ: {'найден' if key_found else 'не найден'}, Инвентарь: {inventar}")

    print("Введите направление хода (вверх, влево, вправо, вниз) или действие с инвентарем (сортировать, развернуть):")
    vector = input().strip().lower()

    if vector == "вверх":
        xpos, ypos = step(xpos, ypos, 0, -1)
    elif vector == "вниз":
        xpos, ypos = step(xpos, ypos, 0, 1)
    elif vector == "вправо":
        xpos, ypos = step(xpos, ypos, 1, 0)
    elif vector == "влево":
        xpos, ypos = step(xpos, ypos, -1, 0)
    elif vector == "сортировать":
        inventar = sortinventar(inventar)
    elif vector == "развернуть":
        inventar = reverseinventar(inventar)
    else:
        print("Неизвестная команда")
        continue

    print("\nКарта лабиринта:")
    for i in range(0, 6):
        for j in range(0, 6):
            if xpos == j and ypos == i:
                print('P', end=" ")
            elif visor == [j, i]:
                print("()", end=" ")
            else:
                print(matrix[i][j], end=" ")
        print()

    hp, inventar, key_found, game_over = checkroom(xpos, ypos, hp, inventar, key_found)


    hp = health

    if is_proklyat:
        hp -= 5
        health = hp

    if game_over:
        in_labirint = False
        if hp <= 0:
            print("Игра окончена. Вы проиграли.")
        else:
            print("Поздравляем! Вы победили!")