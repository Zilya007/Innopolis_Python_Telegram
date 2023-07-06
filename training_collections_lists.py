import random

# a = [1,2,3, ['a',4],'hello']
# b = list((1, 2, 3))
# c = [1, 2, 3, 4,]
# d = list('hello')
# e = [1, 2, 3, 4,]
# Для копирования списка без зависимостей нужно использовать метод copy , проверка области в памяти id
# a = [1, 3, 4, 2 , 6, 6, 7]
# a.sort()
# a.reverse()
# print(a.sort())
# print(a.count(6))
# b = []
# for elem in a:
#     if a.count(elem) > 1 and elem not in b:
#         b.append(elem)
#     else:
#         pass
#
# for elem in a:
#     if elem in b:
#         a.remove(elem)
#     else:
#         pass
# a.clear()
# del a - полное удаление из памяти
# a = [1, 2, 3 , 3]
# a.sort()
# random.shuffle(a) # метод перемешивает данные
# b = sorted(a)
# a.insert(2,99) подставляет новое значение , старое смещается на +1

# b = [8, 9, 10, 11]
# a.extend(b)
# b = [2, 5, 8, 7, 6]
# c = set(a)
# for num in c:
#     if num not in b:
#         print(num)

# a = (1)  # не кортеж
# b = (1, 2)
# print(type(a), type(b))

#a = 1, 2  # кортеж
#b = ([1,2,3])
#c = tuple('hello')
#print(c[::-2])            # слайс или срез

# a = 5
# b = 6
# a, b = b, a  # распаковка кортежей
# a, b, c = 1, 2, 'hello'
# print(a, b, c)

a = ('R', 2)
b, c = a
print(b, c)
