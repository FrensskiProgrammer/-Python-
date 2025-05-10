'''4. Магические методы (__getitem__, __setitem__, __delitem__, __getattr__,
__getattribute__, __setattr__, __delattr__)
Проект: Класс CustomDict, который работает как словарь,
но при доступе или удалении ключей печатает предупреждение.
Также блокирует прямой доступ к определённым ключам.'''

class CustomDict:
    def __init__(self):
        self.dicts = {}
    def __getitem__(self, item):
        value = self.dicts[item]
        print(f'[GET] ключ: {item} → значение: {value}')
    def __setitem__(self, key, value):
        if key != 'secret':
            print(f'[SET] ключ: {key} = {value}')
            self.dicts[key] = value
        else:
            raise PermissionError("Доступ к 'secret' запрещён")
    def __delitem__(self, key):
        print(f'[DEL] ключ: {key}')
        del self.dicts[key]
    def __getattr__(self, item):
        print(f"Атрибут '{item}' не найден")

    def __getattribute__(self, item):
        if item not in {'__dict__', '__class__', 'dicts'}:
            print(f"[ATTR ACCESS] {item}")
        return super().__getattribute__(item)
    def __setattr__(self, key, value):
        if key != 'dangerous_attr':
            print(f"[ATTR SET] {key} = {value}")
            self.__dict__[key] = value
        else:
            raise AttributeError("Нельзя устанавливать dangerous_attr")

    def __delattr__(self, item):
        if item == 'dangerous_attr':
            raise AttributeError("Нельзя удалить dangerous_attr")
        else:
            print(f'[ATTR DEL] {item}')
            super().__delattr__(item)

d = CustomDict()
d['a'] = 42
print(d['a'])
del d['a']

d.name = "Azamat"
print(d.name)
print(d.unknown)

d.dangerous_attr = 123
del d.dangerous_attr

