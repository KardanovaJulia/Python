#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

a = int (input("Введите число от 1 до 7: "))
if a <= 5:
    print ("Будний день")
else:
    print ("Выходной день")

#2.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт 
#номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input("x="))
y = int(input("y="))
if x>0 and y>0:
    print('1 четверть')
elif x<0 and y>0:
    print('2 четверть')
elif x<0 and y<0:
    print('3 четверть')
elif x>0 and y<0:
    print('4 четверть')

# 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

number = int(input("Введите номер четверти в диапозоне от 1 до 4: "))
if number == 1:
    print ("x>0, y>0")
elif number == 2:
    print ("x<0, y>0")
elif number == 3:
    print ("x<0, y<0")
elif number == 4: 
    print ("x>0, y<0")
elif number >= 5:
    print ("Введите номер от 1 до 4")

# 4.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a
def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result
statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение является истиной")
else:
    print(f"Утверждение является ложью")

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math
A1 = int(input("Введите координаты A= "))
A2 = int(input("Введите координаты A= "))
B1 = int(input("Введите координаты B= "))
B2 = int(input("Введите координаты B= "))
distance = math.sqrt((B1 - A1)**2 + (B2 - A2)**2) 
print (distance)