'''3. Декораторы
Проект: Декоратор @log_time, который логирует время выполнения функции.'''

from time import time, sleep

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        stop = time()
        result = stop - start
        print(f"Вывод: Функция {func.__name__} выполнена за {round(result, 2)}")
    return wrapper

@log_time
def heavy_operation():
    sleep(7.8)
heavy_operation()
