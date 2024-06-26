"""
Дано натуральное число N. Выведите все его цифры
 по одной, в обратном порядке, разделяя
их пробелами или новыми строками.
При решении этой задачи нельзя использовать строки,
списки, массивы (ну и циклы, разумеется).
Разрешена только рекурсия и целочисленная
арифметика.

# 1) декомпозиция задачи
# 2) обратный порядок цифр
# while True:
#     last_digit = int(input("write:>"))
#     print(number % 10)
# 3) каждая цифра на новой строке
# print(last_digits)
# 4) используем рекурсию, для перехода к следующей цифре
# reverse_digits(n // 10)
# 5)  если число однозначное то отрабатываам базовый случай
# if n<10
# print(n)
"""


def reverse_digits(number: int) -> int:
    """
    Рекурсивная функция, реверсивно выводящая цифры числа n.

    Args:
        n: Неотрицательное целое число.

    Returns:
            None. Функция выводит результат в виде побочного эффекта.
    """
    # базовый случай
    if number < 10:
        return number
    # находим последнюю цифру
    last_digits = number % 10
    # вывожу последнюю цифру

    print(last_digits, end=" ")
    # рекурсивно вызываем функцию, переходим к следующей цифре
    return reverse_digits(number // 10)


# эскейп последовательности \n перенос каретки на новую строку
# принимаем число
number_1: int = int(input("write:>"))
# вызов функции
# передача ключевых аргументов
print(reverse_digits(number=number_1))


#     if n == 0:
#         return 1
#     return n * reverse_digits(n - 1)

# print(reverse_digits(5))
# # x:int = int(input())
# number: int = 12345
