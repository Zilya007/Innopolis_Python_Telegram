# Реализовать скрипт вычисляющий разность квадрата суммы и суммы квадратов.
# Использование циклов, для решения задачи

result = []
for i in range(1, 101):
    result.append(0)
square_sum = []
sum_square = []


for i in range(1, 101):
    square_sum.append((i+i)**2)

for i in range(1, 101):
    sum_square.append(i**2 + i**2)

for i in range(0, 100):
    result[i] = (square_sum[i] - sum_square[i])
    print('Разность квадрата суммы и суммы квадратов числа ', end='')
    print(i+1, result[i], sep=' = ', end='.\n')

