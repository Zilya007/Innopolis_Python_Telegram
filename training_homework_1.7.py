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