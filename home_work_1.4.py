print("Программа нарисует елочку из выбранного символа!")

flag_input = True
while flag_input:
    symbol = input("Введите любой один символ:\n")
    if len(symbol) == 1:
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

split = level - 1
count = 1
for i in range(0, level):
    print(split * ' ', end='')
    split -= 1
    print(count * symbol, end='')
    count += 2
    print()