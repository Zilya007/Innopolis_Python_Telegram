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

file = open('text/newtest.txt', 'a')            # режим добавления строки
file.write('\thello')
file.close()

