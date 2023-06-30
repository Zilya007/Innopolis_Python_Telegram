# Реализовать скрипт вычисляющий разность квадрата суммы и суммы квадратов.
# Использование циклов, для решения задачи
# Вариант решения без цикла - разность квадратов равна "2 * число в квадрате"

result = []
square_sum = []
sum_square = []
print("Программа выведет разность квадратов чисел от 1 до Вашего значения!")
while True:
    exit_flag = input('Для выхода из программы нажмите 0 , для продолжения нажмите Enter.\n')
    if exit_flag == '0':
        print("Завершение работы программы.")
        break
    else:
        scope = input("Введите число до 100:\n")
        if scope.isnumeric() and len(scope) <= 3 and int(scope) <= 100:
            user_number = int(scope) + 1

            for i in range(1, user_number):
                square_sum.append((i + i)**2)

            for i in range(1, user_number):
                sum_square.append(i**2 + i**2)

            for i in range(0, user_number - 1):
                result.append(square_sum[i] - sum_square[i])
                print('Разность квадрата суммы и суммы квадратов числа ', end='')
                print(i + 1, result[i], sep=' = ', end='.\n')
        else:
            print(f"Ошибка ввода, введите число до 100. Вы ввели {scope}\n")
