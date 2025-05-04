'''Условие задачи:
1. Свойства (@property)
Проект: Класс Temperature с хранением температуры в цельсиях и
автоматическим пересчётом в фаренгейты и обратно.'''

class Temperature:
    def __init__(self):
        self.__celsius = 0.0
    @property
    def celsius(self):
        return self.__celsius
    @celsius.setter
    def celsius(self, new):
        if new < -273.15:
            raise ValueError('Неверная температура')
        self.__celsius = new

    @property
    def fahrenheit(self):
        return self.__celsius * 1.8 + 32
    @fahrenheit.setter
    def fahrenheit(self, new):
        if new < -459.67:
            raise ValueError('Неверная температура')
        self.__celsius = float(int(5/9*(self.__celsius - 32)))


temp = Temperature()

print(temp.celsius)
print(temp.fahrenheit)

temp.celsius = 100
print(temp.fahrenheit)

temp.fahrenheit = 98.6
print(temp.celsius)