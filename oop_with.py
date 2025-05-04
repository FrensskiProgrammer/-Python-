'''2. Оператор with и менеджеры контекста
Проект: Класс FileLocker, который создаёт лог-файл и
автоматически записывает время входа и выхода из блока'''

from datetime import datetime
from time import sleep

class FileLocker:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        time = datetime.now()
        time = time.strftime('%Y-%m-%d %H:%M:%S')
        file = open(self.filename, 'a', encoding='UTF-8')
        file.write(f'[{time}] Вход\n')
        file.close()
        sleep(5)
    def __exit__(self, exc_type, exc_val, exc_tb):
        time = datetime.now()
        time = time.strftime('%Y-%m-%d %H:%M:%S')
        file = open(self.filename, 'a', encoding='UTF-8')
        file.write(f'[{time}] Выход\n')
        file.close()

with FileLocker('session.log'):
    print("Это контекстный менеджер!")