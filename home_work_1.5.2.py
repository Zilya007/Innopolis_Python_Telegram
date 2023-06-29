# Изначально считаем что разность квадрата суммы и суммы квадратов
# вычисляется по формуле "2 умноженное на число в квадрате "

print("Вывод разности квадрата суммы и суммы квадратов числа из выбранного диапазона.")
result = []

start_number = input("Введите начальное число для диапазона: ")
if start_number.isnumeric() and int(start_number) > 0:
    last_number = input("Введите конечное число: ")
    if last_number.isnumeric() and int(last_number) > 0 and int(last_number) > int(start_number):
        print(f"Будет выведен результат по диапазону от {start_number} до {last_number} ")

        for i in range(int(start_number), int(last_number) + 1):
            result.append(2 * i * i)
    else:
        print(f'Ошибка ввода, вы ввели {last_number}')
    user_range = range(int(start_number), int(last_number) + 1)
    print(user_range)
    for i in range(0, len(user_range)):
        print(f'{user_range[i]} = {result[i]}  ')
else:
    print(f'Ошибка ввода, вы ввели {start_number}')

# for i in range(0,int(user_number -1)):
#     print(i)
#
#     # print(f"Разность числа {i + 1} = {result[i]}")
