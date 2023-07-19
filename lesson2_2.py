# my_list = [i*i for i in range(1,100)]
# print(my_list)
# chars = [i for i in 'Hello']
# print(chars)

# my_list = [i for i in range(1, 10) if i % 3 == 0]
# print(my_list)
# my_list= [[i * j for i in range(1,4)] for j in range(1,6)]
# print(my_list)
# my_list = [[0 for i in range(3)] for j in range(3)]
# for i in my_list:
#     print(i)

# my_list = [(lambda i: i * i)(i) for i in range(0,10)]
# print(my_list)

import itertools

# my_list = [i for i in itertools.repeat(1,5)]
# print(my_list)
# my_tuple = (i for i in range(0,5))
# print(my_tuple)
# print(next(my_tuple))
# my_dict = {x: x * 2 for x in range(1,10) if x % 2 == 0 }
# print(my_dict)

# my_dict = {x : y for x in 'abc' for y in 'defgh'}              доработать
# print(my_dict)
# my_dict ={x :0 for x in [1,3,5,7]}
# print(my_dict)

# my_dict = {}.fromkeys('abc',iter('def'))   доработать
# print(my_dict)

# my_dict =list(zip('abc', 'def'))
# # print(my_dict)
#
# my_dict_1 = {x: y for x,y in my_dict}
# print(my_dict_1)

# my_dict = {x: [y for y in range(x,x+3)] for x in range(4)}
# print(my_dict)

# my_dict = {x: {y for y in 'xyz'} for x in 'abc'}
# print(my_dict)

# my_dict = dict(zip('abcd', range(4,8)))
# print(my_dict)

# num = int(input('Введите числоЖ '))
# result = [i ** 0.5 for i in range(1,num)]
# print(result)

