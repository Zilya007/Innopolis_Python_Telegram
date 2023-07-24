# Реализовать программу использующую генераторы, и обрабатывающую данные последовательно с использованием итераторов
class Stack():
    def __init__(self):
        self.stack = [i for i in range(1, 50) if i % 2 == 0]  # генератор
        self.stack_pointer = 0

    def __iter__(self):                                     # настраиваем экземпляры класса итерируемыми
        stack_iter = iter(reversed(self.stack))
        return stack_iter

    def show_stack(self):
        rev = reversed(self.stack)
        if len(self.stack) != 0:
            print(*rev)
        else:
            print('Стек пуст!')

    def push(self, elem):
        print(f'Элемент {elem} будет добавлен в стек')
        self.stack.append(elem)
        self.stack_pointer += 1

    def pop(self):
        print("Выполняется удаление элемента из стека: ")
        if len(self.stack) != 0:
            elem = self.stack[self.stack_pointer - 1]
            self.stack.remove(elem)
            self.stack_pointer -= 1
        else:
            print('Ошибка, стек пуст!')

    def peek(self):
        if len(self.stack) != 0:
            print(f'Элемент на вершине стека {self.stack[self.stack_pointer - 1]}')
        else:
            print('Ошибка, стек пуст!')

stack = Stack()
myiter = iter(stack)
while True:
    choice = input('1 - Показать стек\t\t 2 - Добавить элемент\n'
                   '3 - Удалить элемент\t\t 4 - Показать вершину стека\n'
                   '0 - Выход\n')


    match choice:
        case '1':
            for i in myiter:
                print(i, end=' ')
            print()
        case '2':
            pass
        case '3':
            pass

        case '4':
            pass
        case '0':
            pass

