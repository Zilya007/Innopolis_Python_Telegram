# Реализовать поиск последовательности Фиббоначи, А также найти элементы повторяющиеся в коллекции

# fib = [0, 1]
#  for i in range(2,100):
#      fib.append(fib[i-1] + fib[i-2])
#  print(fib)
#
#  count = 0
#  while len(fib) <= 100:
#      fib.append(fib[count] + fib[count + 1])
#      count += 1
#  print(fib)
#
# count = 0
# while fib[-1] < 100:
#     fib.append(fib[count] + fib[count + 1])
#     count += 1
# print(fib)

fib2 = [0, 1]
count = 0
while len(fib2) <= 15:
    fib2.append(fib2[count] + fib2[count + 1])
    count += 1
print(fib2)


#collection = ['hello', 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
collection = ['hello', 0, 1, 1, 2, 3, 3, 5, 8, 8, 8, ['a', ['b']], 13, 21, 34, 55, 89, 89, 89, 144, 233, 377, 610]
#collection = fib2.copy()
fib = []
reps = []

for elem in collection:
    if collection.count(elem) > 1 and elem not in reps:
        reps.append(elem)
print(f' Повторяющиеся элементы в последовательности : {reps}')

deleted = []

for elem in collection:
    if isinstance(elem, int) and elem not in deleted:
        pass
    else:
        deleted.append(elem)

for elem in collection:
    if elem in deleted:
        collection.remove(elem)
print(collection)

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

if len(fib) > 0:
    print(fib)
else:
    print("Последовательность фиббоначи не обнаружена")
