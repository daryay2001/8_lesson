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
def my_star(n) -> str:
    if n > 0:
        print("*", end="")
        my_star(n-1)
    else:
        return print()
try:
    number = int(input("Enter your number: "))
    my_star(number)
except Exception as error:
    print(error)


# Задание 3.
#
# Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a до b.
# Пользователь вводит a и b. Проиллюстрируйте работу функции примером.
#
#




########
# Дополнительно:
#
# Задание 4.
#
# Напишите рекурсивную функцию, которая принимает одномерный массив из 100 целых чисел
# заполненных случайным образом и находит позицию, с которой начинается последовательность из 10 чисел,
# сумма которых минимальна.