# Задание 3
#
# Напишите функцию, определяющую количество простых чисел в списке целых.
# Список передаётся в качестве параметра. Полученный результат возвращается из функции.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def is_simple(number: int) -> bool:
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 return False
#         return True
#
#     return False
#
#
# # print(is_simple(7))
# # print(is_simple(8))
#
#
# def show_simple_numbers(numbers) -> None:
#     for number in numbers:
#         if is_simple(number):
#             print(number)
#
#
# show_simple_numbers(numbers=nums)

###
# def hello(): print("Hello")
#
#
# print(hello)
# message = hello
# print(message)
# message()
# hello()

######
# def add(a, b): return a + b
# def sub(a, b): return a - b
# def mult(a, b): return a * b
# def division(a, b): return a / b
#
#
# def select_math_operation(user_choice):
#     match user_choice:
#         case "+":
#             return add
#         case "-":
#             return sub
#         case "*":
#             return mult
#         case "/":
#             return division
#         case _:
#             raise Exception("Invalid math operation!")
#
#
# try:
#     operation = input("Enter math operation: ")
#     math_operation = select_math_operation(operation)
#     result = math_operation(3, 5)
#     print(f"Result: {result}")
# except Exception as e:
#     print(f"Error: {e}")


############
# message = lambda: print("Hello")
# message()
# #
# square = lambda side_1, side_2: side_1 * side_2
# print(square(2, 3))

#
# def calculate(a, b, math_function) -> None:
#     print(f"Result: {math_function(a, b)}")
#
#
# calculate(2, 4, lambda n1, n2: n1 + n2)
# calculate(2, 4, lambda n1, n2: n1 - n2)

#

# def select_math_operation(user_choice):
#     match user_choice:
#         case "+":
#             return lambda a, b: a + b
#         case "-":
#             return lambda a, b: a - b
#         case "*":
#             return lambda a, b: a * b
#         case "/":
#             return lambda a, b: a / b
#         case _:
#             raise Exception("Invalid math operation!")
#
#
# operation = input("Enter math operation: ")
# math_operation = select_math_operation(operation)
# result = math_operation(3, 5)
# print(f"Result: {result}")

#####
# области видимости
# number = 10
#
#
# def test() -> None:
#     number: int = 11  # перекрытие глобальной переменной
#
#     if 1:
#         number = 12
#
#         if 1:
#             #number = 13
#             print(number)
#     print(number)
#
#
# print(number)
# test()
# print(number)
# number = 35
# print(number)

############
# LEGB - почитать
# number = 10
#
#
# def test():
#     global number
#     number = 11  # изменяем значение глобальной переменной
#     print(number)
#
#
# print(number)
# test()
# print(number)

####
# def outer():
#     number = 1
#
#     def inner():
#         nonlocal number
#         number = 2
#         print(number)
#
#     inner()
#     print(number)
#
#
# outer()

###
# number = 10
#
#
# def outer():
#     global number
#     number = 1
#     new_number = number
#
#     def inner():
#         global number
#         nonlocal new_number
#         new_number = 2
#         print(new_number)
#         number = 2
#
#         # def inner_number_2():
#         #     global number
#         #     nonlocal new_number
#         #     new_number = 3
#         #     print(new_number)
#         #     number = 3
#         #
#         # inner_number_2()
#
#     inner()
#     print(new_number)
#
#
# outer()
# print(number)

##############
#
# Замыкание (closure) представляет функцию, которая запоминает свое лексическое окружение даже в том случае,
# когда она выполняется вне своей области видимости.

# внешняя функция, которая определяет некоторую область видимости и в которой определены некоторые
# переменные и параметры - лексическое окружение
#
# переменные и параметры (лексическое окружение), которые определены во внешней функции
#
# вложенная функция, которая использует переменные и параметры внешней функции

# def outer():
#     number = 10
#     print("outer")
#     test = 10
#     test_2 = 111
#
#     def inner():
#         nonlocal number
#         number += 1
#         # print(test)
#         print(number)
#         # print("hello")
#
#     return inner
#
#
# inner_func = outer()
# inner_func()
# inner_func()
# inner_func()


# v1
# def multiply(num1):
#     def inner(num2): return num1 * num2
#     return inner

# v2
# def multiply(num1): return lambda num2: num1 * num2


# def multiply_v2(num1, num2):
#     return num1 * num2
#
#
# for i in range(1, 10):
#     print(f"{3} * {i} = {multiply_v2(3, i)}")


# number1 = 3
# mult_func = multiply(number1)
# # print(mult_func(4))
# # print(mult_func(5))
# # print(mult_func(7))
#
# for number2 in range(1, 10):
#     print(f"{number1} * {number2} = {mult_func(number2)}")

############
#
# Рекурсия - когда функция вызывает сама себя
# 1. определить условие или условия выхода из рекурсии
# 2. запустить рекурсию (вызов этой же функции)
# 3. продумать какое или какие параметры функции будут изменены при рекурсивном вызове

# 5! => 1 * 2 * ... * 5
# def factorial(number):
#     if number <= 1:
#         return 1
#
#     # factorial(number - 1) -> запуск рекурсии
#     return number * factorial(number - 1)
#
#
# print(factorial(5))
# #
# #
# # factorial(5) -> 5 * factorial(4) => 120
# # factorial(4) -> 4 * factorial(3) => 24
# # factorial(3) -> 3 * factorial(2) => 6
# # factorial(2) -> 2 * factorial(1) => 2
# # factorial(1) => 1

#########
# дополнительно: расписать вызовы: fib(2) и fib(3)
# def fib(number):
#     if number == 0 or number == 1:
#         return number
#
#     return fib(number - 2) + fib(number - 1)
#
#
# # print(fib(10))
#
# for i in range(1, 10):
#     print(fib(i), end=' ')
