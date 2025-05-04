'''7. Создай иерархию классов, реализующую полиморфизм: у всех классов
будет один общий метод pay(amount),
но реализация будет разной в зависимости от способа оплаты.
'''

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f'Оплата картой на сумму {amount}₽')

class PayPalPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f'Оплата через PayPal на сумму {amount}₽')

class CryptoPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f'Оплата криптовалютой на сумму {amount}₽')


payments = [
    CreditCardPayment(),
    PayPalPayment(),
    CryptoPayment()
]

for method in payments:
    method.pay(1500)
