round = 1
while True:
    print(f'Раунд {round}')
    choice = input('Хотите начать игру? да/нет\n').lower()

    if choice == 'нет':
        break
    elif choice == 'да':
        print(f'Раунд {round}')
        print("Игра кретсики-нолики")
        print()
        ROWS = int(input("Введите число строк"))
        COLUMNS = int(input("Введите число столбцов"))
        area = []
        for i in range(ROWS):
            area.append([])
            for j in range(COLUMNS):
                area[i].append('*')

        step = 1
        for _ in area:
            print(_)
        while True:
            if step % 2 == 0:
                char = '0'
            else:
                char = 'X'
            print(f'Ходит {char}')
            row = int(input('Введите строку '))
            column = int(input('Введите столбец '))
            if area[row -1][column -1] == '*':
                area[row-1][column-1] = char
            else:
                print("Поле занято! Введите другие значения")
                continue
            step += 1

            if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
                print("Победили крестики")
                round += 1
                break

            if area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0':
                print("Победили нолики")
                round += 1
                break

            if step == 10:
                print("Ничья")
                round += 1
                break

            for _ in area:
                print(_)
    else:
        print("Неправильный выбор\n")
