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

collection = ['hello', 2, 8, 3, 8, 21, 55]
fib = []
repeats = []
# for elem in collection:
#     if collection.count(elem) > 1 and elem not in repeats:
#         repeats.append(elem)
# print(*repeats)

deleted = []

for elem in collection:
    if elem is int and elem not in deleted:
        pass
    else:
        deleted.append(elem)

        # if int(collection[i]) == int(collection[i-2]) + int(collection[i-1]):
        #     fib = fib.append(collection[i], collection[i-1], collection[i-2])
        # else:
        #     print('error')
        #
print(deleted)



