
# создать декоратор который будет считать сколько раз была запущена функция и будет выводит это
# значение после каждого запуска функции

def count_check(function, count=[1]):

    def increase_count(*args, **kwargs):
        print(f'decorator called {count[0]}')
        count[0] += 1
        return function(*args, **kwargs), count[0]

    return increase_count


@count_check
def sample_func():
    print('Function execution.')


sample_func()
sample_func()
sample_func()
sample_func()
sample_func()
sample_func()
sample_func()
