"""
День 5. Неделя 6.
Тема: Класс методы.

Типы методов класса:

- class methods - методы класса
Метод класса не может изменять состояние экземпляра класса, но могут изменять состояние класса.
Вместо self принимают cls

Метод класса не может изменять состояние экземпляра объекта

- instance methods - Методы объектов(экземпляров) класса
Те самые методы, с которыми мы до этого работали и будем чаще всего использовать.
 self.method()
Методы экземпляра также могут иметь доступ к самому классу - при помощи аттрибута self.__class__

Методы объектов класса доступны через экземепляры класса, но не доступны через класс.
- static methods - данные методы не принимают self и cls, но спокойно принимает другие параметры.
Он не может изменить состояние ни объекта, ни класса.

static methods помещаются в класс, чтобы они находились в пространстве имен этого класса, т.е. для организационных целей.



Начало практики

- instance  method -> self
- class method --> @classmethod --> cls
- static method --> @staticmethod

"""

# class Makers:
#     language_choices = 'Python', 'JavaScript'

#     def __init__(self, name):
#         self.name = name

#     def instance_method(self):
#         return f"Hello, {self.name}"

#     @classmethod
#     def class_method(cls):
#         return f"Welcome to Makers! What type of language do you choose ? {cls.language_choices}"

#     @staticmethod
#     def static_method(choice):
#         return f"Great! You chose {choice} course"

# student = Makers(name = 'Lucas')
# print(student.instance_method())
# print(student.class_method())
# print(student.static_method('Python'))

# print()

# student2 = Makers('Ashly')
# print(student2.instance_method())
# print(student2.class_method())
# print(student2.static_method('JavaScript'))

"""
Использование class методы на примере класса User

В данном примере мы использовали список из пользователей и сделали из каждого элемента списка объект класса User и вывели 
о нем информацию через метод get_info()

"""
# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email

#     def get_info(self):
#         return f"{self.name}, {self.email}"

#     @classmethod
#     def add_data(cls, user_info: list):
#         name, email = user_info
#         return cls(name, email)

# list_of_users = [
#     ['Emily','emi@yahoo.com'],
#     ['Booby','bob@gmail.com'],
#     ['Jane','jane@mail.com']
# ]

# for info in list_of_users:
#     user = User.add_data(info)
#     print(user.get_info())


"""
Использование static методов на примере класса Lottery

"""
# class Lottery:
#     def __init__(self,name):
#         self.name = name

#     @staticmethod
#     def __generate_number(): # чтобы не было видно счастливого числа игрока
#         import random
#         number = random.sample(list('123456789'),5)
#         number = ''.join(number)
#         return number

#     def get_number(self):
#         number = self.__generate_number()
#         self.number = number
#         return f"Dear {self.name}! Your lucky number is {self.number}"

# participant1 = Lottery(name = 'Lucas')
# print(participant1.get_number())

# participant2 = Lottery('Sandy')
# print(participant2.get_number())


"""
Использование всех типов методов класса
"""
# class Pizza:

#     def __init__(self,ingredients: list):
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f"Pizza with {self.ingredients}"


# pizza1 = Pizza(['tomaties','mozarella','bazil'])
# pizza2 = Pizza(['meat','chilli pepper','cheese'])

# print(pizza1)
# print(pizza2)


"""
Усложним и улучшим пример выше и сделаем его более удобным для пользователя.
"""
# class Pizza:

#     def __init__(self,ingredients: list):
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f"Pizza with {self.ingredients}"

#     @staticmethod
#     def circle_area(radius):
#         from math import pi
#         area = round(pi* radius**2)
#         return  f'Pizza\'s area is {area} sm2'


#     def area(self, radius):
#         self.radius = radius
#         return self.circle_area(radius)

#     @classmethod
#     def margarita(cls):
#         return cls(['mozarella','tomatoes','bazil'])

#     @classmethod
#     def pepperoni(cls):
#         return cls['pepperoni','cheese']

#     @classmethod
#     def chilli(cls):
#         return cls(['chilli peppers','cheese'])


# pizza1 = Pizza.margarita()
# print(pizza1)
# print(pizza1.area(4))

# print()

# pizza2 = Pizza.margarita()
# print(pizza2)
# print(pizza2.area(20))

# print()

# pizza3 = Pizza.chilli()
# print(pizza3)
# print(pizza3.area(15))

"""
ClassWork
Классная работа


1) Создайте класс Passport, в котором есть следующие атрибуты:
Атрибут класса users_images, в котором хранится пустой список, и атрибут класса black_list - тоже пустой список
Атрибуты экземпляра класса при инициализации объекта: name, last_name, date_of_birth, image, INN (INN при создании объекта 
равен None)
Метод check_dublicate_person, который при вызове через созданный объект класса, заносит атрибут данного объекта image в 
список users_image, если такой фотографии еще нет, если же она уже есть, т.е. если человек с такой фотографией уже есть в 
нашей “базе данных”, то этот объект-человек, через который мы вызвали данный метод, заносится в черный список. 
Также есть метод get_inn, который выдает сгенерированный INN для объекта. INN должен содержать какое-то число от 
1999999-19999999. Но если объект находится в черном списке, то метод get_inn выдает сообщение: 
“Для объекта черного списка INN не генерируется”
По надобности переопределите методы __str__ или __repr__
Создайте объекты от класса Passport и вызовите у каждого объекта метод check_dublicate_person и метод get_inn. 
Также проверьте черный список и users_images. 

"""
# class Passport:
#   @classmethod
#   def users_images(cls):
#     list_ = []
#     black_list = []

#     def __init__(self,name, last_name, date_of_birth, image, INN):
#       self.name = name
#       self.last_name = last_name
#       self.date_of_birth = date_of_birth
#       self.image = image
#       self.INN = INN
    
#     def check_dublicate_person(self):


# class Passport: 
#     users_images = [] 
#     black_list = [] 
 
#     def __init__(self, name, last_name, date_of_birth, image) -> None: 
#         self.name = name 
#         self.last_name = last_name 
#         self.date_of_birth = date_of_birth 
#         self.image = image 
#         self.INN = None 
     
 
#     def check_dublicate_person(self): 
#         if self.image not in self.__class__.users_images: 
#             self.__class__.users_images.append(self.image) 
#         else: 
#             self.__class__.black_list.append(self) 
 
#     @staticmethod 
#     def generate_inn(): 
#         import random 
#         return random.randrange(1999999, 19999999) 
 
#     def get_inn(self): 
#         if self not in self.__class__.black_list: 
#             inn = self.generate_inn() 
#             print(f"generated inn: {inn}") 
#             return inn 
#         else: 
#             return "Для объекта черного списка INN не генерируется" 
 
#     def __str__(self) -> str: 
#         return f"{self.name} {self.last_name} born on {self.date_of_birth}, with an INN: {self.INN}" 
 
#     def __repr__(self) -> str: 
#         return f"{self.name} {self.last_name} born on {self.date_of_birth}, with an INN: {self.INN}" 
 
 
# p1 = Passport("Emily", "Boris", "11.11.1990", "image_emily.png") 
# print(p1) 
# p1.INN = p1.get_inn() 
# print(p1) 
 
# p2 = Passport("Jake", "Kim", "10.09.2001", "image_jake.png") 
# p1.check_dublicate_person() 
# p2.check_dublicate_person() 
# print(Passport.users_images) 
# p2.check_dublicate_person() 
# print(Passport.black_list) 
# print(p2.get_inn())

"""
Tasks
Таски

Создайте класс Product, для какого-либо продукта, у класса должна быть переменная класса - base_price, базовая цена, равная
20000.

Экземпляры класса должны иметь атрибуты model, year и color.

Создайте для класса метод has_garantiya() принимающий в переменную year год и проверяющий действительна ли гарантия на 
продукт, если с указанного года прошло больше 2х лет, возвращайте строку:

Ваша гарантия истекла 
в противном случае:

Гарантия действительна 
Также создайте метод класса change_price(), который повышает базовую цену на процент переданный в переменную rate - процент 
инфляции.

Создайте от класса объект obj примените все методы.

Ввод должен быть:

obj = Product('A218', 2008, 'red') 
obj.change_price(2) 
print(obj.has_garantiya(2010)) 
print(obj.base_price) 
А вывод:

Гарантия действительна 
40000 
"""


# class Product:
#     base_price = 20000

#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color

#     def has_garantiya(self, year):
#         if year - self.year > 2:
#             return 'Ваша гарантия истекла '
#         else:
#             return 'Гарантия действительна '
    
#     @classmethod  
#     def change_price(cls,rate):
#         cls.base_price *=rate


# obj = Product('A218', 2008, 'red')
# obj.change_price(2)
# print(obj.has_garantiya(2010))
# print(obj.base_price)

"""
2.Создайте класс User, объекты которого имеют атрибуты - name, lastname, email.

Создайте статический метод validate_email, который проверяет есть ли в имейле знак собачки @ и возвращает True либо False.

Переопределите метод __str__ так чтобы если у юзера был валидный имейл при использовании print() вам возвращалась строка:

"{Имя юзера}: {имейл}"

где вместо Имя юзера и имейл должны быть соответствующие значения.

В противном случае должна быть строка:

"email в неправильном формате".

Создайте класс метод create_user, который может создавать объекты от класса User из строк, переданных в 
таком формате - "Имя, Фамилия, имейл".

Например:

user1 = User.create_user('John, Snow, john@email.com') 
применив метод create_user получим объект с John в атрибуте name, Snow в атрибуте lastname и john@email.com в атрибуте email.

Создайте 2 экземпляра класса User - user1 и user2, где user2 должен иметь неправильный имейл(без @). Распечатайте эти объекты .

Ввод должен быть:

print(user1) 
print(user2) 
А вывод:

John: john@gmail.com 
email в неправильном формате 
"""
# class User:
#     def __init__(self,name, last_name, email):
#         self.name = name
#         self.last_name = last_name
#         self.email = email
    
#     @staticmethod
#     def validate_email(email):
#         if '@' in email:
#             return True
#         else:
#             return False

#     def __str__(self):
#         if self.validate_email(self.email):
#             return f"{self.name}: {self.email}"
#         else:
#             return f"email в неправильном формате"
            
#     @classmethod
#     def create_user(cls,string:str):
#         name, last_name, email = string.split(', ')
#         return cls(name,last_name,email)


# user1 = User.create_user('John, Snow, john@email.com') 
# user2 = User.create_user('Mary, Antuanetter, antygmail.com')

# print(user1) 
# print(user2) 

"""
3.Напишите класс учеников Makers, который будет содержать 4 атрибута:

атрибут экземпляра класса name (имя студента)
атрибут экземпляра класса language (язык, которому обучается студент)
атрибут экземпляра класса kpi (оценка студента)
атрибут класса students_count (количество учеников)
Также класс должен содержать следующие методы:

класс-метод new_student, который будет создавать нового ученика (экземпляр класса), и при этом увеличивать количество студентов на 1.
метод get_info, который будет возвращать имя и язык, выбранный учеником.
а также метод set_kpi, который будет устанавливать и возвращать оценку ученика.
Создайте двух студентов student1, student2 и примените к ним методы set_kpi и get_info. В конце вывести общее количество студентов.

Ввод должен быть:

print(student1.set_kpi(89)) 
print(student1.get_info()) 
print(student2.set_kpi(89)) 
print(student2.get_info()) 
print(Makers.student_count) 
Вывод:

89 
Student name: Vlad, Language: Python 
89 
Student name: Malik, Language: JavaScript 
2 

"""
# class Makers:
#     student_count = 0
#     def __init__(self, name, language, kpi):
#         self.name = name
#         self.language = language
#         self.kpi = kpi
        
#     @classmethod
#     def new_student(cls,name, language, kpi):
#         cls.student_count +=1
#         return  cls(name, language,kpi)

    
#     def get_info(self):
#         return f'Student name: {self.name}, Language: {self.language}' 
    
#     def set_kpi(self,kpi):
#         self.kpi = kpi
#         return self.kpi
        
# student1 = Makers.new_student(name = 'Vlad', language = 'Python', kpi = 0)
# student2 = Makers.new_student(name = 'Malik', language = 'JavaScript', kpi = 0)

# print(student1.set_kpi(89)) 
# print(student1.get_info()) 
# print(student2.set_kpi(89)) 
# print(student2.get_info()) 
# print(Makers.student_count) 

"""
4.Создайте класс Bike в котором будут инициализированы следующие атрибуты:

self.cost (стоимость)
self.make (производитель)
self.model (модель)
self.year (год выпуска)
self._sale_price = None (цена для продажи, по умолчанию None)
self.sold = False (продан или нет, по умолчания False)
self.min_profit (мин. прибль, которая должна прийти с продажи велосипеда)

Создайте метод set_cost для указания цены для продажи, который принимает цену и устанавливает ее если она больше стоимости, 
а если она меньше стоимости, то ставит дефолтную цену для продажи (стоимость + мин. прибыль).

Для ремонта велосипеда будет использоваться метод service, который принимает стоимость ремонта велосипеда, 
соответственно продажная цена велосипеда возрастает на столько, сколько обошелся ремонт и возвращает новую цену для продажи.

При продаже велосипеда будет использоваться метод sell, который меняет значение self.sold на True и возвращает прибыль с продажи.

Допишите метод класса get_default_bike, который будет создавать дефолтный велосипед со следующими параметрами: (10000, "Author", "Basic ASL", 2020, 2000).

Создайте объект:

bike = Bike.get_default_bike() 
Используете метод set_cost с аргументом 6000 затем service cо значением 300, и проверьте значения всех его атрибутов. (распечатайте print(bike.cost) и.т.д).

Ввод должен быть:

bike = Bike.get_default_bike() 
bike.set_cost(6000) 
bike.service(300) 
print(bike.sell()) 
print(bike.cost) 
print(bike.make) 
print(bike.year) 
print(bike._sale_price) 
print(bike.sold) 
print(bike.min_profit) 
Вывод:

1700 
10000 
Author 
2020 
8300 
True 
2000 
"""
# class Bike:
#     def __init__(self,cost,make,model,year, min_profit):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self._sale_price = None
#         self.sold = False
#         self.min_profit = min_profit
      
#     def set_cost(self, sale_price):
#         if sale_price < self.cost:
#             self._sale_price = sale_price + self.min_profit
#             return self._sale_price
#         else:
#             self._sale_price = sale_price
#             return sale_price
    
#     def service(self, service_cost):
#         self._sale_price += service_cost
#         return self.cost
    
#     def sell(self):
#         self.sold = True
#         profit = self.cost - self._sale_price
#         return profit

#     @classmethod
#     def get_default_bike(cls):
#         return cls(cost = 10000, make = "Author", model ="Basic ASL",year = 2020, min_profit = 2000)

# bike = Bike.get_default_bike() 
# bike.set_cost(6000) 
# bike.service(300) 
# print(bike.sell()) 
# print(bike.cost) 
# print(bike.make) 
# print(bike.year) 
# print(bike._sale_price) 
# print(bike.sold) 
# print(bike.min_profit) 

"""
5.Создайте класс MoneyFmt, экземпляры класса должны иметь один единственный атрибут amount. Создайте static метод dollarize, который принимает дробное число float в переменную float_num и переводит его в долларизованный формат, то есть:

dollarize(123456.78901) --> "$123,456.80"

dollarize(-123456.7801) --> "-$123,456.78"

dollarize(1000000) --> "$1,000,000"

Класс должен содержать 5 метода:

__init__ - инициализирует значение атрибута amount
update - задаёт объекту новое значение amount
__repr__ - возвращает значение float
dollarize - статический метод
__str__ - метод, который использует метод dollarize()
Создайте обьект cash класса MoneyFmt.

Ввод у вас должен быть:

cash = MoneyFmt(12345678.021) 
print(cash) 
cash.update(100000.4567) 
print(cash) 
cash.update(-0.3) 
print(cash) 
print(repr(cash)) 
Вывод:

$12,345,678.02 
$100,000.46 
-$0.30 
-0.3 
"""

# class MoneyFmt:
#     def __init__(self, amount):
#         self.amount= amount
    
#     def update(self, amount):
#         self.amount = amount

#     def __repr__(self):
#         return f'{self.amount}'
        
#     @staticmethod
#     def dollarize(float_num):
#         if float_num < 0:
#             float_num = abs(float_num)
#             amount = "-${:,.2f}".format(float_num)
#             return amount        
#         else:
#             amount = "${:,.2f}".format(float_num)
#             return amount
    
#     def __str__(self):
#         return self.dollarize(self.amount)
        
    
# cash = MoneyFmt(12345678.021) 
# print(cash) 
# cash.update(100000.4567) 
# print(cash) 
# cash.update(-0.3) 
# print(cash) 
# print(repr(cash))        
        


"""
Начало разбора

1. Методы экземпляра класса(instance methods)
Изменяют состояние( изменять атрибуты объекта) и класса

"""
# class A:
#     attr1 = 'a'

#     def __init__(self, attr2):
#         self.attr2 = attr2

#     def set_attr1(self, value):
#         self.attr1 = value
    
#     def set_attr2(self, value):
#         self.__class__.attr2 = value

# a1 = A(10)
# a2 = A(20)

# a1.set_attr1(11)
# print(a1.attr1)
# print(a2.attr1)

# a1.set_attr2(30)
# print(a1.attr2)
# print(a2.attr2)

"""
2. Методы класса(class methods)
"""
# class A:
#     def __init__(self, attr2):
#         self.attr2 = attr2

#     def set_attr1(self, value):
#         self.attr1 = value
    
#     @classmethod
#     def set_attr2(cls, value):
#         cls.attr2 = value

"""
3.Статический метод(static methods) -  это функция, которая помещена внутрь класса для группировки логики. Не имеет доступа ни к классу, ни к его объектам.
 
Пример с классом Car
"""

# class Car:
#     produced = []

#     def __init__(self, vin_code):
#         self.vin = vin_code

#     @classmethod
#     def create(cls):
#         vin_code = cls.generate_vin()
#         cls.produced.append(vin_code)
#         return cls(vin_code)
    
#     @staticmethod
#     def generate_vin():
#         import random
#         code = random.randrange(1, 1000)
#         return code

"""

"""

# class Converter:
#     @staticmethod
#     def celsius_to_fahrenheit(temprerature):
#         pass

#     @staticmethod
#     def fahreheit_to_celsiud(temprerature):
#         pass

#     @staticmethod
#     def meter_to_yard(distance):
#         pass

#     @staticmethod
#     def kg_to_pound(weight):
#         pass

# print(Converter.celsius_to_fahrenheit(56))


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


"""

"""


"""

"""


"""

"""


"""

"""
