#
# try:
#     num = int(input('Введите число'))
#     print(num + 10)
# except Exception as err:
#     print(err)
# finally:
#     print('finally')
#

# class MyException(Exception):
#     def __init__(self,*args):
#         if args:
#             self.message = args[0]
#         else:
#             self.message = None
#
#     def __str__(self):
#         print("Call str")
#         if self.message:
#             return f'new error'
#         else:
#             return 'exception new error'
#
# raise MyException('This is my error')

# class Test:
#     def __init__(self):
#         self.name = 4
#
#     def __del__(self):                  #вызывается в конце , очищает из памяти
#         print("delete")
#
# a = Test()
# print(a.name)


# class Test:
#     def __init__(self, number):
#         self.number = number
#
#     def __add__(self, other):
#         return self.number + other
#
#     def __radd__(self, other):
#         return other + self.number
#
#     def __iadd__(self, other):
#         return self.number + other
#
#
# a = Test(5)
# print(a + 10)
# print(10 + a)

class Test:
    @classmethod            # обращение к методу через класс
    def say(cls):
        print('hello')
    @property                     #использование без скобок
    def say_hello(self):
        print('hello with decorator')

    @staticmethod                  #статический метод
    def say_static():
        print('static')


a = Test()
a.say()
Test.say()
a.say_hello
