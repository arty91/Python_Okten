'''
прога, що виводить кількість кожного символа з введеної строки,
  наприклад:
  st = 'as 23 fdfdg544' #введена строка
'''

# def func_string_to_el(s: str):
#     s_unique = list(dict.fromkeys(s))
#     for i in s_unique:
#         print(f'"{i}" -> {s.count(i)}')
#
#
# print(func_string_to_el('as 23 fdfdg544'))

'''
вивести послідовність Фібоначі, кількість вказана в знінній,
  наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
  (число з послідовності - це сума попередніх двох чисел)
'''

# def fibo_func(n: int) -> str:
#     ls, el1, el2 = [], 0, 1
#     for _ in range(n):
#         sum = el1 + el2
#         ls.append(str(el2))
#         el1 = el2
#         el2 = sum
#     return ' '.join(ls)
#
#
# print(fibo_func(10))

'''
порахувати кількість парних і непарних цифр числа, 
  наприклад: х = 225688 -> п = 5, н = 1;
         х = 33294 -> п = 2, н = 3
'''

# def count_num(num: int):
#     odd = sum(x % 2 != 0 for x in [int(x) for x in str(num)])
#     even = len(str(num)) - odd
#     return f'odd - {odd}, even - {even}'
#
#
# print(count_num(33294))

'''
генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
задача сделать c него лист листов такого плана:

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
[1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
[1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
[1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]
'''


# def list_gen(n: int):
#     ls = [x for x in range(n) if x % 2 != 0]
#     new_ls = []
#     i, k, m = 0, 1, 1
#
#     while k < n:
#         if ls[i:k]:  # checking chunk is not empty, if it is - do not add to new_ls
#             new_ls.append(ls[i:k])
#         i = k
#         k = k + m + 1  # key factor to complete task, as k should be 1, 3, 6, 9....
#         m += 1
#     return new_ls
#
#
# print(list_gen(14))

'''
// Дан массив целых чисел, найдите тот, который встречается нечетное количество раз.
// Всегда будет только одно целое число, которое встречается нечетное количество раз
//     [1,2,3,4,5,2,4,1,3] -> 5
'''

# def count_ls(ls: list) -> int:
#     for i in ls:
#         if ls.count(i) % 2 != 0:
#             return i
#
#
# print(count_ls([1, 1, 2, 2, 9, 9, 8]))

'''
//     Перевірити чи слово має в собі такі самі літери як і поеперднє слово.
//
//     ANAGRAM | MGANRAA -> true
// EXIT | AXET -> false
// GOOD | DOGO -> true
'''

# def check_words(s: str) -> bool:
#     s = s.split(' | ')
#     a = ''.join(sorted(s[0][:]))
#     b = ''.join(sorted(s[1][:]))
#     return True if a == b else False
#
# print(check_words('EXIT | AXET'))


'''
// Точная степень двойки
// Дано натуральное число N.
//     Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
//     Операцией возведения в степень пользоваться нельзя!
'''

# def two_check(n: int) -> bool:
#     if (n != 0) and (n & (n-1) == 0):
#         return 'YES'
#     else:
#         return 'NO'
#
#
# print(two_check(16))

'''
//  Сумма цифр числа
// Дано натуральное число N. Вычислите сумму его цифр.
//     При решении этой задачи нельзя использовать строки,
//     списки, массивы ну и циклы, разумеется.
//     Рекурсія)
'''

# def calc_sum(num: int) -> int:
#     sum = 0
#
#     while (num != 0):
#         sum = sum + (num % 10)
#         num = num // 10
#     return sum
#
#
# print(calc_sum(12345))

# 2nd option
# def calc_sum(num: int) -> int:
#     return sum(int(digit) for digit in str(num))
# or sum(map(int, str(num)))
#
# print(calc_sum(12345))

'''
// Палиндром
// Дано слово, состоящее только из строчных латинских букв. Проверьте, является ли это слово палиндромом. Выведите YES или NO.
//     При решении этой задачи нельзя пользоваться циклами, в решениях на питоне нельзя использовать срезы с шагом, отличным от 1.
'''

# def check_palindrome(s: str):
#     return 'YES' if s == s[::-1] else 'NO'
#
#
# print(check_palindrome('anna'))

'''
// Количество единиц
// Дана последовательность натуральных чисел  в строке, завершающаяся двумя числами 0 подряд.
// Определите, сколько раз в этой последовательности встречается число 1. Числа, идущие после двух нулей, необходимо игнорировать.
//
// 2176491947586100 -> 3
'''

# def find_one(num: int) -> int:
#     return sum(1 for x in str(num).split('00')[0] if x == '1')
#
# print(find_one(2176491947586100))

'''
// Вирівняти багаторівневий масив в однорівневий
//     [1,3, ['Hello, 'Wordd', [9,6,1]], ['oops'], 9] -> [1, 3, 'Hello, 'Wordd', 9, 6, 1, 'oops', 9]
// flat використовувати заборонено.
'''

# def list_to_list(ls: list) -> list:
#     new_ls = []
#
#     for i in ls:
#         if type(i) is list:
#             for item in list_to_list(i):
#                 new_ls.append(item)
#         else:
#             new_ls.append(i)
#     return new_ls
#
#
# print(list_to_list([1, 3, ['Hello', 'Wordd', [9, 6, 1], [11, 22, 33, [11, 11, 11, [22, 22, 22, [33, 33, 33]]]]], ['oops'], 9, [11, 11, 22, 33]]))

'''
// Знайти набільший елемент в масиві за допомогою reduce
//     [1,6,9,0,17,88,4,7] -> 88
'''

# from functools import reduce
#
# ls = [1, 6, 9, 0, 17, 88, 4, 7]
# print(reduce(lambda x, y: x if x > y else y, ls))
