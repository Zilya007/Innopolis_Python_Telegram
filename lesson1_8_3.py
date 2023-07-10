# def main(x, y):
#     '''Это функция возвращает сумму элементов'''
#     return x + y

# print(main(6,7))
# print(main.__doc__)
# print(dir(main))
# print(main.__name__)
# print(main.__module__)

# def main1(n, *args, **kwargs):
#     # print(f'{n = }')
#     # print(f'{args = }')
#     # print(f'{kwargs = }')
#     if args:
#         for ar in args:
#             n += ar
#     if kwargs:
#         for i in kwargs.values():
#             n += i
#     return n
#
#
# print(main1(2,  x=5, y=6))

# Рекурсия - функция которая вызывает саму себя с измененными данными
# для выхода оператор return
# def recur(n):
#     if n == 0:
#         return 1
#     print(f'{n}')
#     return recur(n - 1)
#
# recur(5)


# import sys
# sys.setrecursionlimit(5000)
#
# def main(n):
#     print(f'{n=}')
#     return main(n+1)
#
# main(0)

# def main(n):
#     if n <= 0:
#         return 1
#     return n * main(n - 1)
#
#
# print(main(3))

# def main(n):
#     while True:
#         if n == 247:
#             return
#         print(n)
#         n += 1
#
# main(1)

def bank(a, years):
    for i in range(years):
        a += a /10
    return a   # надо ставить после цикла


print(bank(100, 3))





# if __name__ == '__main__':
#     print('Меня вызвали как основную функцию')
#     print(main(3,2))