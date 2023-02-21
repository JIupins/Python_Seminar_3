# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
from random import randint


def create_number(phrase):
    number = int(input(phrase))
    return number


def create_array(num1, num2):
    collect = [randint(1, num2) for i in range(num1)]
    return collect


def find_near_number(arr, num):
    min_value = abs(abs(num) - abs(arr[0]))
    min_number = arr[0]
    for i in range(len(arr) - 1):
        if abs(abs(num) - abs(arr[i])) < min_value:
            min_value = abs(abs(num) - abs(arr[i]))
            min_number = arr[i]
    print(f"В рассматриваемом массиве первым самым близким по значению числом к числу {num}", end=' ')
    print(f" является число {min_number}, разница между ними составляет {min_value}.")


num_one = create_number("Введите колличество элементов массива: ")
num_two = create_number("Введите максимальное значение элемента массива: ")

arra = create_array(num_one, num_two)

print(arra)

num_three = create_number("Задайте любое число: ")

find_near_number(arra, num_three)
