"""
День 1. Неделя 6.
Тема : Разбор старых тем


1.Создайте класс Soda(для определения типа газированной воды), принимающий 1 аргумент при инициализации
(отвечающий за добавку к выбираемому лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий
над печать "Газировка и {Добавка}" в случае наличия добавки, а иначе отобразится следующая фраза: 
"Обычная газировка".
"""

# class Soda:
#     def __init__(self, *add) :
#         self.add = add

#     def show_my_drink(self):
#         if self.add:
#             return f'Газировка и {self.add}'
#         else:
#             return 'Обычная газировка'

# soda = Soda('лимон')
# soda1 = Soda()
# print(soda.show_my_drink())
# print(soda1.show_my_drink())

"""
2. Николай – оригинальный человек. Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст. 
Но на этом он не успокоился. Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать 
“Николая”. В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет, а если его зовут, 
например, Максим, то оно преобразуется в “Я не Максим, а Николай”.Более того, никаких других атрибутов и методов у экземпляра
не может быть добавлено, даже если кто-то и вздумает так поступить (т.е. если некий пользователь решит прибавить к 
экземпляру свойство «отчество» или метод «приветствие», то ничего у такого хитреца не получится).
"""
# class Nikola:
#     __slots__ = ['name','age']

#     def __init__(self, name, age):
#         self.name = name
#         if not self.name == 'Николай':
#             self.name = f'Я не {self.name}, а Николай'
#         self.age = age

# name = Nikola('Jane',9)
# print(name.name)

# name1 = Nikola('Николай',31)
# print(name1.name)

"""
3.Мебель
1. class House: тип дома, общая площадь, оставшаяся площадь и список мебели.
2. Мебель имеет название и площадь, например, кровать: 4 м2, шкаф-купе: 2 м2,
стол: 1,5 квадратных метров.
3. Добавьте вышеуказанную мебель в дом.
4. При печати информации о доме требуется вывод: тип дома, общая площадь,
оставшаяся площадь, список мебели.
"""
# class Furniture:
#     def init(self,name_of_furniture,furniture_square):
#         self.name_of_furniture = name_of_furniture
#         self.furniture_square = furniture_square
#     def repr(self) -> str:
#         return f'{self.name_of_furniture},{self.furniture_square}'

# class House:
#     def init(self, type, area):
#         self.type = type
#         self.area = area
#         self.left_area = area
#         self.list_of_furniture = []
#     def add(self,classes):
#         if self.area > classes.furniture_square:
#             self.list_of_furniture.append(classes)
#             self.left_area -= classes.furniture_square
#         else:
#             print('Площаль мебели больше площади дома')

#     def str(self):
#         return f'тип дома:{self.type}, площадь дома:{self.area}, оставшаяся площадь:{self.left_area}, список мебели: {self.list_of_furniture}'

# krovat = Furniture('bed',2)
# bassein = Furniture('pool',100)
# house = House('kvartira',200)
# house.add(krovat)
# house.add(bassein)
# print(house)

"""
Таск
Создайте группу. Выведите информацию о группе: кол-во студентов, кол-во мальчиков и девочек, изучаемый язык, 
имя ментора, время занятий - также можно добавить свою логику

Попробовать дальше усовершенствовать программу
"""

# class Group:
#     def __init__(self, name, language, mentors, number_of_students, students) -> None:
#         self.name = name
#         self.language = language
#         self.mentors = mentors
#         self.number_of_students = number_of_students
#         self.students = students

#     def gender_filter(self):
#         print(self.students)
#         girls = {key: value for key, value in self.students.items()
#                  if value == 'Ж'}
#         boys = {key: value for key, value in self.students.items()
#                 if value == 'М'}
#         return f'Количество девушек в группе: {len(girls.keys())} и количество {len(boys.keys())}'
    
#     def get_general_info(self):
#         mentors = ' ,'.join(self.mentors)
#         students = {'Mr' + key for key in self.students.keys()}
#         return f'Есть группа с названием {self.name}\nОни изучают {self.language} \nKоличество студентов {self.number_of_students} \nMентора: {mentors} \nCтуденты: {students}'

#     # def del_students = 

#     def __str__(self) -> str:
#         return f'{self.mentors},{self.students} also {self.name},{self.language},{self.number_of_students}'
    


# name = input('Введите название группы: ')
# language = input('Введите название языка программирования: ')
# mentors = input('Введите имена менторов через пробел: ').split()
# number_of_students = int(input('Введите количество студентов: '))
# students = {}
# for i in range(1, number_of_students+1):
#     student = input('Введите студентов и их пол: ').split()
#     students[student[0]] = student[1]

# group = Group(name, language, mentors, number_of_students, students)
# print(group.get_general_info())
# print(group.gender_filter())

"""
Задача 1. Дана функция:
def say_hi():
    return 'python is good language'
print(say_hi())

Написать и применить к ней три декоратора:
Первый декоратор - для приведения всех символов к верхнему регистру
Второй декоратор - для разделения строки
Третий декоратор - для объединения в одно предложение
В результате должно получиться: "PYTHON IS GOOD LANGUAGE"
"""
# def upp(func):
#     def wrapper():
#         return func().upper()
#     return wrapper

# def spliting(func):
#     def wrapper():
#         return func().split()
#     return wrapper

# def united(func):
#     def wrapper():
#         return ' '.join(func())
#     return wrapper

# @united
# @spliting
# @upp
# def say_hi():
#     return 'python is good language'
# print(say_hi())

"""
Задача 2. Калькулятор

Напишите программу с классом Math. Создайте два атрибута — a и b. 
Напишите методы addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание. 
При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

"""
# class Math:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
    
#     def addition(self):
#         return f' a + b = {self.a + self.b}'
    
#     def multiplication(self):
#         return f' a * b = {self.a * self.b}'

#     def division(self):
#         return f' a / b = {self.a / self.b}'

#     def subtraction(self):
#         return f' a - b = {self.a - self.b}'
    
# count = Math(a = int(input('Enter the first number: ')),b = int(input('Enter the second number: ')))
# print(count.addition())
# print(count.subtraction())
# print(count.multiplication())
# print(count.division())
        

"""
Задача 3. Профиль 
Создайте класс профиля из соц сети. У профиля должен быть никнейм, эл. почта и возраст. 
Также создайте метод get_info, который выводит информацию о профиле в следующем виде: 
Nickname: girl_hunter 
Email: your_hero@gmail.com
Age: 12 y.o.
Затем объявите экземляр класса и вызовите метод.
"""
# class Profile:
#     def __init__(self,nickname,email,age):
#         self.nickname = nickname
#         self.email = email
#         self.age = age
    
#     def get_info(self):
#         return f'Nickname: {self.nickname} \nEmail: {self.email} \nAge:{self.age} y.o.'

# example = Profile(nickname = input('Enter your nickname: '), 
#                     email = input('Enter your email: '), 
#                     age = int(input('Enter your age: '))
#                     )

# print(example.get_info())
        

"""
Задача 4. Напишите программу с классом Car. Создайте конструктор класса Car. 
Создайте атрибуты класса Car — color (цвет), brand (тип), year (год). Напишите пять методов. 
Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». 
Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». 
Третий — присвоение автомобилю года выпуска. 
Четвертый метод — присвоение автомобилю бренда. 
Пятый — присвоение автомобилю цвета.
"""
# class Car:
#     def __init__(self,color,brand,year):
#         self.color = color
#         self.brand = brand
#         self.year = year
    
#     def start(self):
#         print('Автомобиль заведен')
    
#     def off(self):
#         print('Автомобиль заглушен')
    
#     def get_year(self):
#         return f'Возраст машины: {self.year}'
    
#     def get_brand(self):
#         return f'Бренд машины: {self.brand}'
    
#     def get_color(self):
#         return f'Цвет машины: {self.color}'
    
#     def __str__(self) -> str:
#         return self.age, self.brand, self.color

# car = Car(color = input('Enter your car\'s color: '), brand = input('Enter car\'s brand: '), year = input('Enter your car\'s year of release: '))
# car.start()
# car.off()
# print(car.get_year())
# print(car.get_brand())
# print(car.get_color())

"""
Задача 5. Спортсмены
Создайте классы Footballer и Snowboarder с одинаковым методом skill_info. 
Для футболиста он должен печатать "Я могу забить штрафной с 30 метров", 
для сноубордиста "В прыжке я делаю разворот на 360 градусов".
Объявите для каждого из классов по экземпляру. Затем объявить функцию show_skills, 
которая будет принимать спортсмена и вызывать у него метод skill_info.
"""

# class Footballer:
#     def skill_info(self):
#         return 'Я могу забить штрафной с 30 метров'

# class Snowboarder:
#     def skill_info(self):
#         return 'В прыжке я делаю разворот на 360 градусов'

# def show_skills(sportsman):
#     print(sportsman.skill_info())

# f = Footballer()
# s = Snowboarder()
# show_skills(f)
# show_skills(s)


"""
Check yourself. Week 5
"""

"""
1) Напишите декоратор, который печатает перед вызовом полученной функции строку: "Вызываю функцию <имя_функции>". 
Затем следует вызов функции. После вызова функции должна печататься строка: "Вызов функции <имя_функции> прошёл успешно"
"""

# def func_call(func):
#     def wrapper():
#         print(f'Вызываю функцию {func.__name__}')
#         func()
#         print(f'Вызов функции {func.__name__} прошёл успешно')
#     return wrapper

# @func_call
# def func1():
#     print('Функция запущена')
# func1()

"""
2) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). 
Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. 
Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и 
расчитайте площадь фигуры.
"""
# class Circle:
#     color = 'blue'
#     pi = 3.14

#     def __init__(self,radius:int):
#         self.radius = radius
    
#     def get_square(self):
#         return (self.radius**2)*self.pi
    
# circle = Circle(4)
# circle.color = 'white'
# print(circle.color)
# print(circle.get_square())
    
"""
3) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. 
Также создайте метод get_info, который выводит информацию о контакте в следующем виде: 
"Контакт: Иван Петров, телефон: +996555777888".
Затем объявите экземляр класса и вызовите метод.
"""
# class Telephone:
#     def __init__(self, name, last_name, number):
#         self.name = name
#         self.last_name = last_name
#         self. number = number

#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.number}')


# tel1 = Telephone('Иван', 'Петров', '+99678321142')
# tel1.get_info()

        
"""
4) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. 
Создайте метод display(), который будет выводит данные об этом человеке.
Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, 
которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. 
Создайте метод display_student(), который будет выводить данные об этом студенте.
Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.
"""
# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         return f'Имя: {self.name}\nВозраст: {self.age}'


# class Student(Person):
#     def __init__(self, name, age,faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
    
#     def display_student(self):
#         print(super().display(), f'\nСтатус: {self.faculty}')

# student = Student('Саске', 10, 'личинка шиноби')
# print(student.display())
# student.display_student()


"""
5) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", для кошек "Мяу".
Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), которая будет принимать животное и 
вызывать у него метод voice()
"""
# class Dog:
#     def voice(self):
#         return 'Гав'

# class Cat:
#     def voice(self):
#         return 'Мяу'

# dog = Dog()
# cat = Cat()

# def to_pet(animal):
#     print(animal.voice())

# to_pet(dog)
# to_pet(cat)