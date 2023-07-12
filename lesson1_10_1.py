# class Person:
#     def __init__(self, name, age):  # init вызывается при создании экземпляра класса - инициализация
#         self.name = name
#         self.age = age
#
#     # name = 'Иван'
#     # age = 35
#     def say_hello(self):  # self указание на самого себя
#         print('Hello, user')
#
#
# person1 = Person('Рамиль', 37)
# person2 = Person('Зиля', 31)

# #print(type(person1))
# #print(dir(person1))            # показывает все доступные методы
# # print(person1.name)
# # person1.say_hello()
# person1.name = 'Федор' # Изменение значения экземпляра класса
# Person.name = 'Зиля' # изменения атрибута самого класса

# class Car:
#     def __init__(self, color, speed):
#         self.color = color
#         self.speed = speed
#
#     def say_color(self):
#         return f'Цвет =  {self.color}'
#
#     def say_speed(self):
#         print(f'Скорость =  {self.speed}')
#
#
# car1 = Car('black', 100)
#
# print(car1.color)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Привет! Меня зовут {self.name}'

class Person1(Person):
    def __init__(self, name, age):
        super().__init__(name,age)

person1 = Person1('Ramil',33)
print(person1.say_hello())

