# Важно: не использовать циклы для реализации основной логики.
#
# Нужно использовать рекурсию.
#
# Цикл можно использовать только в 4 задании для нахождения суммы чисел.
#
#
#
# Задание 1.
#
# Написать рекурсивную функцию нахождения степени числа.
#
# def number_degree(number, degree) -> int:
#     if degree == 1:
#         return number
#     if degree == 0:
#         return 1
#     if degree < 0:
#         raise Exception("Please, enter positive degree")
#     return number * number_degree(number, degree - 1)
#
# try:
#     print(number_degree(number=5, degree=3))
#
#     print(number_degree(number=2, degree=0))
#
#     print(number_degree(number=3, degree=-2))
#
# except Exception as error:
#     print(error)


#
# Задание 2.
#
# Написать рекурсивную функцию, которая выводит N звезд в ряд, число N задает пользователь.
# Проиллюстрируйте работу функции примером. (протестировать)
#
# def my_star(n) -> str:
#     if n > 0:
#         print("*", end="")
#         my_star(n-1) #не пишу return так как функция выводит принт
#     else:
#         return print()
# try:
#     number = int(input("Enter your number: "))
#     my_star(number)
# except Exception as error:
#     print(error)


# Задание 3.
#
# Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a до b.
# Пользователь вводит a и b. Проиллюстрируйте работу функции примером.
#
#
# def diap_nums(a, b) -> int:
#
#     if a == b:
#         return a
#
#     if a < b:
#         total = 0
#         total = total + a
#         return total + diap_nums(a + 1, b)
#
#     if a > b:
#         a, b = b, a
#         return diap_nums(a, b)
#
# try:
#     print(diap_nums(1, 8))
#     print(diap_nums(8, 1))
#     print(diap_nums(-8, 1))
# except Exception as error:
#     print(error)





########
# Дополнительно:
#
# Задание 4.
#
# Напишите рекурсивную функцию, которая принимает одномерный массив из 100 целых чисел
# заполненных случайным образом и находит позицию, с которой начинается последовательность из 10 чисел,
# сумма которых минимальна.

import math
import random

#Рабочая версия

# inf : Константа math. inf возвращает положительную бесконечность,
# значение которое является типом float и может присутствовать в математических выражениях.

def min_sum_index(numbers, start_index, end_index, min_sum=math.inf, min_index=0):
    if end_index < len(numbers):
        current_sum = sum(numbers[start_index:end_index+1])

        if current_sum < min_sum:
            min_sum = current_sum # Т.е. вначале мин сумма была бесконечно большим числом, а теперь поменялась
            min_index = start_index

        start_index += 1
        end_index += 1

        print(f"Min sum: {min_sum} Current sum: {current_sum}")
        return min_sum_index(numbers, start_index, end_index, min_sum, min_index)
    return min_index

try:

    nums = [random.randint(-20, 20) for num in range(100)]
    print(nums)
    result = min_sum_index(nums, 0, 10)
    print(result)


except Exception as error:
    print(error)



