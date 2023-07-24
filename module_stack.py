class Stack():
    def __init__(self):
        self.stack = []
        self.stack_pointer = 0

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
stack.pop()
stack.peek()
stack.show_stack()
stack.push(6)
stack.push(7)
stack.push(8)
stack.show_stack()
stack.peek()
stack.push(9)
stack.show_stack()
stack.peek()
stack.pop()
stack.show_stack()
stack.peek()
