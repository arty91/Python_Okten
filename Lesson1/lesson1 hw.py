'''
1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад:
st = 'as 23 fdfdg544' введена строка
2,3,5,4,4        #вивело в консолі.
'''

# def func1(string):
#     return ','.join(str(el) for el in string if el.isnumeric())
#
# print(func1('as 23 fdfdg544'))


'''
2)написати прогу яка вибирає зі введеної строки числа і виводить їх 
так як вони написані
наприклад:
  st = 'as 23 fdfdg544 34' #введена строка
  23, 544, 34              #вивело в консолі
'''

# import re
# def func2(string):
#     return list(map(int, re.findall(r'\d+', string)))
#
#
# print(func2('as 23 fdfdg544 34'))

#without import:
# def func2(string):
#     return ','.join(str(el) for el in [int(i) for i in ''.join((x if x in '0123456789' else ' ') for x in string).split()])
#
# print(func2('as 23 fdfdg544 34'))


'''
list comprehension

1)есть строка:
greeting = 'Hello, world'
записать каждый символ в лист поменяв его на верхний регистр
пример:
['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
'''

# def func3(string):
#     return [i.upper() for i in string]
#
#
# print(func3('Hello, world'))

'''
2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
пример:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
'''

# print([i ** 2 for i in range(50) if i % 2 == 1])

# function

# - створити функцію яка виводить ліст - геніальна функція

# def l_print(ls):
#     print(ls)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.

# def ret_min(a, b, c):
#     return min(a, b, c)
#
#
# print(ret_min(2, 10, 4))

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def ret_min(a, b,  4))c):
# #     return max(a, b, c)
# #
# #
# # print(ret_min(2, 10,

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def func5 (*args):
#     print(max(*args))
#     return min(*args)
#
#
# print(func5(5, 33, 55, 10, 23, 98, 111))

# - створити функцію яка виводить ліст - геніальна настільки, щоби її 2 рази записувати

# - створити функцію яка повертає найбільше число з ліста

# def func6(ls):
#     return min(ls)
#
#
# print(func6([11, 22, 33, 5, 88, 99, 13, 15]))

# - створити функцію яка повертає найменьше число з ліста
# def func6(ls):
#     return max(ls)
#
#
# print(func6([11, 22, 33, 5, 88, 99, 13, 15]))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def func7(ls):
#     return sum(ls)
#
#
# print(func7([11, 22, 33, 44, 55]))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def func7(ls):
#     return sum(ls)/len(ls)
#
#
# print(func7([11, 22, 33, 44, 55]))

########################################################################################

'''
1)Дан лист:
  list = [22, 3,5,2,8,2,-23, 8,23,5]
  - найти min число в листе
  - удалить все дубликаты в листе
  - заменить каждое четвертое значение на "Х" 
'''

# list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
#
# def func8(ls):
#     print(min(ls))  #  - найти min число в листе
#     ls = list(dict.fromkeys(ls))  #   - удалить все дубликаты в листе
#     print(ls)
#     for idx, el in enumerate(ls):  #   - заменить каждое четвертое значение на "Х"
#         if idx % 4 == 0:
#             ls[idx] = 'X'
#     return ls
#
#
# print(func8(list1))

'''
2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой
'''

# def func_sq(num):
#     print('* ' * num)
#     for _ in range(num - 2):
#         print('* ' + '  ' * (num - 2) + '*')
#     print('* ' * num)
#
# func_sq(17)

'''
3) вывести табличку умножения с помощью цикла while
'''
# j = 1
# while j < 10:
#     i = 1
#     while i < 10:
#         print(j*i, end='\t')
#         i += 1
#     j += 1
#     print("\n")



'''
***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
пример:
[1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
[-1, -2, 3, 4, 555] => 4
[5, 5, 5, 5] => 5
[-10, 5, 5] => 5
'''

# def func_av(ls):
#     avg = int(sum(ls)/len(ls))
#     return min(ls, key=lambda x: abs(avg - x))
#
# print(func_av([1, 2, 3, 4, 5, 6, 7, 8, 9]))
