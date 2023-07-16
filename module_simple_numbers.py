def simple_numbers(a, b):
    non_simple = []
    simple = []
    for i in range(2, b + 1):
        for j in range(2, b + 1):
            if i % j == 0 and i != j and i not in non_simple:
                non_simple.append(i)
    non_simple = list(set(non_simple))

    for i in range(a, b + 1):
        if i not in non_simple:
            simple.append(i)

    print(f'Список простых чисел диапазона {a, b}:')

    for i in range(0, len(simple)):
        if i >= 6 and i % 6 == 0:
            print('\n')
            print(simple[i], end='\t\t')
        else:
            print(simple[i], end='\t\t')

    print()
    return simple
