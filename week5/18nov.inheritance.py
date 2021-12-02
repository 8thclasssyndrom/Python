"""
День 4.Неделя 5.
Тема: Наследование


Родительский(суперкласс, надкласс, базовый) ---> parent, inharited,base
Дочерний(подкласс, производный)             ---> child,derived

Наследование - это один из принципов ООП.
Наследование - это процесс, когда из одного класса происходит другой.

- Дочерний класс может определять свои свойства
- Дочерний класс может переопределять свойства родителя, дополнять методы родителя.

- Дочерние классы наследуют особенности родительских
- Дочерние классы не зависят от других дочерних классов
- Объект дочернего класса является экземпляром родительского класса.
- Для удобства обращение к методам родительского класса Python предоставляет функцию super().


super - функция, которая может возвращать методы и аттрибуты родительского класса.


Синтаксис наследования: 

Parent наследуется от object, но сейчас писать такое не обязательно
Также можно просто писать Parent()
"""

# class Parent(object):
#     pass

# class Child(Parent):
#     pass


"""
Дочерний класс получает все методы родительского
"""
# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

"""
isinstance(obj,class) - проверяет является ли объект obj экзмепляром класса class
"""
# c = C()
# print(isinstance(c,A))

"""
Наследование методов и атрибутов на примерах

Например, создадим многоульник и найдем его периметр
"""
# class Polygon: #родительский

#     sides = 'many' #сколько сторон есть у нашего многоугольника

#     def __init__(self,*args, **kwargs):
#         self.args =  args
#         self.kwargs = kwargs
#         # print(self.args)
#         # print(self.kwargs)

#     def get_perimetr(self):
#         if self.args:
#             return sum(self.args)
#         elif self.kwargs:
#             return(sum(self.kwargs.values()))

# class Rectangle(Polygon): #дочерний
#     sides = 4 #у прямоугольника четыре стороны, поэтому прописываем это
#     def __init__(self,a , b ):
#         self.a = a
#         self.b = b
#     def get_perimetr(self): # меняем формулу для получения периметра
#         return (self.a+self.b)*2

# def Triangle(Polygon): # ещё один дочерний класс от многоульника
#     sides = 3
#     # def __init__(self,g,b,c):
#     #     self.g = g
#     #     self.b = b
#     #     self.c = c

#     # def get_perimeter(self):
#     #     return self.a + self.b + self.c

# triangle1= Triangle(g=3, b=4,c=5,d =7, f =6)
# print(triangle1.sides)
# print(triangle1.get_perimeter())


# rectangle = Rectangle(a = 7, b = 6)
# print(rectangle.sides)
# print(rectangle.get_perimetr())

# polygon1 = Polygon(8,9,3)
# polygon2 = Polygon(a = 9, b= 6, t =8)
# print(polygon1.get_perimetr())
# print(polygon2.get_perimetr())


"""
Переопределение методов и атрибутов в дочерних классах

Можно наследоваться от встроенных классов

int, tuple, dict, str, set, frosenset, bool, list
"""
# class MyDict(dict):
#     def get(self,key,default = 'No key :('):
#         print('This method has been changed')
#         return dict.get(self,key,default)

# dict1 = dict(a=3, b =4, c=7)
# print(dict1.get('d'))
# dict2 = MyDict(a = 5,b=6,c=6)
# print(dict2.get('d'))

"""
Создадим класс Person и его дочерний класс Employee 
Переопределим его метод get_info() добавив к нему аттрибуты position и salary

Используем метод super() для обращения к аттрибутам и методом Родительского класса.

super - функция, которая может возвращать методы и аттрибуты родительского класса.

"""
# class Person:
#     def __init__(self, name, last_name, id_number):
#         self.name = name
#         self.lastname = last_name
#         self.id = id_number

#     def get_info(self):
#         print(f'{self.name} {self.lastname}, id: {self.id}')


# class Employee(Person):
#     def __init__(self, name, last_name, id_number, position, salary):
#         super().__init__(name, last_name, id_number)
#         self.position = position
#         self.salary = salary

#     def get_info(self):
#         super().get_info()
#         print(f'He works as {self.position} and his salary is {self.salary}')


# person = Person(name='Itachi', last_name='Uchiha',
#                     id_number='01194531343411103\n')
# person.get_info()

# employee = Employee(name='Itachi', last_name='Uchiha',
#                     id_number='01194531343411103', position='nukenin', salary="confidential")
# employee.get_info()

"""
Ещё один пример с использованием наследованием
"""
# class Art:
#     students_count = 100

# class Music(Art):
#     students_count = 50
#     def __init__(self):
#         Music.students_count +=1
#         Art.students_count += 1

# class Acting(Art):
#     atudents_count = 50
#     def __init__(self):
#         Acting.students_count+=1
#         Art.students_count +=1


# student1 = Music()
# student2 = Acting()
# student3 = Acting()
# print(Music.students_count)
# print(Acting.students_count)
# print(Art.students_count)


"""
Если в методе родительского класса мы хотим не прописывать ничего, то можем прописать pass или вызвать 
исключение NotImplementedError, чтобы переопределить этот метод
"""
# class Animal:
#     def sound(self):
#         raise NotImplementedError

# class Cat(Animal):
#     def sound(self):
#         print('Meow')

# class Dog(Animal):
#     def sound(self):
#         print('Gav-Gav')

# class Cow(Animal):
#     def sounf(self):
#         print('Mu-mu')

# # animal = Animal()
# # animal.sound()

# cat = Cat()
# cat.sound()

# dog = Dog()
# dog.sound()

"""
Начало разбора

Принципы ООП:
- наследование
- инкапсуляция
- полиморфизм

"""
# class A:
#     attr1 = 'a'

#     def method1(self):
#         print('AAA')
# class B:
#     attr1 = 'b'
#     def method1(self):
#         print('BBB')
# b1 = B()
# b1.method1()

"""
Дочерние классы могут дополнять поведение родителей

super - функция, для обращения к родительскому классу.
"""
# class A:
#     attr = 'a'

#     def method1(self):
#         print('itachi')

#     def method2(self):
#         return self.attr1.upper()

# class B(A):
#     attr = 'b'
#     def method1(self):
#         super().method1()
#         print('uchiha')

#     def method2(self):
#         value = super().method2()
#         my_value = value + 'best'
#         return my_value



# class A:
#     attr1 = 'a'

# class B(A):
#     attr1 = 'b'

# class C(B):
#     attr1 = 'c'

# class D(C):
#     attr1 = 'd'

# '''   D -> C -> B -> A    '''

# d1 = D()
# print(d1.attr1) #d

"""
Если нет нужного свойства(аттрибута), то вызовется исключение AttributeError
"""


"""
ассоциация - связь объектов разных классов
"""
# class Engine:
#     def __init__(self, fuel, volume, power):
#         self.fuel = fuel
#         self.volume = volume
#         self.power = power
    
# v8 = Engine('gasoline', 5, 350)
# v6 = Engine('diesel',3,200)

# class Car:
#     def __init__(self: str , model: str, year: int, color,engine:Engine):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.engine = engine

# car1 = Car('Toyota Land Cruser', 'S7 JXN', 2010, 'black', v5 = Engine('gasoline', 5,200))
        
"""
Пример с классом Product
"""
# class Category:
#     def __init__(self,name,id) -> None:
#         self.name = name
#         self.id = id

# cat1 = Category('электро')
# cat2 = Category('техника')

# class Product:
#     pass

# p1 = Product()
# p2 = Product()


# class User:
#     def __init__(self,email,adress,number) -> None:
#         self.email = email
#         self.adress = adress
#         self.number = number

# user1 = User('nik.000@gmail.com','Токтогуля, 197', '+99655543223')

# class Order:
#     def __init__(self,id,user,date,total_sum,products) -> None:
#         self.id = id
#         self.user = user
#         self.date = date


# order1 = Order(1,user1,'10-11-2021 18:56')

# class OrderItem:
#     def __init__(self,order_id, product,quantity):
#         self.order_id = order_id
#         self.product = product
#         self.quantity = quantity
    
# order_item1 = OrderItem(1,p1,2)
# order_item2 = OrderItem(1,p2,4)



"""
Меняем атрибутт класса
"""
# class A:
#     attr1 =5
#     def method1(self):
#         self.attr1 +=1

#     @classmethod
#     def method2(cls):
#         cls.attr1 +=1
    
# a1 = A()
# a1.method1()


"""


"""
# class A:
#     instance_count = 0

#     def __new__(cls):
#         cls.instance_count +=1
#         return super().__new__(cls)

# a1 = A()
# a2 = A()
# a3 = A()
# print(A.instance_count)


"""
1) Создайте класс Languages. В этом классе должен быть атрибут класса, который обозначает количество студентов,
изучающих какой-либо язык программирования. От класса Languages создайте два дочерних класса: Python, JavaScript. 
В них  также должны быть атрибуты, указывающие на количество студентов, изучающих тот или иной язык. 
При создании объекта-студента от одного из дочерних классов, автоматически количество студентов в классах меняется. 
Если студент изучает язык Python, то количество студентов должно увеличиться на один и в классе Python и в классе Languages. 
Аналогично со студентами JavaScript. Далее, в дочерних классах должен быть переопределен метод coding, в классе Python 
он должен выдавать вам строку “I am Python student. I am coding now.”, 
а в классе JavaScript - “I am JavaScript student. I am coding now”. Создайте двух студентов от двух дочерних классов. 
Далее программа сама рандомно выбирает студента и предлагает вам угадать, 
какого студента она выбрала. После вашего выбора, он вызывает метод coding у загаданного студента и выдает вам 
результат: если вы отгадали правильно, пишет “Good job!”, если нет - “No bueno :(”
"""
# # писать код здесь
# class Languages:
#   students_num = 0
#   def __init__(self):
#     Languages.students_num+=1

# class Python:
#   students_num = 0
#   def __init__(self):
#     Python.students_num +=1
#     Languages.students_num +=1
#   def coding(self):
#     print('I am Python student. I am coding now')
  
# class JavaScript:
#   students_num = 0
#   def __init(self):
#     JavaScript.students_num +=1
#     Languages.students_num +=1
#   def coding(self):
#     print('I am JavaScript student. I am coding now')
  
# student1 = Python()
# student2 = JavaScript()

"""
2) Создайте свой класс MyList, который наследуется от list. 
Переопределите метод списка insert(), который обычно принимает первым аргументом индекс, а вторым - элемент. 
В своем классе MyList переопределите этот метод так, чтобы он принимал аргументы  в обратном порядке: первым - элемент, 
вторым - индекс
"""
# писать код здесь
# class MyList(list):
#     def insert(self,element,index):
#         element,index = index, element
#         return list.insert(index,element)

# new_list = MyList(['s','srt','sertf','sdrf','drr'])
# new_list.insert('d',2)

"""
Task
Таски

1.Создайте класс Class1 с 2 методами - first и second.

Создайте второй класс Class2, который наследуется от Class1, и 
определите в новом классе Class2 ещё 2 метода - third и fourth.

Создайте экземпляр obj от класса Class2 и вызовите у него все четыре метода.

внутри методов прописывать и возвращать ничего не нужно, можно просто оставить ключевое слово pass. 
pass говорит Python что функция пока ничего не выполняет, но в будущем возможно вы вернетесь и допишите туда код.

"""
# class Class1:
#     def first(self):
#         pass
#     def second(self):
#         pass

# class Class2(Class1):
#     def third(self):
#         pass
#     def fourth(self):
#         pass

# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()

"""
2.Создайте класс A и определите в нём метод method1, который будет печатать строку

Основной функционал.
Затем создайте второй класс B, который наследуется от класса A.

Внутри класса B переопределите method1 таким образом, чтобы он помимо строки "Основной функционал", также печатал строку

Дополнительный функционал.
Объявите экземпляр класса B и вызовите метод method1. Результат в терминале должен быть:

Основной функционал 
Дополнительный функционал 
"""
# class A:
#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()

"""
3.Создайте класс MyString, который будет наследоваться от str.
Определите 2 своих метода:
- append, который будет принимать строку и добавлять её в конец исходной
- pop, который удаляет из строки последний элемент и возвращает его.

Затем, создайте экземпляр example от класса MyString со значением String. 
Добавьте к example строку 'hello' методом append, затем примените метод pop.
Пример:
example = MyString('String') 
example.append('hello') 
print(example) 
Вывод в терминал будет:
Stringhello 
Применим метод pop() к объекту example:
print(example.pop()) 
print(example) 
cам метод возвратит нам удаленную строку, в терминале получим:
o 
Stringhell 
"""
# class MyString(str):
#     def __init__(self, string):
#         self.string = string

#     def append(self,stri):
#         self.string = self.string + stri
        

#     def pop(self):
#         poped = self.string[-1]
#         self.string = self.string[:-1]
#         return poped
    
#     def __str__(self):
#         return self.string

# example = MyString('String')
# example.append('hello')
# print(example)
# print(example.pop()) 
# print(example) 

"""
4.Создайте класс MyDict который будет наследоваться от встроенного класса dict. 
Переопределите метод get() таким образом, чтобы при попытке получения несуществующего ключа, по умолчанию он возвращал, 
вместо None, строку:

Are you kidding?
Создайте экземпляр класса в переменной 'obj_dict' и попробуйте получить несуществующий ключ методом get().

Например:

obj_dict = MyDict({'some_title': 2}) 
print(obj_dict.get('some')) 
Ключа 'some' в нашем словаре нет, есть только 'some_title', в терминале получим:

Are you kidding? 
Метод get имеет такой синтаксис: словарь.get(ключ, значение), в значение передается 
то что вы хотите возвратить если такого ключа не существует. По умолчанию, если второе значение не передано, 
метод возвращает None. Для переопределения метода унаследуйте метод от родителя и передайте в метод свое значение
"""

# class MyDict(dict):
#     def get(self,key,default = 'Are you kidding?'):
#         return dict.get(self,key,default)

# obj_dict = MyDict({0:'string'})
# print(obj_dict.get(0))

"""
5.Создайте класс Person который будет описывать человека, а точнее его имя - name и возраст - age. 
Добавьте к классу метод display(), который будет выводить данные об этом человеке.

Создайте второй класс Student, который будет наследоваться от класса Person.

Объекты от класса Student должны иметь все атрибуты, которые были определены в родительском классе и 
еще один дополнительный атрибут - faculty, который будет описывать факультет, где учится студент.

Создайте метод display_student(), который будет выводить данные об этом студенте.

Создайте от класса Student объект в перемнной obj_student, и выведите данные о нём, как о человеке, 
затем как о студенте.

Например, применим методы к объекту obj_student:

obj_student.display() 
obj_student.display_student() 
допустим, у нашего объекта в атрибуте name хранится значение Rick, в age - 21, а в faculty значение science, 
вывод в терминал должен быть:

name:Rick, age:21 
name:Rick, age:21, faculty:science 

"""
# class Person:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def display(self):
#         print(f'name:{self.name}, age:{self.age}')

# class Student(Person):

#     def __init__(self, name, age,faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')

# obj_student = Person(name = 'Rick', age = 21)
# obj_student = Student(name = 'Rick', age = 21,faculty='science')
# obj_student.display() 
# obj_student.display_student() 

"""
6.Создайте класс ContactList, который должен наследоваться от встроенного класса list.

В вашем классе должен быть реализован метод search_by_name, который должен принимать имя и 
возвращать список всех совпадений.

Создайте экземпляр класса в переменной all_contacts и передайте список ваших контактов.

Примерный ввод:

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya')) 
Метод search_by_name возвращает все строки содержащие подстроку "Olya":

['Ivan Olya', 'Olya Ivan'] 
"""
# class ContactList(list):
#     def __init__(self,list_):
#         self.list_ = list_
#     def search_by_name(self,name):
#         res = [i for i in self.list_ if name in i]
#         return res

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
# print(all_contacts.search_by_name('Olya'))

"""
7.Создайте класс Smartphones, экземпляры класса должны иметь такие свойства:

name - название
color - цвет
memory - память
battery - процент заряда батареи
Значение battery по умолчанию должно быть 0.

Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона.

У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.

Создайте два дочерних класса от Smartphones:

Iphone - с дополнительным аттрибутом экземпляра - ios и методом send_imessage(принимает в аргументы строку и возвращает эту строку и от какого телефона сообщение было выслано в таком формате - sending 'ваша строка' from 'название объекта-телефона')

Samsung - с дополнительным аттрибутом android и методом show_time(который показывает текущее время)

Создайте объекты phone, iphone7, samsung21 от классов SmartPhones, Iphone, Samsung и примените все методы.

Для правильной работы тестов, проделайте все следующие операции:

создайте объект от класса SmartPhones:

phone = SmartPhones('generic', 'blue', '128GB') 
print(phone) 
вывод:

generic 128GB
распечатайте свойство батарейки,затем примените метод charge(), зарядив телефон до 20%:

print(phone.battery) 
phone.charge(20) 
print(phone.battery) 
получим в терминале:

0 
20 
создайте объект от класс Iphone, распечатайте этот объект, и примените метод send_imessage:

iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello')) 
вывод будет:

Iphone 7 128gb 
sending hello from Iphone 7 128gb 
создайте объект от Samsung и примените метод show_time():

samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time()) 
вывод будет:

18:37:02.712036 
"""
# import datetime
# class SmartPhones:
#     def __init__(self,name,color,memory) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0
#     def __str__(self) :
#         return f'{self.name} {self.memory}'
#     def charge(self,battery_charge):
#         self.battery += battery_charge
#         return self.battery
    
# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory,ios) -> None:
#         super().__init__(name, color, memory)
#         self.ios = ios
#     def send_imessage(self,string):
#         return f"sending {string} from {self.name} {self.memory}"


# class Samsung(SmartPhones):
#     def __init__(self, name, color, memory,android) -> None:
#         super().__init__(name, color, memory)
#         self.ios = android
#     def show_time(self):
#         return datetime.datetime.now().time()

# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 

# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello')) 

# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time()) 


"""
8.Напишите класс CustomError который наследуется от встроенного класса исключений Exception.

Переопределите __init__ таким образом чтобы через экземпляр класса можно было передавать сообщение и 
создавать новые виды исключений.

Создайте исключение от этого класса в переменной capitals_error с сообщением:

ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ

Напишите функцию check_letters(вне класса, отдельно от класса), проверяющую строки на регистр и если строка 
не написана в верхнем регистре выбросите исключение созданное классом CustomError:

Traceback (most recent call last):
  File "inheritance.py", line 121, in <module>
    check_letters(a)
File "inheritance.py", line 117, in check_letters
    raise capitals_error
main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ 
Если же все хорошо необходимо вывести сообщение: ВСЕ ОТЛИЧНО! {ваша строка}.

Например:

print(check_letters("HELLO")) 
Вывод будет:

ВСЕ ОТЛИЧНО! HELLO 
Если мы применим функцию к этой строке:

print(check_letters("hello")) 
Получим исключение от нашего класса CustomError:

Traceback (most recent call last): 
 File "inheritance.py", line 121, in <module> 
     check_letters(a) 
 File "inheritance.py", line 117, in check_letters 
     raise capitals_error 
__main__.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ 
"""
# class CustomError(BaseException):
#     def __init__(self,error_name):
#         self.error_name = error_name

# def check_letters(letters):
#     if not letters == letters.upper():
#         raise capitals_error
#     else:
#         return f'ВСЕ ОТЛИЧНО! {letters}'

# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
# print(check_letters("HELLO")) 

