"""Write task2."""

# Задание 2.
# Для заданного четырехзначного числа найти разницу
# между наибольшей и наименьшей
# цифрой. Ограничений по использованию циклов и массивов нет.
# Файл с заданием: task_2.1.py
# """


# #  iterable - это объект который можно еребрать поэлементно с помощью цикла
# # принять число
# # найти наибольшее и наименьшее
# # cравнить
# итерация это один проход в цикле
# if условная констуркция и проверяет условия , не делает итерации
def find_difference(num: int) -> int:
    """функция считает разницу между числами"""
    # подсчёт разницы
    # sub_num = int(max(f"{num}")) - int(min(f"{num}"))
    for number in str(num):
        max_number: str = str(num)
        if int(max_number) < int(number):
            max_number = number
    return int(max_number)


print(find_difference(num=12345))


# input_value = int(input(":>"))

# print(find_difference(num=input_value))


# list_num = [1,2,3]

# for number in list_num:
#     max_number = list_num[0]
#     if max_number < number:
#         max_number = number
#     min_number = list_num[0]
#     if min_number > number:
#         min_number = number
