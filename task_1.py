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


import random

# V1

# def min_sum_ind(my_array, start = 0):
#     if start + 10 > len(my_array):
#         return start
#     min_sum = sum(my_array[start: start+10]) # Нашла в интернете, что так можно писать для удобства
#     min_position = start
#
#     for i in range(start + 1, len(my_array) - 9): # Чтобы не выйти за пределы массива
#         actual_sum = sum(my_array[i: i+10])
#         if actual_sum < min_sum:
#             min_sum = actual_sum
#             min_position = i
#     return min_sum_ind(my_array, start + 1)

# Пишет, что превышена глубина рекурсии

# V2
def min_sum_index(my_array, start_pos=0):
    if start_pos + 10 > len(my_array):
        return start_pos

    sums = []
    for i in range(start_pos, len(my_array) - 9):
        actual_sum = sum(my_array[i: i+10])
        sums.append(actual_sum) # Записываю последовательно суммы в массив 2

    min_sum_index = sums.index(min(sums)) # Вывожу минимальную сумму по индексу

    return min_sum_index(my_array, start_pos + min_sum_index)
#     Нужно ли тут написать return min_sum_index(my_array, start_pos + 1) ?

try:

    NUMS_SIZE = 100
    nums = []
    FIRST = -20
    LAST = 20

    for i in range(NUMS_SIZE):
        nums.append(random.randint(FIRST, LAST))
    # print(min_sum_ind(nums))
    print(min_sum_index(nums))
    print(nums[3])


except Exception as error:
    print(error)



#  Для функции min_sum_index получаю 'int' object is not callable