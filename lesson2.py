import random
secretNumber = random.randint(1,10)
print("Угадай число от 1 до 10. ")
attempts = 3
userAttempts = f"Ваши введенные попытки :"
while attempts > 0:
    print("Введите число, дается 3 попытки: ")
    userNumber = input()
    if userNumber.isnumeric():
        userNumber = int(userNumber)
        if userNumber == secretNumber:
            print("Вы угадали!")
            print(userAttempts)
        elif userNumber > secretNumber:
            if userNumber - secretNumber >= 10:
                print("Число слишком большое! Попробуйте снова!" )
            else:
                print("Число чуть больше чем загаданное!")
        elif userNumber < secretNumber:
            if secretNumber - userNumber >=10:
                print("Число слишком маленькое, попробуйте снова!")
            else:
                print("Число чуть меньше загаданного!")
        attempts -= 1
        userAttempts = userAttempts + " " + str(userNumber)
        if attempts == 0:
            # print("Вы проиграли!" + "Секретное число = " + str(attempts))
            print(f'Вы проиграли! Секретное число было {secretNumber}')
            print(userAttempts)
    else:
        print("Ошибка Ввода!")