# Реализовать программу выводящую необходимый результат, в зависимости от выбора пользователя
# Планируемый результат: приложение, которое корректно обрабатывает ввод данных от пользователя.


print("Программа нарисует елочку из выбранного символа!")

flag_input = True  # Логическая переменная для проверки успешности блока ввода пользователя
while flag_input:
    symbol = input("Введите любой один символ, кроме пробела:\n")
    if len(symbol) == 1 and symbol != ' ':
        level = input("Введите высоту до 30:\n")
        if level.isnumeric() and int(level) <= 30:
            level = int(level)
            flag_input = False
        else:
            print("Ошибка Ввода")
            flag_input = True
    else:
        print("Ошибка ввода!")
        flag_input = True

split = level - 1   # Переменная для расчета длины отступа
count = 1
for i in range(0, level):
    print(split * ' ', end='')  # Вывод отступа в зависимости от каждого уровня рисунка
    split -= 1
    print(count * symbol, end='')   # Вывод символа на каждый уровень
    count += 2
    print()
