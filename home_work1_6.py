#Реализовать приложение для проверки верности введенных пользователем данных в виде строки

fio = []
while True:
    user_name = input("Введите ФИО через пробел:\n").title()
    fio = user_name.split()
    if len(fio) == 3:
        number = input("Введите номер телефона без восьмерки:\n").strip()
        if number.isdigit() and len(number) == 10:
            phone = number.strip()
            print(f'Поздравляем {fio[1]}, Вы успешно зарегистрированы!')
            print("Ваши регистрационные данные:\n Фамилия: {}\n Имя: {}\n "
                  "Отчество: {}\n Номер телефона: {}".format(fio[0], fio[1], fio[2], phone))
            break
        else:
            print(f'Ошибка ввода, Вы ввели {number}')
    else:
        print(f"Ошибка ввода, Вы ввели {user_name}")
