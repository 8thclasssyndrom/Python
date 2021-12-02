"""
День 4. Неделя 6.
Тема: Магические методы

Магические методы обрамлены двумя нижними подчеркиваниями

Магические, потому что мы не задумываемся, что происходит под капотом.

__new__ - конструктор, срабатывает до метода __init__

Метод  __init__ - инициализатор, принимает все аргументы, переданные в конструкторе.




Использование функции dir()
"""
# class X:
#     pass

# obj = X()
# # print(dir(obj))
# # print(dir(6))
# # print(dir('makers'))
# def func():
#     pass

# print(dir(func))

"""
1) __init__()
Все магические методы вызываются автоматически
"""
# class User:
#     def __init__(self,**kwargs):
#         print('Object is initializing .....')
#         self.name = kwargs['name']
#         self.surname = kwargs['last_name']
#         print('Object is initialized')

# user = User(name = 'Linis', last_name = 'Torvalds')
# print(user.name)
# print(user.surname)


"""
2) __new__ - конструктор, который отвечает за то, что создание экземпляра класса.
Срабатывает раньше, чем __init__
"""
# class Human(object):
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         instance = super().__new__(cls)
#         instance.heart = '4хкамерное'
#         print(human.heart)
#         print('Object created')
#         return instance

#     def __init__(self, name, last_name) -> None:
#         print('Object is inializing ...')
#         self.name = name
#         self.familia = last_name

# human = Human(name = 'Linus', last_name = 'Torvald')


"""
Singleton - от одного классса можно создать только один объект.
"""
# class Sun:
#     instance = None

#     def __new__(cls):
#         if not cls.instance:
#             cls.instance == object.__new__(cls)
#         return cls.instance

# sun1 = Sun()
# sun2 = Sun()
# sun3 = Sun()
# print(sun1 is sun2)
# print(id(sun1))
# print(id(sun2))

"""
3.__str__ 
"""
# class Human:
#     def __init__(self,name,last_name):
#         self.last_name = last_name
#         self.name = name

#     def __str__(self):
#         return f"{self.name} {self.last_name}"

# human1 = Human('Linus','Torvalds')
# print(human1)
# a = str(human1)
# print(a)

"""
4) __repr__() - больше используется для разработчиков
и вызывается, просто через имя экземпляра, а str через print

"""
# class Human:
#     def __init__(self,name,last_name):
#         self.last_name = last_name
#         self.name = name

#     def __repr__(self):
#         return f"{self.name} {self.last_name}"

# human1 = Human('Linus','Torvalds')
# print(human1)

"""
Числовые dunder методы


__add__(self, other) --> +
__sub__(self, other) --> -
__mul__(self, other) --> *
__truediv__(self, other) --> /
__mod__(self, other) --> %


"""
# class MyInt(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self,other):
#         #self.value + other
#         print('This is my addition')
#         return self.value + other

#     def __sub__(self,other):
#         #self.value - other
#         return self.value - other +100


#     def __mul__(self,other):
#         #self.value * other
#         return self.value * other - 1

#     def __truediv__(self, other):
#         return self.value / other +1


#     def __mod__(self, other):
#         return f'Остаток от деления {self.value % other}'

#     def __radd__(self,other):
#         # other + self.value
#         print('This is my r-addition')
#         return other + self.value

#     def __rsub__(self, other):
#         return other - self.value/2

#     def __rmul__(self, other):
#         print('This is my r-multiplication')
#         return other * self.value + 5


#     def __iadd__(self, other):
#         print('Это мое i-addition ')
#         return self.value + other


# '''
# Отражённые арифметические операторы
# self.value + other, self.value - other
# other + self.value, other - self.value
# Пример: __radd__, __rmul__ and etc

# Составное присваивание - a+=8

# '''

# a = MyInt(10)
# print(a + 5)
# print(a -101)
# print(a*3)
# print(a/4)
# print(a%8)

# b = MyInt(5)
# b+=7
# print(b)

"""
Магические методы:

__eq__ --> ==
__ne__ --> !=
__gt__ --> >
__lt__ --> <
__le__ --> <==
__ge__ --> >=

"""
# from os import name


# class Human:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def __eq__(self, other):
#         print('Ages are ==== :')
#         return self.age == other.age

#     def __ne__(self,other):
#         print('Ages are !=  :')
#         return self.age != other.age

#     def __gt__(self, other):
#         print('Ages are > :  ')
#         return len(self.name)  > len(other.name)


# human1 = Human(name = 'Tom', surname ='Levi',age = 19)
# human2 = Human(name = 'Jojn',surname ='Snow',age = 23)
# # print(human1 == human2)
# # print(human1 > human2)

"""
__getattr__ -  аттрибут, который вы пытаетесь достать не существует.
__setattr__ - когда мы пытаемся изменить значение нашего аттрибута.
__delattr__ - удаляет аттрибут

__getattribute__ - если


"""
# class MyClass:
#       def __init__(self):
#             self.name = 'Makers'
#             self.last_name = 'Bootcamp'
#             # print(self.__dict__)

#       def __getattr__(self,item): #обращаемся к ключам словаря, для получения их значений. item - название ключа
#             print(self.__dict__)
#             return self.__dict__.get(item, 'Hello world')

#       def __getattribute__(self, item): #получаем бесконечную рекурсию
#             print('This is custom getattibute method')
#             return self.__dict__.get(item,0)
            
#       def __setattr__(self, item,value): #self.item = value
#             print(f"I want ot set attribute {item} with {value} ")
#             self.__dict__[item] = value

#       def __delattr__(self, item): #del self.item 
#             print(f'I want to delete attribute named {item}')
#             self.__dict__.pop(item, 0)            


# obj = MyClass()
# # print(obj.age)
# obj.age = 2
# del obj.age
"""
__len__(self) --> len()
__getitem__(self, key) --> self.key
__setitem(self, key, value) -> self.key = value
__delitem__(self, key) --> del self[key]
__contains__(self, item) --> item in self or item not in self ---> True or False


"""
# class MyClass(dict):
#       def __getitem__(self,key):
#             print(f"I am giving you a value of {key} and adding it 4")
#             result = super().__getitem__(key) + 4
#             return result
      
#       def __setitem(self, key, value):
#             value += 1
#             super().__setitem__(key, value)


# dict_ = MyClass(a = 6, b = 7, c =8)

# print(dict_)
# print(dict_['a'])          


"""
Пример использования метода __contains__
"""
# class MyList(list):
#       def __init__(self, iterable):
#             self.list = iterable
      
#       def __contains__(self, item):
#             if item in self.list:
#                   return True
#             else:
#                   return False

# a = MyList([1,2,3,4,5])
# print(3 in a)



"""
Начало разбора


Магические методы нужны для того, чтобы созданные нами объекты могли работать со встроенными функциями и операциями.

- Арифметические 
- Операции сравнения 
- Приведение типа 
- Работа с последовательностями
- Вызов встроенных функций 
- Обращение к аттрибутам 


Арифметические :

+ --> __add(self,other)
self + other

__radd__(self, other)
other + self

- --> __sub__(self,other)
self - other

__rsub__(self,other)
other - self

* --> __mul__(self,other)
self * other

__rmul__(self,other)
other * other

/ --> __truediv__(self,other)
self / other

// --> __floordiv__(selt,other)
self // other

% ---> __moddiv__(self,other)
self % other

** --> __pow__(self,other)
self**other


"""
# class Balance:
#     def __init__(self,value):
#         self.value = value

#     def __add__(self, other'):
#         return self.value + other.value

# balance1 = Balance(103)
# balance2 = Balance(100)

# print(balance1 + balance2)

"""
Операции сравнения:

== --> __eq__(self,other)
!= --> __ne__(self,other)
>  --> __gt__(self,other)
<  --> __lt__(self,other)
>= --> __ge__(self,other)
<= --> __le__(self,other)

"""
# a = 5
# b = 3

# a > b  # True


# class Forbes:
#     def __init__(self, name, capital):
#         self.name = name
#         self.capital = capital

#     def __gt__(self, other):
#         return self.capital > other.capital

#     def __lt__(self, other):
#         return self.capital < other.capital

#     def __ne__(self, other):
#         return self.capital != other.capital

#     def __le__(self,other):
#         return self.capital <= other.capital

#     def __ge__(self, other):
#         return self.capital >= other.capital

# mark = Forbes('Mark Zuckerberg', 200)
# jeff = Forbes('Jeff Bezos', 240)

# print(mark > jeff) #False
# print(mark < jeff) # True
# print(mark != jeff) #True
# print( mark >= jeff) # False
# print(mark <= jeff) #True


"""
Приведение типа:

str(obj) ---> obj.__str__()
int(obj) ---> obj.__int__()
bool(obj) ---> obj.__bool__()

Работа с последовательностями:

a = [1,2,3,4]
b = {'a' : 1, 'b': 2}

# доступ к элементам

a[0] ---> a.__getitem__(0)
b['a'] --> b.__getitem__('a')

#замена элементов

a[0] = 5 ---> a.__setitem__(0, 5)
b['a'] = 22 ---> b.__setitem('a', 22)

#удаление элементов

del a[0] ---> a.__delitem__(0)
del b['b'] ---> b.__delitem__('b')

#нахождение длины

len(a) ---> a.__len__()
len(b) ---> b.__len__()

#проверка на вхождение

value in a: ---> a.__contains__(value)

key in b: b.__contains__(key)


#итерация
for x in a --> a.__iter__()
iter(a) ---> a.__iter()

#reversed

reversed(a) ---> a.__reversed__()

Вызов встроенных функций :
print(obj) --> obj.__str__()
repr(obj) ---> obj.__repr__()


Обращение к аттрибутам :
                                                                                                                                     
"""
# class MyClass:
#     attr1 = 'a'

# obj1 = MyClass()


"""
obj1.attr1 ---> obj1.__getattribute__('atrr1')
obj1.attr1 = 'new_value' ---> obj1.__setattr__('attr1','new_value')
del obj1.attr1 ----> obj1.__delattr__('attr1')

setattr(), delattr(), getattr()

setattr(obj1, 'attr1', 'new_value'), delattr(obj1, 'attr1'),
getattr(obj1, 'attr1'), hasttr(obj1, 'attr1')
"""
# class A:
#     attr1 = 'a'

# a1 = A()
# a1.attr2 = 100
# print(getattr(a1, 'attr2'))
# print(hasattr(a1, 'attr2'))

# a2 = A()


"""


"""

"""


"""

"""


"""

"""
Task
Таски
1.Создайте класс Account и переопределите в нем методы __init__, __repr__, __str__ и __del__.

Объекты класса должны содержать атрибуты:

name - имени держателя счета
balance - баланса
city - города, где открыт счет
Переопределенные методы:

__init__ должен также выводить сообщение "Счет создан"
__repr__ должен возвращать имя держателя счета и баланс
__str__ должен возвращать сообщение 'Hello' и также информацию о держателе счета: "Hello 'name' 'balance' 'city'" где вместо 'name', 'balance' и 'city' должны быть соответствующие значения атрибутов объекта.
__del__ должен выводить сообщение "Пока"
Создайте обьект класса obj_account с параметрами ('Rick', 2013, 'Bishkek') и вызовите все методы.

Ввод должен быть:

obj_account = Account("Rick", 2013, 'Bishkek')  
print(obj_account)  
print(repr(obj_account)) 
А вывод:

Счет создан   
Hello Rick 2013 Bishkek 
Rick 2013  
Пока 

"""

# class Account:
#     def __init__(self, name, balance, city):
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print("Счет создан")

#     def __repr__(self):
#         return f'{self.name} {self.balance}'

#     def __str__(self):
#         return f'Hello {self.name} {self.balance} {self.city}'

#     def __del__(self):
#         print("Пока")

# obj_account = Account("Rick", 2013, 'Bishkek')
# print(obj_account)
# print(repr(obj_account))

"""
2.Определите класс MyNumber который наследуется от класса int.

У экземпляра класса должен быть обязательный атрибут value.

Переопределите методы сложения, вычитания, умножения и деления для класса таким образом чтобы при использовании операторов + - * /, результат возвращался с сообщением:

"Это сложение и результат равен: x"   
      #для оперетора + 
"Это вычитание и результат равен: x"  
      #для '-'   
"Это умножение и результат равен: x"  
      #для '*' 
"Это деление и результат равен: x"  
      #для '/' 
где вместо x должен быть результат вычислений.

Создайте обьект от класса MyNumber в переменной obj_int cо значением равным 5.

Примените все операторы по порядку +,-,*,/.

Ввод должен быть:

obj_int = MyNumber(5)  
print(obj_int + 5)  
print(obj_int - 5)  
print(obj_int * 5)  
print(obj_int / 5)  
Вывод:

Это сложение и результат равен: 10  
Это вычитание и результат равен: 0  
Это умножение и результат равен: 25  
Это деление и результат равен: 1.0 

"""
# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return f'Это сложение и результат равен: {self.value + other}'

#     def __sub__(self, other):
#         return f'Это вычитание и результат равен: {self.value - other}'

#     def __mul__(self, other):
#         return f'Это умножение и результат равен: {self.value * other}'

#     def __truediv__(self, other):
#         return f'Это деление и результат равен: {self.value / other}'


# obj_int = MyNumber(5)
# print(obj_int + 5)
# print(obj_int - 5)
# print(obj_int * 5)
# print(obj_int / 5)

"""
3.Напишите класс MyList, который наследуется от list.

Сделайте так, чтобы индексация элементов начиналась с 1.

Создайте обьект obj_list и проверьте работоспособность программы.

Ввод должен быть:

obj_list = MyList([1,2,3,4,5])  
print(obj_list[1])  
А вывод:

1 

"""
# class MyList(list):
#       def __init__(self, list1):
#             self.list1 = list1
#       def __getitem__(self, a):
#             return self.list1[a-1]


# obj_list = MyList([1,2,3,4,5])
# print(obj_list[1])

"""
4.Напишите класс Student, который описывает студента.

У студента есть следующие атрибуты: имя(name), класс(class_name), и оценки(ball) по предметам в виде словаря, в следующем виде: {’math’: 100, ‘history’: 89, literature’: 88}.

Переопределите методы сравнения >, < ,>=, <= так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.

Создайте два обьекта от класса Student в переменных obj_student1 и obj_student2.

Сравните эти два объекта знаками >, < ,>=, <=, и распечатайте результат.

Ввод у вас должен быть:

obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
print(obj_student1 > obj_student2)  
print(obj_student1 < obj_student2)  
print(obj_student1 >= obj_student2)  
print(obj_student1 <= obj_student2)  
Вывод должен быть в виде строки:

> False 
< False 
>= True 
<= True 

"""
# class Student:
#     def __init__(self, name, class_name, ball):
#         self.name = name
#         self.class_name = class_name
#         self.ball = ball
#         score = {value for value in self.ball.values()}
#         self.score_num = sum(list(score)) / len(list(score))

#     def __gt__(self, other):
#         return f'> {self.score_num > other.score_num}'

#     def __lt__(self, other):
#         return f'< {self.score_num < other.score_num}'

#     def __ge__(self, other):
#         return f'>= {self.score_num >= other.score_num}'

#     def __le__(self, other):
#         return f'<= {self.score_num <= other.score_num}'


# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})
# print(obj_student1 > obj_student2)
# print(obj_student1 < obj_student2)
# print(obj_student1 >= obj_student2)
# print(obj_student1 <= obj_student2)
"""
5.Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для 
сравнения объектов класса - строк по длине(len).

Также в методе __new__ напишите условие для удаления пробелов и пустых строк в созданных словах.

Создайте обьекты word1 и word2 класса Word и сделайте сравнения.

Ввод:

word1 = Word('H  e  l  l  o')  
word2 = Word('world!')  
print(word1 > word2)  
print(word1 < word2)  
print(word1 >= word2)  
print(word1 <= word2) 
Вывод должен быть:

False  
True  
False  
True 

"""


# class Word:
#       def __new__(cls, string):
#             string = string.replace(' ', '')
#             obj = super().__new__(cls)
#             obj.string = string
#             return obj

#       def __gt__(self, other):
#             return len(self.string) > len(other.string)

#       def __lt__(self, other):
#             return len(self.string) < len(other.string)

#       def __ge__(self, other):
#             return len(self.string) >= len(other.string)

#       def __le__(self, other):
#             return len(self.string) <= len(other.string)

# word1 = Word('H  e  l  l  o')  
# word2 = Word('world!')  
# print(word1 > word2)  
# print(word1 < word2)  
# print(word1 >= word2)  
# print(word1 <= word2) 

"""
6.Создайте класс Kopilka, у экземпляров класса должны быть приватные атрибуты:

total - общее количество накопленных монет, изначально равно 0
coins список монет которые были брошены в копилку, изначально пуст - [].
Добавьте метод add_moneta, который принимает аргумент moneta, и увеличивает total на данное значение, а также добавляет 
монету в список coins.

Переопределите в классе магические методы __len__ и __getitem__ таким образом, чтобы при применении функции len к объекту 
выдавалось количество монет в списке coins, а при попытке перебора объекта класса циклом for, печатались монеты из списка.

Создайте объект obj от класса Kopilka, вызовите все методы класса, примените функцию len() и переберите объект циклом for.

Ввод должен быть:

obj = Kopilka() 
obj.add_moneta(25) 
obj.add_moneta(30)

print(len(obj) 
for i in obj: 
     print(i) 
А вывод:

2 
25 
30 

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
