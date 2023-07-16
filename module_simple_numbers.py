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
    # for elem in simple:
    #     if len(simple) > 6:
    #         if simple.index(elem) > 0 and simple.index(elem) % 6 == 0:
    #             print(elem)
    #         else:
    #             print(elem, end='\t\t')
    #     else:
    #         print(elem, end='\t\t')
    for i in range(1,len(simple)):
        if i == 6 or i % 6 == 0:
            print(simple[i],end='\n')
        else:
            print(simple[i],end ='\t\t')

    print()
    return simple
