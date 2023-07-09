# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(5))
#
#
# x = lambda: 'welcome'
# y = lambda x: print(f'world {x()} ')
# y(x)

# def main(func):
#     print('hello')
#     func()
#     print('end')
#
# func = lambda : print('world')
# main(func)
#import tkinter.messagebox as tmb  #псевдоним
#tmb.showerror()

def main():
    work_list = []
    while True:
        print('Выберите действие: ')
        choice = input('1-Add; 2-Change; 3-Delete; 4-Show all; 0-Exit\n')
        match choice:
            case '1':
                add_db(work_list)
            case '2':
                change_db(work_list)
            case '3':
                delete_db(work_list)
            case '4':
                show_all(work_list)
            case '0':
                print('Выход')
                break
            case _:
                print("Неправильный выбор")
def add_db(work_list):
    number = int(input('Введите значение: '))
    if number not in work_list:
        work_list.append(number)
    else:
        print('Данное значение уже есть ')

def change_db(work_list):
    number = int(input('Введите значение для изменения: '))
    try:
        index = work_list.index(number)
        work_list[index] = int(input('Введите новое значение'))
        print(work_list)
    except Exception as err:
        print(f"error {err}")

def delete_db(work_list):
    number = int(input('Введите значение для удаления: '))
    try:
        work_list.remove(number)
    except Exception as err:
        print(f'Ошибка {err}')

def show_all(work_list):
    for _ in work_list:
        print(_)
if __name__ == '__main__':
    main()