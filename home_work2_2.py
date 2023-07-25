# Реализовать программу использующую генераторы, и обрабатывающую данные последовательно с использованием итераторов
class Stack:
    def __init__(self):
        self.stack = [i for i in range(1, 15) if i % 2 == 0]  # создание списка с помощью генератор
        self.stack_pointer = (int(len(self.stack) - 1))
        self.a = 1

    def __iter__(self):  # настраиваем экземпляры класса итерируемыми
        stack_iter = iter(reversed(self.stack))
        return stack_iter

    def __len__(self):
        return len(self.stack)

    def show_stack(self):
        # rev = reversed(self.stack)
        if len(self.stack) != 0:
            print(next(self.stack))  # использование метода next
        else:
            print('Стек пуст!')

    def push(self, elem):
        print(f'Элемент {elem} будет добавлен в стек')
        self.stack.append(elem)
        self.stack_pointer += 1

    def pop(self):
        if len(self.stack) != 0:
            elem = self.stack[self.stack_pointer]
            print(f'Элемент {elem} будет удален из стека ')
            self.stack.remove(elem)
            self.stack_pointer -= 1
        else:
            print('Ошибка, стек пуст!')

    def peek(self):
        if len(self.stack) != 0:
            print(f'Элемент на вершине стека {self.stack[self.stack_pointer]}')
        else:
            print('Ошибка, стек пуст!')


stack = Stack()

while True:
    choice = input('1 - Показать стек\t\t 2 - Добавить элемент\n'
                   '3 - Удалить элемент\t\t 4 - Показать вершину стека\n'
                   '5 - перебор элементов\t 0 - Выход\n')

    match choice:
        case '1':
            myiter = iter(stack)  # Использование итератора
            for i in myiter:
                print(i, end=' ')
            print()
        case '2':
            choice = input('Введите элемент для добавления в стек: ')
            stack.push(choice)
        case '3':
            stack.pop()
        case '4':
            stack.peek()
        case '5':
            myiter = iter(stack)
            input("Нажимайте 'Enter' для последовательного перебора элементов  ")
            for i in range(len(stack)):
                print(next(myiter), end=' ')  # использование итератора
                input()
        case '0':
            print('Завершение работы')
            break
            pass
