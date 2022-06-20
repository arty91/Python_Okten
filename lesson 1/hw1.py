# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# def digit_find(s: str):
# 	return ','.join(str(el) for el in s if el.isnumeric())
#
# print(digit_find('as 23 fdfdg544'))

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# def number_find(s: str):
# 	return ','.join(str(el) for el in [int(i) for i in ''.join(x if x in '0123456789' else ' ' for x in s).split()])
#
#
# print(number_find('as 23 fdfdg544 34'))

# for myself other option:
# import re
# def func2(string):
#     return list(map(int, re.findall(r'\d+', string)))
#
#
# print(func2('as 23 fdfdg544 34'))

# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# def string_to_upper(s: str):
# 	return [i.upper() for i in s]
#
#
# print(string_to_upper('Hello, world'))

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([el ** 2 for el in range(50) if el % 2 == 1])

# function
#
# - створити функцію яка виводить ліст

# def l_print(ls):
#     print(ls)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.

# def ret_min(a, b, c):
#     return min(a, b, c)
#
#
# print(ret_min(2, 10, 4))

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def ret_min(a, b, c):
#     return max(a, b, c)
#
#
# print(ret_min(2, 10, 6))

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def func5 (*args):
#     print(max(*args))
#     return min(*args)
#
#
# print(func5(5, 33, 55, 10, 23, 98, 11))

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
#
# #################################################################################################

# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - найти min число в листе
#   - удалить все дубликаты в листе
#   - заменить каждое четвертое значение на "Х"
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


# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой


# def func_sq(num):
#     print('* ' * num)
#     for _ in range(num - 2):
#         print('* ' + '  ' * (num - 2) + '*')
#     print('* ' * num)
#
# func_sq(17)


# 3) вывести табличку умножения с помощью цикла while

# j = 1
# while j < 10:
#     i = 1
#     while i < 10:
#         print(j*i, end='\t')
#         i += 1
#     j += 1
#     print("\n")

# 4) переделать первое задание под меню с помощью цикла
# from functools import reduce
#
# ls = [2, 3, 4, 5, 6, 7, 11, 22, 44, 55, 66, 77, 88, 2, 11, 66, 7]
# ls_dif = []
# print(ls)
#
# menu_options = {
# 	1: 'Find min value',
# 	2: 'Remove duplicates',
# 	3: 'Replace every 4th el to X',
# 	4: 'Show el which is the closest to middle value',
# 	5: 'Exit menu',
# }
#
#
# def print_menu():
# 	for key in menu_options.keys():
# 		print(key, '--', menu_options[key])
#
#
# def option1():
# 	ls_min = min(ls)
# 	print(f'min value is  {ls_min}')
# 	pass
#
#
# def option2():
# 	ls_unique = list(dict.fromkeys(ls))
# 	print(ls_unique)
# 	pass
#
#
# def option3():
# 	for i, y in enumerate(ls):
# 		if i % 4 == 0:
# 			ls[i] = 'X'
# 	return ls
# 	pass
#
#
# def option4():
# 	m = reduce(lambda x, y: x + y, ls) / len(ls)
# 	for i in ls:
# 		ls_dif.append(m - i)
# 	for y, i in enumerate(ls_dif):
# 		if i < 0:
# 			ls_dif[y] = i * (-1)
# 	print(ls[ls_dif.index(min(ls_dif))])
# 	pass
#
#
# while True:
# 	print_menu()
# 	print('--------------------------------------------')
# 	option = int(input('Your choice: '))
#
# 	if option == 1:
# 		option1()
# 	elif option == 2:
# 		option2()
# 	elif option == 3:
# 		option3()
# 		print(ls)
# 	elif option == 4:
# 		option4()
# 	elif option == 5:
# 		print('Program has finished. Goodbye!')
# 		exit()
# 	else:
# 		print('--------------------------------------------')
# 		print('Please select your option from 1 to 5.')
# 		print('--------------------------------------------')
