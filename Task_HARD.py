# Имеется список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность.
# Порядок элементов менять нельзя. Одно число - это не последовательность.
from random import randint


def create_number(phrase):
    number = int(input(phrase))
    return number


def create_array(num1, num2):
    collect = [randint(1, num2) for i in range(num1)]
    print(f"Создан массив элементов: {collect}")
    collect.sort()
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
            list1 = [collect[i + j - max], collect[i + j]]
        j += 1
    print(f"Максимальная возрастающую последовательность равна {list1}, и состоит из {max + 1} чисел.") \
        if max > 0 else print(f"Последовательности нет!")


num1 = create_number("Введите колличество элементов массива: ")
num2 = create_number("Введите максимальное значение элемента массива: ")
array = create_array(num1, num2)

fing_list(array)
