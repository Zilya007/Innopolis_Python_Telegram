# city = "Kazan"
# for i in range(len(city)):
#     print(city[i], end='')
# print()
# for i in city:
#     print(i,end='')

# Вывести все четные числа из списка:
# a = [1,2,3,4,5,6,7,8,9,10,11,12]
#a = list(range(0,100))
# c = []
# for i in a:
#     if i % 2 == 0 and i > 0:
#         c.append(i)
#     else:
#         pass
# print(c)

# for i in a:
#     if i % 2 == 0 and i > 0:
#         print(i, end=' ')

secret_word = 'book'
print("Игра угадай слово!")
for _ in range(len(secret_word)):
    print('*', end='')
print()

user_chars = []
attempts = 5
length_compare =0
while attempts > 0:
    is_Win = True
    user_letter = input("Введите букву!\n")
    user_chars.append(user_letter)
    for char in secret_word:
        if char in user_chars:
            print(char, end='')
        else:
            print("*", end="")
            is_Win = False

    print()

    # count_in = range(1,4)
    # for _ in count_in:
    #     if user_letter in secret_word and secret_word.count(user_letter) == _:
    #         length_compare += _
    # if length_compare == len(secret_word):
    #     print('Вы победили')
    #     break
    # if length_compare == len(secret_word):
    #     print("Вы победили")
    #     break

    if user_letter not in secret_word:
        attempts -= 1
    if attempts == 0:
        print("Вы проиграли!")
        print(f'Секретное слово {secret_word}')
    if is_Win:
        print("Победа")
        break


