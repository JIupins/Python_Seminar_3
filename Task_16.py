# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
from os import system
from random import randint

system('cls')

def create_number(phrase):
    number = int(input(phrase))
    return number
def create_array(num1,num2):
    collect = [randint(1, num2) for i in range(num1)]
    return collect

def find_quantity_number(arr, num_t):
    count = arr.count(num_t)
    return count

num_one = create_number("Введите колличество элементов массива: ")
num_two = create_number("Введите максимальное значение элемента массива: ")

arr = create_array(num_one,num_two)

print(arr)

num_three = create_number("Введите число колличество вхождений которого вы ищите: ")

print(find_quantity_number(arr, num_three))