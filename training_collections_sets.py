#a = set([])
#a = {1, 2, 3, 4}
#print(type(a))
#a = [1, 2, 3, 1]
#print(a)
#a = list(set(a))            # удаление дублей из разных коллекций
#print(a)

#a = {1, 2, 3, 4}
#b = {5, 6, 7}
#a.update([4, 5])
#a.pop() не известно какой элемент удалиться
#a.remove(4)
#a.add(5)
#a.add((5,6))     # обавлен кортеж,список не добавляется
#a.discard(3) # не вызывает ошибку даже если элемента нет удаляет
#a = a.union(b) # объединеие множеств

#print(a.difference(b))
#print(a.difference_update(b))
#print(a.intersection(b))  # пересечение
#print(a.intersection_update(b))

#print(a.symmetric_difference(b)) # уникальные для каждого из множеств элементы

#print(a.isdisjoint(b))     # проверяет на пересечение множеств
# if a.isdisjoint(b):
#     print('yes')
# else:
#     print('No')
#print(a.issubset(b)) # явяляется ли а подмножеством b

#print(a.issuperset(b)) # Входит ли в множество а множество

#a = frozenset([1, 2, 3, 4, 1])  # не изменяемое множество
#a = set(a)
#print(a)

a = [1, 2, 3, 4, 1]
b = [1, 2, 5]
c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(*c)

#print(set(a).intersection(set(b)))

#a = {1,2,4}
#print(5 in a)

# for i in a:
#     print(i)

a = {'a': 1, 'b': 2, 'c': 3}
# for i in a:         # или for i in a.keys():
#     print(i)

# for i in a.values():
#     print(i)

for k, v in a.items():
    print(f'Ключ: {k}, Значение: {v}')