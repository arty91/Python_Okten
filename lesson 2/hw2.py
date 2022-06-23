'''
1)
написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
- первый записывает в эту переменную запись
- второй возвращает все записи

запишите 5 тудушек
и выведете все
'''

# def notebook():
#     todo_list: list = []
#
#     def add_todo(new_task: str) -> None:
#         nonlocal todo_list
#         todo_list.append(new_task)
#
#     def get_all() -> list[str]:
#         return todo_list
#
#     return get_all, add_todo
#
# #function de-structurization:
#
# get_all, add_todo = notebook()
#
# add_todo('do laundry')
# add_todo('play piano')
# add_todo('watch Olympic Games')
# add_todo('solve kata on Codewars')
# add_todo('go sleep')
# print(get_all())


'''
3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)

Пример:

expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'
'''

# def ret_numbers(num: int) -> str:
#     ls = []
#     count = len(str(num))-1
#     for i in str(num):
#         if i == '0':
#             count -= 1
#             continue
#         else:
#             ls.append(f'{i}{"0" * count}')
#             count -= 1
#     return ' + '.join(ls)
#
# print(ret_numbers(70304))

# создать декоратор который будет считать сколько раз была запущена функция и будет выводит это
# значение после каждого запуска функции

# def count_check(function, count=None):
#
#     if count is None:
#         count = [1]
#
#     def increase_count():
#         print(f'Count: {count[0]}')
#         count[0] += 1
#         return function(), count[0]
#
#     return increase_count
#
#
# @count_check
# def sample_func():
#     print('Function execution.')
#
# @count_check
# def sample_func2():
#     print('Function execution - 2.')
#
#
# sample_func2()
# sample_func2()
# sample_func()
# sample_func()
# sample_func()
# sample_func2()
