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

    def answer(self):
        print("Ответить Да / Нет")
        choice = input()
        if choice == 'Да':
            print(f"Вы ответили на звонок")
        else:
            pass


class IpPhone(Phone):

    def __init__(self, maker, model, poe=None):
        super().__init__(maker, model)
        self.poe = poe
        self.history = []

    def call(self):
        number = input("Наберите номер телефона! ")
        print(f'call to {number}')
        self.history.append(number)

    def answer(self):
        self.number = random.randint(9111111111, 9999999999)
        print("Ответить Да / Нет")
        choice = input()
        if choice == 'Да':
            print(f"Вы ответили на звонок {self.number}")
            self.history.append(self.number)
        else:
            pass

    def show_history(self):
        print("история звонков: ")
        for number in self.history:
            if self.history.index(number) == (int(len(self.history)) - 1):
                print(number, end='.\n')
            else:
                print(number, end=', ')

    def activate_poe(self):
        if self.poe is not None:
            print('Активирована фнкция POE')
        else:
            print("Данная функция не доступна")


class ConferencePhone(IpPhone):
    conference_number = 0

    def _create_conference(self):
        while True:
            members = input("Введите количество участников: ")
            if members.isnumeric() and int(members) <= 10:
                print(f"Создана конференция с количеством участников -  {members}.")
                self.conference_number += 1
                break
            else:
                print('Введите корректное значение')

    def _show_conference_number(self):
        print(f'Количество проведенных конференций - {self.conference_number}')


phone1 = Phone('Panasonic', 'XR24T')
ip_phone1 = IpPhone('Yealink', 'T21P')
conference_phone1 = ConferencePhone('Yealink', 'T54W', 'poe')

while True:
    choice_phone = input(
        "Выберите телефон: 1 - аналоговый , 2 - ip-телефон, 3- конференц-телефон, 0 - выход из программы\n")
    match choice_phone:
        case '1':
            print(f"Вы используете телефон {phone1.maker} {phone1.model}")
        case '2':
            print(f"Вы используете телефон {ip_phone1.maker} {ip_phone1.model}")
            while True:
                print(
                    "Выберите действие: 1 - Позвонить , 2 Ответить на звонок , 3 - Показать историю звонков ,"
                    "4 - активировать режим POE, 0 - выход")
                choice = input()
                match choice:
                    case '1':
                        ip_phone1.call()
                    case '2':
                        ip_phone1.answer()
                    case '3':
                        ip_phone1.show_history()
                    case '4':
                        ip_phone1.activate_poe()
                    case '0':
                        break
                    case _:
                        print("Ошибка ввода повторите")
        case '3':
            print(f"Вы используете телефон {conference_phone1.maker} {conference_phone1.model}")
            while True:
                print(
                    "Выберите действие: 1 - Позвонить , 2 Ответить на звонок , 3 - Показать историю звонков , "
                    "4- создать конференцию, 5- показать количество конференций, 6 - активировать режим POE, 0 - выход")
                choice = input()
                match choice:
                    case '1':
                        conference_phone1.call()
                    case '2':
                        conference_phone1.answer()
                    case '3':
                        conference_phone1.show_history()
                    case '4':
                        conference_phone1._create_conference()
                    case '5':
                        conference_phone1._show_conference_number()
                    case '6':
                        conference_phone1.activate_poe()
                    case '0':
                        break
                    case _:
                        print("Ошибка ввода повторите")

        case '0':
            break

        case _:
            print("Ошибка ввода")
