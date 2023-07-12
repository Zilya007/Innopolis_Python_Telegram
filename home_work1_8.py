# Реализация программы используя прошлый материал для нахождения результата, согласно условиям задачи

collection = ['hello', 6, 6, 0, 1, 1, 1, 2, 3, 2, 3, 3, 5, 8, 8, 8, ['a', ['b']], 13, 21, 34, 55, 89, 89, 89, 144, 233,
              377, 610,
              'hello']
base_collection = collection.copy()


def find_repeats():
    reps = []  # для отслеживания повторений

    for elem in collection:
        if collection.count(elem) > 1 and elem not in reps:
            reps.append(elem)
    return reps


def del_other_types():
    deleted = []
    for elem in collection:
        if isinstance(elem, int) and elem not in deleted:
            pass
        else:
            deleted.append(elem)

    for elem in collection:  # удаление нечисловых элементов последовательности
        if elem in deleted:
            collection.remove(elem)
    return collection


def find_fib(new_collection):
    fib = []  # для генерации ряда фиббоначи
    for i in range(len(collection)):
        if collection[i] == collection[i - 2] + collection[i - 1]:
            if collection[i] == 1 and fib.count(collection[i]) < 2:
                fib.append(collection[i])
            elif collection[i] not in fib:
                fib.append(collection[i])
            if collection[i - 1] != 1 and collection[i - 1] not in fib:
                fib.append(collection[i - 1])
            elif collection[i - 1] == 1 and fib.count(collection[i - 1]) < 2:
                fib.append(collection[i - 1])
            if collection[i - 2] not in fib and collection[i - 2] != 1:
                fib.append(collection[i - 2])
            elif collection[i - 2] == 1 and fib.count(collection[i - 2]) < 2:
                fib.append(collection[i - 2])
            fib.sort()
        else:
            pass
    return fib


def show_fib(fib, reps):
    if len(fib) > 0:
        print('В последовательности', *base_collection)
        print('Найден следующий ряд Фиббоначи: ', *fib)
        print('Повторяющиеся элементы в последовательности: ', *reps)
    else:
        print("Последовательность фиббоначи не обнаружена")


show_fib(find_fib(del_other_types()), find_repeats())
