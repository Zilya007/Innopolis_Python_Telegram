# side = int(input('Введите сторону квадрата: '))
#
#
# def main(side):
#     global area
#     area = side * side
#     print(area)
#
#
# main(side)
# print(area)

# def main():
#     x = 5 * 4
#     return x, 5
#
#
# result, result2 = main()
# print(result, result2)


# def fact(num):
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     return result
#
#
# print(fact(5))


x = 0
# def main():
#     x = 1
#     print(f'Внутри main {x = }')
#     def main1():
#         nonlocal x
#         x = 2
#         print(f'Внутри main1 {x = }')
#
#     main1()
#
#
# main()
# print(x)

# лямбда функции в одну строку

# print((lambda: 1 + 1)())
# sum = lambda: True
# print(sum())
# print((lambda x: x**2)(3))

# sum = lambda x: x + x
# print(sum(9))

# sum = lambda x, y: x + y
# print(sum(10, 2))

# a = lambda x, y, z: x + y * z
# print(a(1, 2, 3))

def perimetr(side1, side2=3):  # аргумент по умолчанию , если не передали
    return (side1 + side2) * 2

print(perimetr(2))
