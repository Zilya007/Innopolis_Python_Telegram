# Реализовать скрипт вычисляющий разность квадрата суммы и суммы квадратов.
# Использование циклов, для решения задачи
# Изначально считаем что разность квадрата суммы и суммы квадратов
# вычисляется по cледующей формуле: "2 умноженное на число в квадрате "

print("Программа выводит разность квадрата суммы и суммы квадратов числа из выбранного диапазона.")
result = []
while True:
    exit_flag = input('Для выхода из программы нажмите 0 , для продолжения нажмите Enter.\n')
    if exit_flag == '0':
        print("Завершение работы программы.")
        break
    else:
        start_number = input("Введите начальное число для диапазона: ")
        if start_number.isnumeric() and int(start_number) > 0:
            last_number = input("Введите конечное число: ")
            if last_number.isnumeric() and int(last_number) > 0 and int(last_number) > int(start_number):
                print(f"Будет выведен результат по диапазону от {start_number} до {last_number}.")

                for i in range(int(start_number), int(last_number) + 1):
                    result.append(2 * i * i)
            else:
                print(f'Ошибка ввода, для начала диапазона Вы ввели {start_number} для конечного значения {last_number}.')
            user_range = range(int(start_number), int(last_number) + 1)

            for i in range(0, len(user_range)):
                print(f'Разность квадратов числа {user_range[i]} = {result[i]}.')
        else:
            print(f'Ошибка ввода, для начального значения Вы ввели {start_number}.')


