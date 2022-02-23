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

'''
сделайте функцию на замыкания которая будет возвращать декоратор который будет
считать общее количество запущенных  функций декорированных этим декоратором
'''


def decor():
    count = 0

    def count_check(function):
        def increase_count():
            nonlocal count
            count += 1
            print(f'Count: {count}')
            function()
        return increase_count

    return count_check


my_decor = decor()


@my_decor
def sample_func():
    print('Function execution.')


@my_decor
def sample_func2():
    print('Function execution - 2.')


sample_func()
sample_func()
sample_func2()
sample_func2()
sample_func2()
sample_func2()
