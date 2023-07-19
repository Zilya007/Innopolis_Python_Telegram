from module_simple_numbers import simple_numbers

while True:
    choice = input("Программа вычисляет простые числа из выбранного диапазона!\n"
                   "Для продолжения наберите любой символ / Выход - 0\n")
    if choice != '0':
        start = input("Введите начальное значения диапазона:\n")
        final = input("Введите конечное значения диапазона:\n")
        if start.isnumeric() and final.isnumeric() and int(start) < int(final):
            simple_numbers(int(start), int(final))
        else:
            print("Ошибка ввода")
    else:
        print('Завершение работы!')
        break
