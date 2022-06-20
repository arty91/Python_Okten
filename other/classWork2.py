
'''
сделайте функцию на замыкания которая будет возвращать декоратор который будет
считать общее количество запущенных  функций декорированных этим декоратором
'''


# def decor():
#     count = 0
#
#     def count_check(function):
#         def increase_count():
#             nonlocal count
#             count += 1
#             print(f'Count: {count}')
#             function()
#         return increase_count
#
#     return count_check
#
#
# my_decor = decor()
#
#
# @my_decor
# def sample_func():
#     print('Function execution.')
#
#
# @my_decor
# def sample_func2():
#     print('Function execution - 2.')
#
#
# sample_func()
# sample_func()
# sample_func2()
# sample_func2()
# sample_func2()
# sample_func2()
