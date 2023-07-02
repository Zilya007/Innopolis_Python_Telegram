#Реализовать приложение для проверки верности введенных пользователем данных в виде строки
word = 'Реализовать приложение для проверки верности введенных пользователем данных в виде строки'
# print(word.split())
# print(word.count('а'))
fio = []
while True:
    user_name = input("Введите ФИО через пробел: ").title()
    fio = user_name.split()
    if len(fio) == 3:
        for item in fio:
            print(item,sep=' ')

        number = input("Введите номер телефона без восьмерки! ").strip()
        if number.isdigit() and len(number) == 10:
            phone = number.strip()
        else:
            print(f'Ошибка ввода, Вы ввели {number}')

        print(f'Поздравляем {fio[1]}, Вы успешно зарегистрированы.')
        print(сделать с форматом рег данные)

    else:
        print(f"Ошибка ввода, Вы ввели {user_name}")


#Фатыхов Рамиль Ильдусович 9196316800




# print(user_name.split())
