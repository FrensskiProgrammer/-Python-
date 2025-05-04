'''6. Проект: Класс BankAccount с приватным балансом и методами deposit,
withdraw, get_balance.
Нельзя напрямую обращаться к __balance, только через методы. Добавить валидацию.'''

class BankAccount:
    def __init__(self):
        self.__balance = 0.0
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print('Ошибка: сумма должна быть положительной')
        else:
            self.__balance += amount
            print(f'Пополнение: +{amount}')
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print('Ошибка: сумма должна быть положительной')
        elif amount > self.__balance:
            print('Ошибка: недостаточно средств')
        else:
            self.__balance -= amount
            print(f'Снятие: -{amount}')
    def get_balance(self) -> float:
        print(f'Текущий баланс: {self.__balance}')
        return self.__balance

acc = BankAccount()
acc.deposit(100)          # Пополнение: +100
acc.withdraw(50)          # Снятие: -50
acc.withdraw(100)         # Ошибка: недостаточно средств
acc.deposit(-20)          # Ошибка: сумма должна быть положительной
acc.get_balance()         # Текущий баланс: 50.0
print(acc.__balance)      # AttributeError — доступ запрещён
