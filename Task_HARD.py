# Имеется список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность.
# Порядок элементов менять нельзя. Одно число - это не последовательность.
from os import system
from random import randint

def create_number(phrase):
    number = int(input(phrase))
    return number

def create_array(num1, num2):
    collect = [randint(1, num2) for i in range(num1)]
    print(f"Sgenerirovan massiv elementov: {collect}")
    collect.sort()
    print(f"Massiv elementov otsortirovan: {collect}")
    return collect

def fing_list(collect):
    max, j = 0, 0
    while j < len(collect) - 1:
        i, count = 0, 0
        while i + j < len(collect) - 1:
            if collect[i + j] == collect[i + j + 1] - 1:
                count += 1
                i += 1
            else:
                break
        if count > max:
            max = count
            list1 = [collect[i + j - max], collect[i+j]]
        j += 1
    print(f"Posledovatelnost {list1} iz {max + 1} chisel.") if max > 0 else print(f"Posledovatelnosti net!")

num1 = create_number("Vvedite collichestvo elementov massiva: ")
num2 = create_number("Vvedite maksimalnoe znachenie elementa massiva: ")
array = create_array(num1, num2)

fing_list(array)