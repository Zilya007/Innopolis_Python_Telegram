# Реализация работы с классами, наследованием и перегрузкой методами
# Корректно реализован класс, использующий псевдо частные методы и реализующий перегрузку методов

import random
class Phone:
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model

    def call(self):
        number = input("Наберите номер телефона! ")
        print(f'call to {number}')

    def answer(self, number):
        self.number = random.randint(8917000000,89174444444)
        print("Ответить Да / Нет")
        choice = input()
        if choice == 'Да':
            print(f"Вы ответили на звонок {self.number}")
        else:
            pass


class IpPhone(Phone):

    def __init__(self, maker, model, poe):
        self.maker= maker
        self.model = model
        self.poe = poe
        # super().__init__(maker)
        # super().__init__(model)
        self.history = []

    def call(self):
        number = input("Наберите номер телефона! ")
        print(f'call to {number}')
        self.history.append(number)

    def show_history(self):
        print("история звонков: ")
        for number in self.history:
            print(number)


class ConferencePhone(IpPhone):
    pass




phone1 = Phone('panasonic', 't20')
print(phone1.maker)
print(phone1.model)
ip_phone1 = IpPhone('Yealink', 'T21P', 'POE')

while True:

    ip_phone1.call()
    ip_phone1.show_history()
    ip_phone1.answer(89174444444)

