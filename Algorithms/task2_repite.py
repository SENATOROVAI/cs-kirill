"""
Дано натуральное число N. Выведите все его цифры по одной, в обратном порядке, разделяя
их пробелами или новыми строками. При решении этой задачи нельзя использовать строки,
списки, массивы (ну и циклы, разумеется). Разрешена только рекурсия и целочисленная
арифметика.
"""
# 1) принимаю N в input()
# 2) N вывожу каждую цифру отдельно на каждой строке
1) найдем последнее число
print(n % 10)
2)
3) рекурсия n//10


def digits_reverse(n: int) -> int:
    """функция возвращает число в обратном порядке"""
    if n < 10:
        print(n)
    # elif - иначе если
    # elif n > 2 and n < 10:
    #     print("hi")
    else:
        last_digits= n % 10
        print(last_digits)
        # напиши везде комменты
        # убираем у числа последнюю цифру и вызываем функцию
        return digits_reverse(n//10)
