'''5. Создай мини-проект, имитирующий систему уведомлений от разных источников
(Email, SMS, Push-уведомления). Базовый класс определяет общий интерфейс,
а дочерние классы реализуют конкретные виды уведомлений.'''

class Notification:
    def send(self, message: str):
        print(f'Отправка уведомления: {message}')
    def log(self, message: str):
        print(f'ЛОГ: Уведомление успешно отправлено через {message}')

class EmailNotification(Notification):
    def send(self, message):
        print(f'Отправка Email: {message}')
        super().log('Email')

class SMSNotification(Notification):
    def send(self, message):
        print(f'Отправка SMS: {message}')
        super().log('SMS')

class PushNotification(Notification):
    def send(self, message):
        print(f'Отправка Push: {message}')
        super().log('Push')

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notifier in notifications:
    notifier.send("Система перезапущена")
