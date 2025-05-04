'''8. Создать собственный дескриптор, который проверяет,
чтобы имя пользователя соответствовало заданным условиям.
'''

class ValidatedString:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value: str):
        if not value:
            raise ValueError("Имя не может быть пустым")
        elif not value.isalpha():
            raise ValueError("Имя должно содержать только буквы")
        elif not value[0].isupper():
            raise ValueError("Имя должно начинаться с заглавной буквы")
        instance.__dict__[self.private_name] = value

class User:
    name = ValidatedString()

    def __init__(self, name):
        self.name = name

u = User("Азамат")
print(u.name)

u.name = "марат"
u.name = "123Мир"
u.name = ""
