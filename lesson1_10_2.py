# class Person:
#     def __new__(cls, *args, **kwargs):
#         print('method new')
#         return super(Person, cls).__new__(cls)
#
#     def __init__(self):
#         print('method init')
#
#
# person1 = Person()
# person2 = Person()

# class Car:
#     # def __init__(self, color):
#     #     self.color = color
#     def say_hello(self):
#         print('Hello')
# class Auto(Car):
#     # def __init__(self, color, speed):
#     #     super().__init__(color)
#     #     self.speed = speed
#     def say_speed(self):
#         print('speed')
#
# class Bus(Car, Auto):
#     def __init__(self,color,seed,speed):
#         super().__init__(color)
#         self.seed = seed
#
#     def say_seed(self):
#         print(f'{self.seed =}')
#
# car1 = Car('yellow')
# car2 = Auto('black',100)
# car3 = Bus('blue',35,80)
#
# car2.say_speed()
# car3.say_speed()

# class Test:
#     __name = 'Зиля'
#
#     def say_name(self):
#         print('hello')
#
# a = Test()
# a.say_name()
# #a.__name = 'Рамиль'
# print(a._Test__name)

# class Person:
#     def say_hello(self):
#         print('hello')
#
#
# class Person2(Person):
#     def say_hello(self):
#         print('world')
#
# a = Person2()
# a.say_hello()

#class Test(list):
    # def reverse_list(self):
    #     if len(self) > 2:
    #         return self[::-1]
    #     else:
    #         self.pop()
#     def __len__(self):          # переопределение метода
#         print('Length ')
#         return super().__len__()
# a = Test()
# a.append(1)
# a.append(2)
# #print(a.reverse_list())
# print(len(a))



