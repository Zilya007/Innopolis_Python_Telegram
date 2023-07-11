import csv

# with open('text/test.csv', mode='r', encoding='windows-1251') as file:
#     reader = csv.reader(file, delimiter=';')
#     for line in reader:
#         print(line)

# with open('text/test.csv', encoding='windows-1251') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     for line in reader:
#         # print(line.keys())

# file = open('text/test.csv', encoding='windows-1251')
# reader = csv.DictReader(file, delimiter=';')
# columns = reader.fieldnames
#
# with open('text/test2.csv', 'w', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, delimiter=',', fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(reader)
#
# file.close()


print('Блокнот')
mode = 'r'
file_name = input('Add name of file')
word_text = open(f'text/{file_name}.txt', mode=mode)
words = word_text.readlines()

while True:
    choice = input('Choose menu item 1, 2, 3, 0\n')
    match choice:
        case '1':
            print('--adding to file--')
            choice = input('Add new string')
            choice = '\n' + choice
            words.append(choice)
            mode = 'a'
        case '2':
            print('--rewriting file--')
            words = []
            choice = input('Add new string')
            words.append(choice)
            mode = 'w'
        case '3':
            print('--clearing file--')
            words = []
            mode = 'w'
        case '0':
            with open(f'text/{file_name}.txt', mode=mode) as file:
                if words != []:
                    print(words[-1])
                    file.writelines(words[-1])
        case _:
            print('error')
