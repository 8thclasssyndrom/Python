"""
День 3. Неделя 5.
Тема: Введение в ООП

ООП(Объектно-ориентрированное программирование или парадигма) - подход(парадигма), в котором чати программы выражатся 
в виде объектов.

Объект описываются классами:
 
class A:
  pass

Основные понятия ООП:
- класс
- объекты класса
- принципы ООП(наследование, инкапсуляция, полиморфизм)

Объектно-ориентированная парадигма имеет несколько принципов:

- Данные структурируются в виде объектов, каждый из которых имеет определенный тип, то есть принадлежит к какому-либо классу.
- Классы – результат формализации решаемой задачи, выделения главных ее аспектов.
- Внутри объекта инкапсулируется логика работы с относящейся к нему информацией.
- Объекты в программе взаимодействуют друг с другом, обмениваются запросами и ответами.
- При этом объекты одного типа сходным образом отвечают на одни и те же запросы.
- Объекты могут организовываться в более сложные структуры, например, включать другие объекты или наследовать от одного или нескольких объектов.

class SomeClass(object):
  # поля и методы класса SomeClass

class SomeClass(ParentClass1, ParentClass2, …):
  # поля и методы класса SomeClass

Атрибут класса относится ко всем объектам класса. 
Атрибут экземпляра класса относится только к данному объекту.

"""

"""
Создание базового класса
"""
# class SomeClass:
#     pass

"""
Проверим относится объект к объектам класса методом isinstance(object, class)
"""
# class A:
#     #свойства
#     pass

# a = A()
# # print(isinstance(a,A)) #True
# print(type(a)) #<class '__main__.A'>
"""
Встроенные классы:
int,str,list,tuple,dict,bool,set,frozenset and e.t.c

Все они относятся к классу type
"""
# print(type(int)) #<class 'type'>

"""
Создание класса Dog

__init__  - метод инициализации, принимает только объект

Атрибуты или свойства класса одна всю функцию  вызываются .attribute

"""

# class Dog:
#   owner = "Pit" # атрибуты всего класса, относится ко всем объектам
#   def __init__(self,name,age): # метод инициализатор, принимает только объект
#     self.name = name #атрибуты, экзмепляра класса, относятся только к конкретному объекту
#     self.age = age

#   def bark(self):
#     print('Gav-gav')
  
#   def eat(cls):
#     print('Nyam-nyam')

#   def __str__(self) -> str:
#       return f'{self.name}, {self.age}'
  
#   def dog_info(self):
#     return f'This is {self.name} he is {self.age} years old.'

#   def birthday(self,cake):
#     self.age += 1
#     self.cake = cake
#     return f'{self.name} is {self.age}'

#   def friends(self,friend):
#     self.friend = friend
#     friend.friend = self



# dog1 = Dog(name = 'Rex', age =3)
# dog2 = Dog(name = 'Bob', age =2)
# dog3 = Dog(name = 'Oreo',age = 0.5)

# dog3.owner = 'Tom'

# dog1.name = 'Piter'
# dog1.food = 'meat'

''' метод name'''
# print(dog1.name) #Rex
# print(dog2.name) #Bob
'''получаем имя владельца через метод owner'''
# print(dog2.owner) #Pit
# print(dog3.owner) #Tom

# print(dog1.name) #Piter
# print(dog1.food) #meat
# print(dog2.food) #AttributeError: 'Dog' object has no attribute 'food'

'''для функции bark'''

# dog1.bark() #Gav-gav
# dog2.bark() #Gav-gav

'''для функции eat'''

# dog1.eat() #Nyam-nyam

'''для функции str'''

# print(dog1) #Rex, 3
# print(dog2) #Bob, 2

'''для функции dog_info '''

# print(dog3.dog_info()) #This is Oreo he is 0.5 years old.

'''для функции birthday'''

# print(dog3.birthday('Chocolate')) #1.5
# print(dog3.cake) #Chocolate
# print(dog1.birthday('Vanila'))  #4
# print(dog1.cake) #Vanila

'''для функции friends()'''

# dog1.friends(dog2)
# print(dog1.friend.name)  #Bob
# print(dog2.friend.name)  #Rex


"""
Class Rectangle
"""
# from typing import DefaultDict


# class Rectangle:
#   default_color = 'red'

#   def __init__(self,width,length):
#     self.width = width
#     self.length = length
  
#   def area(self):
#     return self.width * self.length


# rec1 = Rectangle(4,6)
# rec2 = Rectangle(2,7)

'''принтим площадь и стороны нашего прямоугольника'''

# print(rec1.area()) # 24
# print(rec1.width)  # 4
# print(rec2.area()) # 14
'''изменяем и принтим цвет машины'''
# rec2.default_color = 'yellow'
# print(rec2.default_color) #yellow


"""
class Car
"""
# class Car:
#   car_count = 0

#   def __init__(self):
#     Car.car_count+=1

# car1 = Car()
# car2 = Car()
# car3 = Car()
# car3 = Car()
# print(Car.car_count) #4

"""
Начало разбора
"""
# class Phone:
#   operationg_system = 'Android'
#   def __init__(self,model,size,color,ram,memory) -> None:
#       self.model = model
#       self.size = size
#       self.color = color
#       self.ram = ram
#       self.memory = memory

# phone1 = Phone('Samsung Galaxy S21',6.5,'gold',8,256)
# phone2 = Phone('Xiaomi Mi 10',5.0,'black',6,128)



# class Patient:
#   def __init__(self,name,last_name,age,weight,height):
#       pass


# class Phone:
#   model : str
#   year: int
#   ram: int
#   color: str
#   os: str

# phone = Phone('Apple Iphone 13',2021,8,'gold','IOS')


"""
Наследование - это процесс, когда из одного класса происходит другой.
"""
# class A: #родительский (базовый) класс # parent, base, inherited
#   attr1 = 'a'

#   def method(self):
#     print('Hello world')
  
# class B(A): #дочерний(производный) класс # child, derived, 
#   pass

# b1= B()
# b1.attr1
# b1.method()

"""
Дочерний класс может определять свои свойства
"""
# class A:
#   attr1 = 'a'

# class B(A):
#   attr2 = 'b'
#   attr3 = 'c'

# b1 = B()
# b1.attr1
# b1.attr2
# b1.attr3


"""
Дочерний класс может переопределять свойства родителя, дополнять методы родителя.
"""
# class A:
#   attr1 = 'a'
#   attr2 = 'b'

# class B(A):
#   attr2 = 'new value for attr2'
#   attr3 = 'c'

# b1 = B()
# b1.attr2 # new value for attr2

# class A:
#   def method1(self):
#     print('Hello!!!')

# class B(A):
#   def method1(self):
#     super().method1()
#     print('BBBB')
  
# b1 = B
# b1.method1()



"""
Classwork
Классная работа
"""
"""
1) Напишите программу по следующему описанию. Есть класс "Снайпер". От него создаются два экземпляра. 
Каждому устанавливается здоровье в 100 очков. В случайном порядке они стреляют друг в друга. 
Тот, кто стреляет, здоровья не теряет. У того, в кого стреляют, оно уменьшается на 20 очков от одного выстрела. 
После каждого выстрела надо выводить сообщение, какой снайпер атаковал, и сколько у противника осталось здоровья. 
Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
"""
# писать код здесь

# class Snaiper:
#   def __init__(self,name):
#     self.name = name
#     self.health = 100
  
#   def shoot(self,snaiper):
#     snaiper.health -=20

      
# snaiper1 = Snaiper(name = 'John')
# snaiper2 = Snaiper(name = 'Tim')

# import random

# choices = (snaiper1,snaiper2)

# while True:
#   shooter = random.choice(choices)
#   if shooter == snaiper1:
#     shot = snaiper2
#   else:
#     shot = snaiper1
  
#   shooter.shoot(shot)
#   print(f'Shooter {shooter.name} is shooting, {shot.name} has {shot.health} health points')

#   if snaiper1.health == 0:
#     print(f'{snaiper1.name} dead. {snaiper2.name} won')
#     break
#   elif snaiper2.health == 0:
#     print(f'{snaiper2.name} dead. {snaiper1.name} won')
#     break
#   else:
#     continue
  

"""
2) Напишите программу по следующему описанию. Есть класс Hogwarts. В нем определены следующие атрибуты-факультеты: 
Gryffindor, Ravenclaw, Hufflepuff, Slytherin. От класса Hogwarts создаются объекты-студенты. 
При создании студентов необходимо указать баллы за их следующие качества: courage (храбрость), intelligence (интеллект), 
justice (справедливость), ambition (амбиции). У студентов не могут быть качества одинакового уровня. 
В зависимости от того, какое качество студента преобладает, метод sorting_hat будет распределять студента в один из 
факультетов и выдавать в какой факультет поступил студент.

Примечание: 
Преобладает courage -> Gryffindor
Преобладает intelligence -> Ravenclaw
Преобладает justice -> Hufflepuff
Преобладает ambition -> Slytherin
"""
# писать код здесь

# class Hogwarts:
#     def __init__(self,courage,intelligience,justice,ambition):
#         self.courage = courage
#         self.intelligience = intelligience
#         self.justice = justice
#         self.ambition = ambition

#     def sorting_hat(self):
#         list_of_characteristics = [self.courage,self.intelligience,self.justice,self.ambition]
#         if max(list_of_characteristics) == self.courage:
#             return 'Ваш факультет Гриффиндор'
#         elif max(list_of_characteristics) == self.intelligience:
#             return 'Ваш факультет Когтевран'
#         elif max(list_of_characteristics) == self.justice:
#             return 'Ваш факультет Хаффлпафф'
#         elif max(list_of_characteristics) == self.ambition:
#             return 'Ваш факультет Слизерин ;)'

# print('Введите оценку ваших качеств по шкале от 1 до 100')
# student1 = Hogwarts(courage = int(input('Введите оценку вашей храбрости: ')), 
#             intelligience =  int(input('Введите оценку вашего ум: ')), 
#             justice = int(input("Введите оценку вашей справедливость: ")), 
#             ambition = int(input("Введите оценку вашей амбициозности: ")))

# print(student1.sorting_hat())
  
  


"""
Task
Таски


1.Создайте класс для песен Song. Каждая песня имеет название - title, автора - author и год выпуска - year.

Добавьте три метода:

show_author

show_title

show_year

выводящие утверждения о каждом атрибуте экземпляра класса Song.

Создайте экземпляр song класса Song с вашей любимой песней и примените все методы.

Например:

song.show_title()
song.show_author()
song.show_year()
Вывод:

Название этой песни Happy
Автор этой песни Pharrell Williams
Эта песня вышла в 2013 году
"""
# class Song:
#   def __init__(self,title,author,year):
#       self.title = title
#       self.author = author
#       self.year = year
#   def show_title(self):
#       print(f'Название этой песни {self.title}')
 
#   def show_author(self):
#       print(f'Автор этой песни {self.author}')
  
#   def show_year(self):
#       print(f'Эта песня вышла в {self.year} году')
        
# song = Song(title = 'Between the bars',author = 'Elliot Smith',year = '1997')

# song.show_title()
# song.show_author()
# song.show_year()

"""
2.Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14).

Экземпляры класса Circle в свою очередь должны иметь обязательное свойство - радиус.

К примеру, создадим объект с радиусом 2:

circle1 = Circle(2) 
Также, класс должен иметь метод расчета площади круга - get_area():

circle1.get_area() 
Возвращает:

12.56 
формула расчета площади: число Пи умножить на радиус в квадрате

Создайте экземпляр класса, переопределите цвет экземпляра и примените метод get_area().

Распечатывать результат не нужно, методы должны возвращать результат ключевым словом return.
"""
# class Circle:
#   color = 'Синий'
#   pi = 3.14

#   def __init__(self,radius):
#       self.radius = radius
#   def get_area(self):
#     square = (self.radius**2)*Circle.pi
#     return square
  
# circle = Circle(radius = 2) 
# circle.color = 'white'

"""
3.Создайте класс BankAccount, у объектов данного класса есть аттрибут balance со значением по умолчанию 0: balance = 0.

Определите метод withdraw с параметром amount, который будет отнимать сумму от баланса и возвращать текущий баланс.

Добавьте еще один метод deposit, который также имеет параметр amount и соответсвенно добавляет сумму к балансу и 
возвращает баланс.

Например:

account.deposit(1000) 
account.withdraw(500) 
Получим такой вывод:

Ваш баланс: 1000 сом 
Ваш баланс: 500 сом 
в начале, увеличили переменную balance на 1000, затем уменьшили на 500, и получили в итоге 500.
"""

# class BankAccount:
#   balance = 0
#   def __init__(self,amount = 0):
#     self.balance = amount
  
#   def withdraw(self,amount):
#     self.balance  -= amount
#     print(f'Ваш баланс: {self.balance} сом')
  
#   def deposit(self,amount):
#     self.balance  += amount
#     print(f'Ваш баланс: {self.balance} сом')

# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500)

"""
4.Создайте класс Taxi, объекты которого имеют такие атрибуты как 
название компании - name, стоимость посадки - cost, стоимость за каждый пройденный километр - cost_km.

Добавьте к классу метод get_total_cost, принимающий 
параметр km - сколько километров составила поездка и возвращающий стоимость поездки.

Создайте три экземпляра класса Taxi для 
трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждой из них.

Например:

print(taxi1.get_total_cost(10)) 
print(taxi2.get_total_cost(6)) 
print(taxi3.get_total_cost(14))  
Вывод:

Такси Namba, стоимость поездки: 179 сом 
Такси Yandex, стоимость поездки: 127 сом 
Такси Jorgo, стоимость поездки: 238 сом  
"""
# class Taxi:
#     def __init__(self,name: str,cost: int,cost_km: int):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self,km):
#         taxi_name = self.name
#         full_cost = (self.cost_km* km) + self.cost
#         return f'Такси {taxi_name}, стоимость поездки: {full_cost} сом'
    
# taxi1 = Taxi('Namba', 17, 9)
# taxi2 = Taxi('Yandex', 20, 7)
# taxi3 = Taxi('Jorgo', 17, 0)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))  

"""
5.Создайте класс телефонной книги Phone. У контактов должны быть такие аттрибуты:

name - имена
last_name - фамилии
phone - телефонные номера
Добавьте метод get_info, который выводит информацию о контакте в следующем виде:

contact.get_info()
Вывод в терминал:

Контакт: John Snow, телефон: +996707707707
Затем, создайте объект от класса Phone в переменной contact и примените метод get_info.
"""
# class Phone:
#     def __init__(self,name,last_name,phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
    
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

# contact = Phone(name = 'John',last_name = 'Snow',phone ='+996707707707')
# contact.get_info()


"""
6.Напишите класс Salary для расчета налогов на заработную плату. 
У класса должна быть обязательная переменная класса - percent = 8, 
обозначающий процент налога на ежемесячную зарплату - 8%.

Объекты класса должны иметь, в качестве атрибутов сумму зарплаты salary и 
стаж работы в месяцах - experience.

Также у класса должен быть метод count_percent, расчитывающий сумму налога заплаченного 
за весь стаж работы.

Создайте экземпляр класса obj и посчитайте сумму вашего налога.

К примеру, если у вашего объекта salary имеет значение 10000, а experience равен 10, то:

print(obj.count_percent()) 
Выдаст вам такой результат в терминале:

8000.0 
Каждый месяц с зарплаты в 10000 сомов снимается 8% на налоги, т.е 800 сом, за 10 месяцев 
трудового стажа эта сумма будет 8000.0 сом
"""
# class Salary:
#     percent = 8
#     def __init__(self,salary,experience):
#         self.salary = salary
#         self.experience = experience
#     def count_percent(self):
#         return (self.salary*(self.percent/100))*self.experience
    

# obj = Salary(10000,10)
# print(obj.count_percent()) 

"""
7.Вам дан такой код:

winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
print(winner1.category, winner1.year, winner1.winner) 
print(winner1.get_year())

  
winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
print(winner2.category, winner2.year, winner2.winner) 
print(winner2.get_year())
который выводит в терминал такие значения:

Литература 1971 Пабло Неруда
выиграл 50 лет назад 
Литература 1994 Кэндзабуро Оэ 
выиграл 27 лет назад
Напишите класс Nobel и метод класса get_year() таким образом, 
чтобы данный вам код вывел указанные значения в терминале.

Дату сколько лет назад была получена премия в методе get_year() 
не вписывать вручную, а высчитывать используя datetime
"""
# class Nobel:
#     def __init__(self,category,year,winner):
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):
#         from datetime import datetime
#         return f'выиграл {datetime.now().year - self.year} лет назад'


# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

"""
8.Создайте класс Password, экземеплярами класса являются пароли в виде строк. 
У класса должен быть метод validate для валидации пароля:

В начале, проверьте, что пароль состоит из минимум 8 символов, но меньше 15

Вторая проверка должна проверять что пароль содержит цифры

Третья проверка проверяет содержит ли пароль буквы

В конце проверьте, содержит ли пароль хотя бы один из символов:

'@', '#', '&', '$', '%', '!', '~', '*'

если одно из условий не выполнено, выводите свое исключение, если же все условия выполнены 
метод validate должен возвращать строку:

Ваш пароль сохранен.
Также переопределите метод __str__, чтобы при попытке распечатать сам пароль, вам выдавалась 
строка из звездочек количество которых равно длине пароля.

К примеру, если пароль joe@123456, при попытке распечатать пароль, в терминал должно выводиться: **********

пишите код для проверки пароля в указанном порядке
"""
# class Password:
#     def __init__(self,password):
#         self.password = password
#     def validate(self):
#         if not len(self.password)>=8 and not len(self.password)<=15:
#             raise ValueError('Password should be longer than 8, and less than 15')
#         check1 = [i for i in self.password if i.isdigit()]
#         if check1 == []:
#             raise ValueError('Password should contain digit')
#         check2 = [i for i in self.password if i.isalpha()]
#         if check2 == []:
#             raise ValueError('Password should contain letter')
#         symbols = ['@', '#', '&', '$', '%', '!', '~', '*']
#         check3 = [i for i in self.password if i in symbols]
#         if check3 == []:
#             raise ValueError('Password should contain symbol')
          
#         print('Ваш пароль сохранен')
      
#     def __str__(self):
#         new_password = len(self.password)*'*'
#         return new_password

      
# password1 = Password('joe@123456')
# password1.validate()
# print(password1)

"""
9.Создайте класс Math, экземпляром которого должно быть число. У классa Math должно быть 3 метода:

get_factorial - возвращает факториал числа(перемножить все составные числа до самого числа)

get_sum - возвращает сумму цифр числа

get_mul_table - возвращает таблицу умножения для числа до 10 в формате:

5x1=5
5x2=10
.....

Создайте экземпляр класса и примените к нему все методы.

Например, если экземпляром класса Math является число 11,

вызов get_factorial возвратит такой результат:

39916800 
т.к 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10 x 11 = 39916800

метод get_sum, возвратит:

2 
т.к число 11 состоит из двух цифр 1 и 1, сумма 1 + 1 = 2

метод get_mul_table возвратит:

11 x 1 = 11 
11 x 2 = 22 
11 x 3 = 33 
11 x 4 = 44 
11 x 5 = 55 
11 x 6 = 66 
11 x 7 = 77 
11 x 8 = 88 
11 x 9 = 99 
11 x 10 = 110 
результат методов возвращайте ключевым словом return, print() использовать не надо.
"""
# class Math:
#     def __init__(self,num):
#         self.num = num
#     def get_factorial(self):
#         res =1
#         for n in range(1,self.num+1):
#             res*=n
#         return res
#     def get_sum(self):
#         list_num = list(map(int,str(self.num)))
#         resu = sum(list_num)
#         return resu
#     def get_mul_table(self):
#         res = ''
#         for i in range(1,11):
#             res +=f'{self.num}x{i}={self.num*i}\n'
#         return res
      
# a = Math(2)
# print(a.get_factorial())
# print(a.get_sum())
# print(a.get_mul_table())

"""
10.Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в кино, сделать домашку, 
выгулять собаку и.т.д).

У класса должна быть переменная класса instances значением которой является пустой словарь.

Создайте внутри класса метод give_priority, который имеет параметр priority, куда принимает число - 
приоритет вашей задачи (1, 2, 3) и записывает вашу задачу в словарь instances с ключом в виде числа - priority, 
а значением в виде вашей задачи.

Например:

{3: 'сходить в кино'}
приоритет сходить в кино у вас не самый высокий.

{1: 'сделать домашку'}
в этом случае это у вас самая важная задача, с приоритетом 1.

При каждом вызове метода give_priority - словарь в instances обновляется. Если вы создали три объекта от класса ToDo и к каждому объекту вызвали метод give_priority и дали приоритет, 
то ваш словарь в instances в конце будет выглядеть примерно так:

{3: 'сходить в кино', 1: 'сделать домашку', 2: 'выгулять собаку'} 
У класса должен быть метод list_of_tasks, который возвращает вам список отсортированных задач по приоритету:

[(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]
"""
# class ToDo:
#   instances = dict()
#   def __init__(self,task):
#     self.task = task
  
#   def give_priority(self,priority):
#     self.instances[priority] = self.task
  
#   def list_of_tasks(self):
#     tasks =[(key,value) for key,value in self.instances.items()]
    
#     def get_priority(to_do):
#       return to_do[0]
    
#     tasks.sort(key = get_priority)
#     print(tasks)


# to_do1 = ToDo('сходить в кино')
# to_do1.give_priority(3)
# to_do1.list_of_tasks()

# to_do2 = ToDo('выгулять собаку')
# to_do2.give_priority(2)
# to_do2.list_of_tasks()


# to_do3 = ToDo('сделать домашку')
# to_do3.give_priority(1)
# to_do3.list_of_tasks()
