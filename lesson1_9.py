# Работа с файлами 1

# file = open('text/test.txt', 'r')
# result = file.read()
# #result2 = file.readlines()
# print(result)
# file.close()

# with open('text/test.txt','r') as file:                    # с данным методом закрывается автоматически
#     result = file.read()
# print(result)
#print(file.writable())         #проврека возможности записи
# file = open('text/test.txt', 'w')
# text = 'python'
# file.write(text)
# file.close()
#
# file = open(file='text/test.txt', mode='w')
# text = input('Введите текст:')
# file.write(text)
# file.close()

# file = open('text/newtest.txt', 'w')
# file.write('hello world')
# file.close()
#
# file = open('text/newtest.txt', 'a')            # режим добавления строки
# file.write('\npython language')
# file.close()
#
# file = open('text/newtest.txt', 'r')
# result = file.readlines()
# #print(result)
# result_temp = result[0]
# i = result_temp.find('\n')
# result[0] = result_temp[:i]
# # result[0] = result[0].split()
# # print(result[0][1])
# #result_temp.rstrip('\n')
#
# result[1] = 'c# language'
#
# file = open('text/newtest.txt', 'a')
# # for i in result:
# #     file.write(i)
# #     file.write('\n')
# # file.close()
#
# file.writelines(result)

with open('text/newtest.txt', 'w') as file:
    file.write('hello')
with open('text/newtest.txt', 'a') as file:
    file.write('\nworld')

with open('text/newtest.txt') as file:
    print(file.read())

