"""
День 3. Неделя 6.
Тема: Множественное наследование и миксины.

Виды наследования:
1. Многоуровневое - когда дочерний класс наследуется от родителя, который соответсвенно наследуется от другого класса
(A --> B --> C)

2. Одиночное - когда дочерний класс, наследуется от одного  родителя
(A --> B)

3. Иерархическое - когда много дочерних классов, наследуются от одного родителя
(A ---> P , B --> P, C --> P)

4. Гибридное - смесь более, чем одного вида наследования.
(A --> B, B ---> (A,C))


5. Множественное -  когда дочерний класс наследуется от множества родителей.
При множественном наследовании существует более одного родительского класса. От 2 до 10 или больше :)

A --> (P, B)

MRO(Method Resolution Order) - порядок, решения методов. Решает какой аттрибут родительского класса унаследует дочерний.

Миксины - это классы, не предназначенные для создания от них объектов.
Цель миксинов - расширение функционала других классов.

Начало практики:

- Повторение

"""
# class Parent:
#     def who_am_i(self):
#         print("I'm a parent")


# class Child(Parent):
#     def who_am_i(self):
#         super().who_am_i()
#         print("I'm a child")

# child = Child()
# child.who_am_i()

"""
- Множественное наследование на примерах

"""
# class Father:
#     last_name = 'White'


# class Mother:
#     last_name = 'Brown'


# # class Child(Father, Mother):
# #     pass


# class Child(Mother, Father):
#     pass

# child = Child()

# print(child.last_name) # White, если класс Father стоит впереди класса Mother при указании порядка наследования при создании класса Child

# print(child.last_name) # Brown, так как класс Мама стоит теперь впереди класса Папа

"""
Усложним этот же пример добавив Бабушку и Дедушку
В зависимости от порядка передачи родительских классов наследование аттрибутов будет проходить по порядку сперва 
первый родитель, а потом 2.
Следователь Питон сперва ищет аттрибут в первом родителе, если он находит, то сразу выдает, если такого аттрибута ищет в следующем родителе и так далле.
То есть ищет ближайщий аттрибут и выдает результат.
"""
# class Grandpa:
#     def talant(self):
#         print("I' good at dancing")

# class Grandma:
#     def talant(self):
#         print("I'm good at singing")

# class Father:
#     last_name = 'White'

#     def talant(self):
#         print("I can build houses")


# class Mother(Grandpa, Grandma):
#     last_name = 'Brown'


# class Child(Mother, Father):
#     pass

# child = Child()

# child.talant()#I' good at dancing

"""
MRO - Method Resolution Order

Рассмотрим данный метод на предыдущем примере.

Class_name.mro() - показывает в виде списка порядок наследования аттрибутов и методов для дочерних классов
"""
# class Grandpa:
#     def talant(self):
#         print("I' good at dancing")

# class Grandma:
#     def talant(self):
#         print("I'm good at singing")

# class Father:
#     last_name = 'White'

#     def talant(self):
#         print("I can build houses")


# class Mother(Grandpa, Grandma):
#     last_name = 'Brown'


# class Child(Father, Mother):
#     pass

# child = Child()

# print(Child.mro())
"""
Еще один пример с MRO
"""
# class A:
#     def __init__(self, param1,param2):
#         print(f"Hey, It's A class, I got first {param1} paremeter and second {param2} ")

#     def get(self):
#         print('AAA')

# class B:
#     def __init__(self,param1) -> None:
#         print(f"Hey, It's B class, I got first {param1} paremeter")


#     def get(self):
#         print('BBbbb')

# class C(B, A):
#     def __init(self):
#         print('Hey it\'s C class, I don\'t have any parameters')

#     def get(self):
#         print('CCCcc')

# c = C('Makers')
# print(C.mro())
# c.get() #CCCcc


"""
Diamond problem
Проблема ромба - получение непреугаданного результата
     
         A
        / \
       B---C
        \ /
         D

D --> B --> C ---> A

Из-за получения таких результатов, рекомендуется не использовать такие конструкции


"""
# class A:
#     def method(self):
#         print("Hello, I'm A")

# class B(A):
#     def method(self):
#         super().method()
#         print("Hello, I'm B")

# class C(A):
#     def method(self):
#         super().method()
#         print("Hello, I'm C")

# class D(B,C):
#     pass
#     # def method(self):
#     #     print("Hey, D")


# d = D()
# d.method()
# # print(D.mro())

"""
Миксины (Mix-in)

SOLID - принцип проектирования

NameMixin по правилам и для своего удобства принято так писать
"""
# class Insects:
#     def __init__(self):
#         print("I'm an insect ")

# class Bird:
#     def __init__(self) -> None:
#         print("I'm a bird")

# class FlyMixin:
#     def fly(self):
#         print("I can fly")

# class Butterfly(Insects, FlyMixin):
#     pass

# class Hawk(Bird, FlyMixin):
#     pass

# class Eagle(Bird, FlyMixin):
#     pass

# class Penguin(Bird):
#     pass

# hawk = Hawk()
# hawk.fly()

# eagle = Eagle()
# eagle.fly()

# ping = Penguin()

# butterfly = Butterfly()
# butterfly.fly()

"""
Пример
"""
# class Vehicle:
#     pass


# class Shower:
#     pass


# class Gadgets:
#     pass


# class RadioMixin:
#     def play_songs(self, station):
#         print(f"Playing some song on {station}")


# class Car(Vehicle, RadioMixin):
#     pass


# class Phone(Gadgets, RadioMixin):
#     pass


# class ShowerCabin(Shower, RadioMixin):
#     pass

# car = Car()
# car.play_songs('AsiaMix')

# phone = Phone()
# phone.play_songs('Europa-pus')

# shower = ShowerCabin()
# shower.play_songs('Retro-FM')


"""
Task
Таски
1.Создайте класс Auto в нем реализуйте метод ride который выводит сообщение 'Riding on a ground'.

Создайте класс Boat реализуйте метод swim, который выводит 'Floating on water'.

Создайте класс Amphibian который наследуется от класса Auto и Boat.

Создайте от него объект obj и вызовите все методы.

Ввод:

obj = Amphibian() 
obj.ride() 
obj.swim() 
Вывод:

Riding on a ground 
Floating on water 
"""

# class Auto:
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian()
# obj.ride()
# obj.swim()

"""
2.Создайте класс-миксин RadioMixin, и реализуйте в нем метод для проигрывания музыки play_music, который принимает в 
переменную title название песни.

Метод должен печатать строку "Песня называется title", где вместо title должно быть переданное название песни.

Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина. Класс Amphibian также как в 
предыдущем задании должен наследоваться от классов Auto и Boat. Создайте экземпляры auto, boat и obj от трех классов и 
примените метод play_music.
"""

# class RadioMixin:
#     def play_music(self, title):
#         print(f'Песня называется {title}')

# class Auto(RadioMixin):
#     def ride(self):
#         print('Riding on a ground')

# class Boat(RadioMixin):
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat, RadioMixin):
#     pass

# auto = Auto()
# auto.play_music('Between the bars')

# boat = Boat()
# boat.play_music('Hello')

# obj = Amphibian()
# obj.play_music('Noo')


"""
3.Будильник. Создайте класс Clock, у которого будет метод current_time показывающий текущее время и класс Alarm, 
с методами on и off для включения и выключения будильника.

Далее, создайте класс AlarmClock, который наследуется от двух предыдущих классов.

Добавьте к нему метод alarm_on для установки будильника, при вызове которого должен включатся будильник.

Создайте экземпляр clock класса AlarmClock и примените к ниму методы current_time и alarm_on.

Ввод должен быть:

clock.current_time() 
clock.alarm_on() 
С выводом:

17:10:41 
Будильник включен 
"""
# import datetime
# class Clock:
#     def current_time(self):
#         print(datetime.datetime.today().strftime('%H:%M:%S'))

# class Alarm:
#     def on(self):
#         print('Будильник включен')
#     def off(self):
#         print('Будильник выключен')

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         print('Будильник включен')

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()

"""
4.Напишите абстрактный класс Coder с атрибутом класса count_code_time = 0 и абстрактными методами get_info и coding.

Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder.

Класс Backend должен принимать дополнительно параметры experience и languages_backend, а Frontend такие параметры 
как — experience и languages_frontend соответственно.

Переопределите в обоих классах методы get_info и coding так, чтобы он принимал количество часов кодинга и при каждом вызове 
этого метода добавлял это значение к count_code_time.

Также бывают FullStack разработчики, поэтому создайте данный класс так чтобы у него были атрибуты и методы предыдущих 
классов. При этом нее определяйте никаких методов и атрибутов в данном классе он должен наследовать их от родительских 
классов.

Создайте экземпляры a, b, c от классов Backend, Frontend, FullStack соответственно и вызовите их методы.

Ввод должен быть:

a.coding(12) 
b.coding(45) 
c.coding(17) 
print(a.get_info()) 
print(b.get_info()) 
print(c.get_info()) 
Вывод:

Python разработчик, уровень: Junior, потрачено 12 часов на программирование

JavaScript разработчик, уровень: Middle, потрачено 45 часов на программирование

Python and JS разработчик, уровень: Senior, потрачено 17 часов на программирование 
"""
# from abc import ABC, abstractmethod

# class Coder(ABC):
#     count_code_time = 0

#     @abstractmethod
#     def get_info(self):
#         return f'{self.time}'

#     @abstractmethod
#     def coding(self, time,):
#         self.count_code_time = time


# class Backend(Coder):
#     def __init__(self, experience, languages_backend):
#         self.experience = experience
#         self.languages_backend = languages_backend

#     def coding(self, time):
#         self.count_code_time = time

#     def get_info(self):
#         return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'


# class Frontend(Coder):
#     def __init__(self, experience, languages_frontend):
#         self.experience = experience
#         self.languages_frontend = languages_frontend

#     def coding(self, time):
#         self.count_code_time = time

#     def get_info(self):
#         return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'


# class Fullstack(Backend, Frontend):
#     def __init__(self,experience, languages_backend):
#         self.experience = experience
#         self.languages_backend = languages_backend


#     def coding(self, time):
#         self.count_code_time = time

#     def get_info(self):
#         return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

# a = Backend('Junior','Python')
# b = Frontend('JavaScript','Middle')
# c = Fullstack('Senior','Python и JS')
# a.coding(12)
# b.coding(45)
# c.coding(17)
# print(a.get_info())
# print(b.get_info())
# print(c.get_info())

"""
5.Создайте два класса: Square и Triangle.

Класс Square должен иметь атрибуты: side - длина стороны квадрата.

Класс Triangle должен иметь аттрибуты: height - высота, base - длина.

У каждого из вышеуказанных классов должен быть метод get_area, который высчитывает и возвращает площадь - результатом должно 
быть целое число.

Создайте третий класс Pyramid который наследуется от первых двух классов, init унаследуйте от Triangle, дополнительные 
аттрибуты присваивать нельзя.

Добавьте метод get_volume для расчета объема пирамиды(формула: 1/3 x основание^2 x высоту), метод должен возвращать целое 
число.

"""
# from math import sqrt
# class Square:
#     def __init__(self, side):
#         self.side = side

#     def get_area(self):
#         return round(self.side**2)


# class Triangle:
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base

#     def get_area(self):
#         return round(0.5*self.base*self.height)


# class Pyramid(Triangle, Square):
#     def get_volume(self):
#         pyramid_height = sqrt(self.height**2 - (self.base/2)**2)
#         return int((1/3)*(self.base**2)*self.height)

# pyramid = Pyramid(5, 7)
# print(pyramid.get_volume())


"""
6.Создайте класс ToDo, с пустым init методом, а также с переменной класса, в виде словаря todos = {}.

У класса должен быть один метод set_deadline, который принимает дату дедлайна и возвращает количество дней оставшихся
 до дедлайна.

Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin, DeleteMixin, UpdateMixin, ReadMixin:

в классе CreateMixin определите метод create, который принимет в себя задачу и ключ по которому нужно добавить задачу 
в словарь todos.

класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу, который передается как аргумент, и 
возвращает сообщение 'удалили название задачу', где вместо слова название должно быть название задачи.

класс UpdateMixin должен содержать метод update, который принимает в себя ключ и новое значение и заменяет задачу 
под данным ключом на новое значение.

класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач.
"""


# class CreateMixin:
#     def create(self, key, task):
#         self.todos[key] = task
#         return self.todos


# class DeleteMixin:
#     def delete(self, key, task):
#         self.todos.pop(key)
#         return f'удалили {task} задачу'


# class UpdateMixin:
#     def update(self, key, new_task):
#         self.todos[key] = new_task
#         return self.todos


# class ReadMixin:
#     def read(self):
#         return sorted(self.todos.items())


# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}

#     def set_deadline(self, deadline):
#         from datetime import datetime
#         deadline = datetime.strptime(deadline, '%d-%m-%Y').date()
#         today = datetime.today().date()
#         diference = (deadline - today).days
#         return f'До дедлайна осталось: {diference} дней '


# todo1 = ToDo()
# print(todo1.create('3', 'помыть посуду'))
# print(todo1.create('1', 'сделать дз'))
# print(todo1.update('1', 'приготовить обед'))
# print(todo1.set_deadline('30-11-2021'))


"""
7.
"""
# class ExtensionMixin:
#     def add_extension(self, extension):
#         self.extensions.append(extension)
#         return f'Добавлено новое расширение {extension} для игры {self.name}'

#     def remove_extension(self, extension):
#         if extension in self.extensions:
#             index = self.extensions.index(extension)
#             self.extensions.pop(index)
#             return f'{extension} был отключен от {self.name}'
#         else:
#             return 'Такого экстеншна нету в списке'


# class Game(ExtensionMixin):
#     def __init__(self, type, name):
#         self.type = type
#         self.name = name
#         self.extensions = []

#     def get_description(self, description):
#         return f'{self.name} это {description}'

#     def get_extensions(self):
#         if self.extensions:
#             return self.extensions
#         else:
#             return 'Нет подключенных расширений'


# game = Game(type='Ps5', name='Minecraft')
# print(game.get_description('Супер игра четкая ваще'))
# print(game.add_extension('Multiverse-Core'))
# print(game.add_extension('New-York life'))
# print(game.remove_extension('Multiverse-Core'))
# print(game.get_extensions())


"""
Начало разбора
"""
# class A:
#     def method(self):
#         print('A')

# class B:
#     def method(self):
#         print('B')

# class C(A,B):
#     def method(self):
#         super().method()
#         print('C')
# c1 = C()
# c1.method()

"""

"""
# class Animal:
#     def walk(self):
#         raise NotImplementedError

# class Snake:
#     def bite(self):
#         pass

"""
abstractmethod
"""
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass

# class Cat(Animal):
#     def eat(self):
#         print('Nyam-nyam')

# cat1 = Cat()
# cat1.eat()


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""


"""

"""
