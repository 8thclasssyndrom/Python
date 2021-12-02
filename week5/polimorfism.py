"""
День 5. Неделя 5. 19 ноября
Тема: Полиморфизм

Полиморфизм  – это возможность обработки разных типов данных, т. е. принадлежащих к разным классам, 
с помощью "одной и той же" функции, или метода 

Под полиморфизмом понимается множество форм одного и того де слова-имени метода

Один метод ----> много разных результатов для разных классов

Начало практики


Пример использование полиформезме на примере оператора " + ":
"""
# a = 6
# b = 9
# print(a+b) #15

# c = '6'
# d = '9'
# print(c+d) #'69

# f = [1,2,3,4,5]
# e = [6,7,8,9,10]
# print(f+e) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


"""
dir() - возвращает все методы класса
__add__ - 
Как мы видим в примере ниже у нас есть одни методы для разных классов
"""
# a = 'makers'
# b = 3
# c = [True, 'bootcamp',677]
# d = {'makers':'bootcamp'}
# e = (6,7,8,9)
# f = {False, 'makers',6,3,8}
# print(f'This is string methods: {dir(a)}')
# print(f'This is integer methods: {dir(b)}')
# print(f'This is list methods: {dir(c)}')
# print(f'This is dictionary methods: {dir(d)}')
# print(f'This is tuple methods: {dir(e)}')
# print(f'This is set methods: {dir(f)}')

"""
pop() -> list, dict, set

"""
# list_ = [3,4,5,6]
# dict_ = dict(a=1,b=2,c=3)
# set_ = {True,'makers',78,0}

# list_.pop(2)   # запрашивает индекс, или по умолчанию последний
# dict_.pop('b') # удаляет по ключу
# set_.pop() # удаляет любой элемент, но начиная с питон 3.7 последний элемент множества

# print(list_, dict_, set_)

"""
update() -> dict, set
"""
# dict_ = dict(a=1,b=3,c=3)
# set_ = {True,'makers'}

# dict_.update(d=4, e=5)
# set_.update({8,0,-1})
# print(dict_)
# print(set_)

"""
Использование полиморфизма в классах
"""
# class Car:
#     def __init__(self,name):
#         self.name = name
#     def go_by_car(self, destination):
#         print(f'{self.name} is going by car to {destination}')

# class  Ship:
#     def __init__(self,name):
#         self.name = name
#     def go_by_ship(self, destination):
#         print(f'{self.name} is going by ship to {destination}')

# class Airplane:
#     def __init__(self,name):
#         self.name = name

#     def fly_by_aiplane(self,destination):
#         print(f'{self.name} is flying by airplane to {destination}')


# class Train:
#     def __init__(self,name) -> None:
#         self.name = name

#     def go(self,destination):
#         print(f'{self.name}is going by train to {destinaton}')

"""
Пример с классом Cat:

"""

# class InfoMixIn: # Mix-in - это такие классы, только от них не создаются экземпляры и объекты, они просто содержат какоё-то функционал, за счет которого функционал другого расширяется.
#     def info(self):
#         my_class = self.__class__.__name__
#         print(f"I'm a {my_class}, named {self.name}, age {self.age}")


# class Cat(InfoMixIn):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print('Meow')

# class Dog(InfoMixIn):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print('Gav-gav')

# class Duck(InfoMixIn):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print('Quack')


"""
Последний пример с одним и тем же названием
"""
# class T1:
#     def __init__(self,iterable):
#         self.list = iterable

#     def total(self):
#         return sum(self.list)

# class T2:
#     def __init__(self,iterable):
#         self.list = iterable

#     def total(self):
#         return len(self.list)

# t1 = T1([1,2,3,4,5])
# t2 = T2([1,2,3,4,5])
# print(t1.total()) #15
# print(t2.total()) #5

"""
Classwork
Классная работа

1) Реализуйте программу по следующему описанию. Есть классы WhatsApp, SnapChat, Telegram. 
При регистрации в WhatsApp и SnapChat необходимо передавать свой номер телефона, который должен быть int. 
При регистрации в Telegram необходимо передавать номер телефона и username. Во всех классах есть метод send, 
в WhatsApp он принимает только text и выдает строку “I am sending a text ...” и вместо … должен быть сам текст сообщения. 
В SnapChat send принимает image и text, при этом image должен быть булевым типом данных. 
Если image True, то выдается сообщение “I am sending a text … with some image ”, если  
False - сообщение “I am sending a text … without image”. В Telegram метод send принимает voice message в виде строки и 
выдает сообщение “I am sending a voice message ...”. Создайте объекты от этих классов и вызовите метод send у всех объектов.
"""
# писать код здесь

# class WhatsApp:
#     def __init__(self,phone:int):
#         self.phone = phone

#     def send(self,text:str):
#         print(f'I am sending a text {text}')

# class SnapChat:
#     def __init__(self,phone:int):
#         self.phone = phone

#     def send(self,image:str,text:str):
#         if image:
#             print(f'I am sending a text {text} with some image')
#         else:
#             print(f'I am sending a text {text} without image')

# class Telegram:
#     def __init__(self,phone:int,username):
#         self.number = phone
#         self.username = username
#     def send(self,voice_message):
#         print(f'I am sending a voice message {voice_message}')


# person1 = WhatsApp(99657548454)
# person1.send('Hello Makers')

# person2 = SnapChat(33445454)
# person2.send(image = True, text = 'What are you doing?')

# person3 = Telegram(42424252,'bber')
# person3.send('Hi')

# person4 = SnapChat(4332424)
# person4.send(0, 'drdr')


"""
2) Создайте два класса A и B. В обоих классах есть метод count. 
В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count, 
а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов и вызовите этот метод у каждого объекта.
"""
# писать код здесь

# class A:
#     def count(self,word:str):
#         vowel = 'eyiuoa'
#         self.res = [i for i in word if i in vowel]
#         if self.res:
#             return len(self.res)

# class B:
#     def count(self,word:str):
#         vowel = 'eyiuoa'
#         self.res = [i for i in word if i not in vowel]
#         if self.res:
#             return len(self.res)

# k=A()
# print(k.count('Makers'))
# b = B()
# print(b.count('Bootcamp'))


"""
Tasks
Таски

1.Объявите 3 переменные - a, b и c.

В а запишите строку, в b - список и в с сохраните словарь. Затем запишите все три переменные в список, 
пройдитесь по нему циклом и распечатайте длину каждого из объектов.

Например:

a = '12342342345' 
b = [1,['a',5,6],2,3,4,5] 
c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 
Вывод:

11 
6 
3 
"""
# class Length:
#     def __init__(self,obj):
#         self.obj = obj
#     def length(self):
#         for i in self.obj:
#             print(len(i))


# a = '12342342345'
# b = [1,['a',5,6],2,3,4,5]
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'}
# list_ = Length([a,b,c])
# list_.length()


"""
2.Создайте классы Dog и Cat с одинаковым методом voice.

Для собак он должен печатать "Гав", для кошек "Мяу".

Объявите для каждого из классов по экземпляру, для класса Cat экземпляр в переменной barsik, а для Dog экземпляр rex.

Затем, вне класса объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice().

Ввод:

to_pet(barsik) 
to_pet(rex) 
Вывод:

Мяу 
Гав 
"""
# class Dog:
#     def voice(self):
#         print('Гав')

# class Cat:
#     def voice(self):
#         print('Мяу')

# def to_pet(animal):
#     return animal.voice()

# barsik = Cat()
# rex = Dog()
# to_pet(barsik)
# to_pet(rex)

"""
3.Создайте 3 класса: Person с параметрами name и last_name, Employee с work и status, Student c university и course, при этом Employee и Student должны наследоваться от Person.

Определите во всех трёх классах метод get_info():

для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.

для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.

для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.

Вне класса, определите функцию get_human_info(), которая будет принимать объект одного из трёх классов и вызывать у него метод get_info и распечатывать результат этой функции.

Создайте для каждого класса по экземпляру, для Person экземпляр person, для Employee экземпляр employee и student для класса Student.

Вызовите метод get_human_info у каждого экземпляра печатать результат.

Ввод должен быть:

get_human_info(employee) 
get_human_info(student) 
get_human_info(person) 
Вывод:

Привет, меня зовут Иван Петров, я работаю в компании Рога и Копыта на должности директор 
Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе 
Привет, меня зовут Иван Иванов 

"""
# class Person:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'


# class Employee(Person):
#     def __init__(self,name,last_name,work,status):
#         super().__init__(name,last_name)
#         self.work = work
#         self.status = status

#     def get_info(self):
#         return super().get_info() + f', я работаю в компании {self.work} на должности {self.status}'

# class Student(Person):
#     def __init__(self,name,last_name,university,course):
#         super().__init__(name,last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return super().get_info() + f', я учусь в {self.university} на {self.course} курсе'

# def get_human_info(information):
#     print(information.get_info())

# person = Person('Иван', 'Петров')
# employee = Employee('Иван', 'Петров','Рога и Копыта','директор')
# student = Student('Иван', 'Петров','КГТУ','3')

# get_human_info(employee)
# get_human_info(student)
# get_human_info(person)

"""
4.Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() 
для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.

Затем, наследуйте от Shape три класса: Triangle, Square и Circle.

треугольник создаётся с заданными основанием base и высотой height

квадрат создаётся с заданной длиной стороны length

круг создаётся с заданным радиусом radius

Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.

Затем, создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()

Подсказка: для создания абстрактных классов воспользуйтесь модулем abc - https://docs.python.org/3/library/abc.html

Ввод должен быть:

print(triangle.get_area()) 
print(square.get_area()) 
print(circle.get_area()) 
Вывод:

12.5 
25 
314.1592653589793 
"""
# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         raise NotImplementedError

# class Triangle(Shape):
#     def __init__(self,base, height):
#         self.base = base
#         self.height = height

#     def get_area(self):
#         return (self.base*self.height)/2

# class Square(Shape):
#     def __init__(self,length):
#         self.length = length
#     def get_area(self):
#         return (self.length*self.length)

# class Circle(Shape):
#     def __init__(self,radius):
#         self.raidus = radius
#     def get_area(self):
#         return (self.raidus*self.raidus) * math.pi

# triangle = Triangle(5,5)
# square = Square(5)
# circle = Circle(10)

# print(triangle.get_area())
# print(square.get_area())
# print(circle.get_area())

"""
5.Создайте класс OS, экземпляры которого имеют аттрибут version - версия системы. От OS наследуйте три класса - Windows, MacOS, Linux.

У всех трех классов должен быть метод copy который принимает в аргументы text и возвращает соответствующую строку.

Создайте экземпляры класса, от Windows - в переменной win, от MacOS - mac, а от Linux в переменной lin.

Примените к каждому объекту метод copy, следующим образом:

Ввод должен быть:

print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
 
print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))
Вывод должен быть:

скопирован текст "Полиморфизм — одна из основных парадигм ООП" горячими клавишами CTRL + C
 

скопирован текст "Полиморфизм - разное поведение одного и того же метода в разных классах" горячими клавишами COMMAND + C
 

скопирован текст "На самом деле одинаковым является только имя метода, его исходный код зависит от класса" горячими клавишами CTRL + SHIFT + C
"""

# class OS:
#     def __init__(self, version):
#         self.version = version


# class Windows(OS):
#     def __init__(self, version):
#         super().__init__(version)
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + C'


# class MacOS(OS):
#     def __init__(self, version):
#         super().__init__(version)
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами COMMAND + C'


# class Linux(OS):
#     def __init__(self, version):
#         super().__init__(version)
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'


# win = Windows('10')
# mac = MacOS('7')
# lin = Linux('Ubuntu')

# print(win.copy('Hello World'))
# print(mac.copy('Makers'))
# print(lin.copy('Never give up!'))


"""
6.Создайте класс Language, экземпляры которого имеют такие свойства как level и type.
Наследуйте от данного класса два других класса - Python и JavaScript. И у Python, и у JavaScript должно быть два метода:

write_function, принимает такие аргументы как func_name и arg
create_variable, с аргументами var_name, value
Создайте экземпляр от класса Python в переменной py.

Затем, примените методы к экземпляру класса Python:

print(py.write_function('get_code', 'a')) 
print(py.create_variable('name', 'John'))
вывод должен быть такой:

def get_code(a):    
name = 'John'
Создайте экземпляр от класса JavaScript в переменной js.

Примените метод следующим образом:

print(js.write_function('validate', 'form')) print(js.create_variable('password', 'john@123'))
Вывод должен быть таким:

function validate(form) {     }; 
let password = 'john@123'
"""
# class Language:
#     def __init__(self,level,type):
#         self.level = level
#         self.type = type

# class Python(Language):
#     def __init__(self, level, type):
#         super().__init__(level, type)

#     def write_function(self,func_name, arg):
#         return f'def {func_name}({arg}):'    

#     def create_variable(self,var_name, value):
#         if isinstance(value,str):
#                     return f"{var_name} = '{value}'"
#         return f"{var_name} = {value}"

# class JavaScript(Language):
#     def __init__(self, level, type):
#         super().__init__(level, type)
    
#     def write_function(self,func_name, arg):
#         return f'function {func_name}({arg})' + ' {     };'     

#     def create_variable(self,var_name, value):
#         if isinstance(value,str):
#             return f"let {var_name} = '{value}';"
#         return f"let {var_name} = {value};"
    

# py = Python('high-level', 'interpreted')
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))

# js = JavaScript('high-level', 'interpreted')
# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))

"""
7.Создайте класс Money, объекты которого имеют аттрибуты country и symbol. Наследуйте от него классы Dollar и Euro. 
У данных методов должна быть переменная класса rate, курс к сому, Dollar - 84.80, Euro - 98.40. 
Добавьте к этим классам метод exchange, который принимает количество которое нужно обменять в переменную amount и 
возвращает такую строку:

$ 100 равен 8480.0 сомам
€ 80 равен 7872.0 сомам
"""
# class Money:
#     def __init__(self,country,symbol):
#         self.country = country
#         self.symbol = symbol
    
# class Dollar(Money):
#     def __init__(self, country, symbol):
#         super().__init__(country, symbol)
#         self.rate = 84.40
#     def exchange(self,count):
#         total = self.rate*count
#         return f'$ {count} равен {total} сомам'

# class Euro(Money):
#     def __init__(self, country, symbol):
#         super().__init__(country, symbol)
#         self.rate = 98.40
#     def exchange(self,count):
#         total = count*self.rate
#         return f'€ {count} равен {total} сомам'
    
# d1 = Dollar('America','$')
# print(d1.exchange(100))
# e1 = Euro('Europe','€')
# print(e1.exchange(80))

        
"""
8.Создайте классы Mercury, Venus, Jupiter, которые наследуют метод __init__ от родительского класса Planet.
 У объектов данного класса должен быть аттрибут orbit, орбита в классе Venus состовляет 225 земных дней, 
 Mercury 88 земных дней, а на Jupiter 12 дней. У всех этих классов должен быть метод get_age, принимающий возраст 
 в переменную earth_age и расчитывающий ваш возраст на данной планете.

Метод должен возвращать возраст на Mercury в годах, на Venus в днях и на Jupiter в часах. 
Например, если возраст earth_age равен 20:

на Венере ваш возраст составляет 11842 дней
на Юпитере ваш возраст составляет 5326080 часов
на Меркурии ваш возраст составляет 82 лет
"""
# class Planet:
#     def __init__(self,orbit) -> None:
#         self.orbit = orbit
    
# class Mercury(Planet):
#     def __init__(self, orbit) -> None:
#         super().__init__(orbit)
#     def get_age(age):
#         return f'на Меркурии ваш возраст составляет {self.orbit}'


# class Venus(Planet):
#     def __init__(self, orbit) -> None:
#         super().__init__(orbit)
    
# class Jupiter(Planet):
#     def __init__(self, orbit) -> None:
#         super().__init__(orbit)

        
"""
Начало разбора

Полиморфизм - возможность функции работать, с объектами разных типов, при условии того, что объект поддерживает 
операцию(объект обладает нужным методом).

"""
# class A:
#     def __init__(self,attr1):
#         self.attr1 = attr1
    
#     def __add__(self,other):
#         return self.attr1 + other.attr1
    
# a1 = A(10)
# a2 = A(20)

# print(a1 + a2) #30


"""
Функции в Питоне очень полиморфичны
 
"""
# class A:
#     def __init__(self,value):
#         self.value = value

# a1 = A(10)
# a2 = A('at')
# a3 = A([1,2,3,4])
# a4 = A({'a':1,'b':2})


# a1 = 'string'
# a2 = [1,2,3]
# a3 = (1,2,3)
# a4 = {'a':1,'b':2}

# def len(obj):
#     if hasattrr(obj, '__len__'):
#         return obj.__len__()
#     raise TypeError('.......')


# class Office:
#     def __init__(self,employees):
#         self.employess =  employees

# office = Office(['alibek','Janyl','Ernek','Janybek','Inna'])

# print(len(office))

"""
Example with class Square, Circle, Triangle 
"""
# class Square:
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         return self.side**2

# sq1 = Square(4)
# print(sq1.area())
    
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
    
#     def area(self):
#         from math import pi
#         return pi*(self.radius**2)

# c1 = Circle(5)
# print(c1.area())

# class Triangle:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
    
#     def perimeter(self):
#         return self.a + self.b + self.c
    
# tr1 = Triangle(10,14,13)
# print(tr1.perimeter())

# def get_shape_area(shape):
#     shape.area()


# get_shape_area(sq1)
# get_shape_area(c1)
# get_shape_area(tr1)

        

   
        

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
