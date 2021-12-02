"""
День 2. Неделя 6.
Тема: Инкапсуляция

Инкапсуляция - это сокрытие данных, то есть невозможность напрямую получить доступ к внутренней структуре объекта, 
так как это небезопасно.

Инкаспуляция - это объединение свойств и поведения в единое целое, в одну капсулу, т.е. в класс.

В Python можно иммитировать сокрытие данных, так как в нём можно получить доступ к любому аттрибуту объекту и изменить его.

В классах может быть множество вспомогательных полей и методов, которые не должны использоваться за их пределами.

Модификаторы данных:

- Приватные данные- это те, которые скрыты от внешнего воздействия.(__name or __method)
- Защищённые данные - данные, которые защищены от внешнего воздей твия, но в языке Python их все ещё можно изменить извне.
- Публичные данные - это данные, которые доступны извне, и свободно могут подвергаться внешним воздействиям.


Методы для извлечения и изменнения данных: 

- getter - для получения данных;
- setter - для изменения данных.

В Python - существует аннотация свойств - использование декоратор @property и @name.setter.


Начало практики!
- Модификаторы доступа в Python

В примере ниже, все конечно хорошо
Но пароль не должен выдаваться, а должен быть скрытым.
"""

# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password

#     def get_info(self):
#         print(f'Useraneme: {self.username},password: {self.password}')

# user1 = User(username = 'Makers',password ='Bootcamp')
# print(user1.username)
# print(user1.password)

# user1.get_info()

"""
Модификаторы доступа:

1. public - password, get_info() - доступны для внешнего воздействия и видны
2. protected - _password, _get_info() - доступен для внешнего воздействия , но не видны, используется _
3. private - __password, __get_info() - не доступен для изменения и не виден, используется __


Изменим пример выше и сокроем его данные

"""
# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password

#     def get_password(self,username):
#         if self.username == username:
#             return self.__password
#         else:
#             return 'No'

#     def set_pasword(self, old_password, new_password):
#         if self.__password == old_password:
#             self.__password = new_password
#         else:
#             return 'No'

#     def __get_info(self):
#         print(f'Useraneme: {self.username},password: {self.password}')

# user1 = User(username = 'Makers',password ='Bootcamp')

"""Получения пароля без использования getter и setter"""

# print(user1.username)
# print(user1.password) #AttributeError: 'User' object has no attribute 'password'

'''Получения пароля и изменение его с помощью методов setter и getter'''

# print(user1.get_password()) #'Bootcamp
# user1.set_pasword(value = 'bootcamp123')

'''Проверка пароля и юзернейма на валидацию(True or False) для получения старого пароля и изменения его на новый'''

# print(user1.get_password(username= 'Makers')) #Bootcamp
# user1.set_pasword(old_password='Bootcamp', new_password = 'Bootcamp123')
# print(user1.get_password(username = 'qwerty')) #No, т.к. username мы указали неправильный

"""
Логика использования getter и setter в том, что мы можем сами прописывать логику получения и изменения скрытых данных и 
логику при которых доступ будет закрыт.
"""

"""
Пример
Если мы не будем скрывать наши данные, а  будем разрешать пользователю менять их, то наша прогромма может сломаться, поэтому изменим это
"""
# class Divider:
#     def __init__(self):
#         self.__divide_num = 1

#     def divide(self,value):
#         return value / self.__divide_num

# obj = Divider
# obj.__divide_num = 0
# print(obj.divide(7))
# print(obj.__divide_num)

"""
Пример с классом Person
"""
# class Person:
#     def __init__(self):
#         print('initialized')

# person = Person()
# person.name = 'Makers'
# person.age = 2
# print(person.name)
# print(person.age)


"""
Есть ещё один обходной путь, для получения данных, но его никто не использует.

Так между разработчиками следует соглашение и если другой разработчик, увидел, что данные скрыты, то он их не пытается 
получить или изменить, так как от этого изменения может сломаться логика программы.
"""
# class Divider:
#     def __init__(self):
#         self.__divide_num = 2

#     def divide(self,value):
#         return value / self.__divide_num

# obj = Divider()
# print(obj.divide(7))
# print(obj._Divider__divide_num) #2


"""
Методы getter и setter
"""
# class Divider:
#     def __init__(self):
#         self.__divide_num = 2

#     def get_divider(self):
#         return self.__divide_num

#     def set_divider(self, value):
#         if not value == 0:
#             self.__divide_num == value
#             return 'Number was changed'
#         else:
#             return 'На ноль делить нельзя'

#     def divide(self,value):
#         return value / self.__divide_num

# obj = Divider()
# print(obj.get_divider()) #2
# print(obj.divide(7)) #3.5
# print(obj.set_divider(value = 14)) #Number was changed
# print(obj.get_divider()) #2

"""
Декораторы @property и @setter

Используя декоратор property мы можем получать значение метода full_name без его вызова
"""
# class Person:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name

#     @property
#     def full_name(self):
#         return  f'{self.name} {self.last_name}'

# person = Person('John','Snow')

# print(person.full_name) #John Snow

"""
Используем декораторы на этом примере
"""
# class Divider:
#     def __init__(self):
#         self.__divide_num = 2

#     @property  #-----> getter
#     def divider(self):
#         return self.__divide_num

#     @divider.setter #-----> setter
#     def divider(self, value):
#         if not value == 0:
#             self.__divide_num == value
#             return 'Number was changed'
#         else:
#             return 'На ноль делить нельзя'

#     def divide(self,value):
#         return value / self.__divide_num

# obj = Divider()
# print(obj.divider) #2, получаем без вызова
# print(obj.divide(7)) #3.5
# obj.divider = 14 # можем сразу менять
# print(obj.divider) #2, получаем без вызова


"""
!!! Важно запомнить, что декоратор @property под капотом функции, которую декорирует принимает только объект, 
то есть при передаче других параметров будет вызываться ошибка
"""

# class Car:

#     def _inject_fuel(self):
#         print('Fuel injected') # 3

#     def _init_bang(self):
#         print('Bang-Bang') # 4

#     def _send_signal_to_ignition_system(self):
#         print('Ignition started') # 2
#         self._inject_fuel()
#         self._init_bang()

#     def _send_signal_to_pc(self):
#         print('Start') # 1
#         self._send_signal_to_ignition_system()

#     def start_engine(self):
#         self._send_signal_to_pc()


# car = Car()
# car.start_engine()

# # Output:

# # Start
# # Ignition started
# # Fuel injected
# # Bang-Bang

"""
Private, protected

Отличие protected от private:
1. Используется _
2. protected - мы её можем получить скрытые данные
3. protected данные наследуются в дочерних классах
"""
# class A:

#     def _say_hello(self):
#         print('Hello, makers!')


# class B(A):
#     pass

# b = B()
# b._say_hello()


"""
Classroom
Классная работа

1.Создайте класс Terminal. Создайте объект-карточку от этого класса, передав номер своей карточки и пин код. При этом, 
необходимо проверить валидность карточки: номер карточки должен содержать строго 16 цифр, а пин код - 4 цифры (для этого 
используйте инкапсуляцию). При создании карточки в ней содержится 0 сом. Далее в классе должны быть следующие методы:

- метод put, который будет принимать в качестве аргументов: пин код карточки, вторым аргументом - сумму денег, которую вы 
хотите закинуть на эту карточку. Прежде, чем закидывать деньги, необходимо проверить введенный пин код на совпадение
(используйте инкапсуляцию)
- метод get_money, который также принимает первым аргументом пин код, вторым аргументом - сумму денег,которую вы хотите извлечь из карточки. Здесь также
необходимо использовать валидацию: проверка пин кода + сумма денег должна быть округленной до десятичных чисел, типа 10, 100, 
200, 5000 и т.д. (67,899, 45.6 - невалидные данные). И только после проверки деньги извлекаются.

Примените данные методы к своей карточке несколько раз и в конце выдайте, сколько денег на карточке. Примечание: нельзя 
извлечь сумму денег, если она больше, чем сумма денег на карточке; также нельзя вытащить пин код карточки (эти данные
должны быть скрыты)
"""
# class Terminal:

#     def _check_card(self,card):
#         if len(card) == 16 and card.isdigit():
#             self.__card = card
#         else:
#             print('Invalid card number')
    
#     def _check_pin(self,pin):
#         if len(pin) == 4 and pin.isdigit():
#             self.__pin = pin
#             self.money = 0
#         else:
#             print('Invalid pin code')
        
#     def __init__(self, card, pin):
#         self._check_card(card =card)
#         self._check_pin(pin=pin)
#         self.money = 0
    
#     def put(self,pin,money):
#         if self.__pin == pin:
#             self.money+=money
#             print(f'There is {self.money} on your balance')
#         else:
#             print('Invalid pin code')

#     def __check_money(self,money):
#         if money %10 == 0:
#             return True
#         else:
#             return False

#     def get_money(self,pin,money):
#         if self.__pin == pin:
#             if self.money > money:
#                 self.money-=money
#                 print(f'There is {self.money} on your balance')
#             elif self.money == money:
#                 print('You\'re out of your balance or your balance 0' )
#             else:
#                 print('There isn\'t enough money to get this sum')
#         else:
#             print('Invalid pin code')


# card1 = Terminal(card = '1234567812345678',pin = '2223')
# card1.put('2223',4000)
# card1.get_money('2223',5000)
# card1.put('2223',1000)
# card1.put('2223',5000)
# card1.get_money('2223',10000)


    

    

        


"""
Таски
Tasks

1.Создайте класс A и объявите в нём 3 метода:

- публичный(public) (возвращает строку 'Public method'),
- защищённый(protected) (возвращает строку 'Protected method')
- приватный(private) (возвращает строку 'Private method')
Затем создайте экземпляр в переменной obj1 данного класса и вызовите (с выводом в терминал) по очереди каждый из методов.
"""

# class A:
#     def public(self):
#         return 'Public method'

#     def _protected(self):
#         return 'Protected method'

#     def _A__private(self):
#         return 'Private method'

# obj1 = A()
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())


"""
2.Определите класс A, в нём объявите метод method1, который печатает строку "Hello World".

Затем, создайте класс B, который будет наследоваться от класса A.

Создайте экземпляр в переменной b1 от класса B, и через него вызовите метод method1.
"""
# class A:
#     def method1(self):
#         print('Hello World')
    

# class B(A):
#     pass

# b1 = B()
# b1.method1()


"""
3.Объявите класс Car, в котором будет приватный экземпляр класса speed.
Затем, определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, который возвращает 
значение скорости.
Создайте экземпляр в переменной car1 класса Car и вызовите все методы.
Ввод:

car1 = Car() 
print(car1.show_speed()) 
car1.set_speed(20) 
print(car1.show_speed()) 
Вывод:

0 
20 
"""
# class Car:
#     def __init__(self):
#         self.__speed = 0
    
#     def set_speed(self,value):
#         self.__speed = value
    
#     def show_speed(self):
#         return self.__speed

# car1 = Car() 
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed()) 

"""
4.Перепишите класс Car из предыдущего задания.

Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора 
@property.

Создайте обьект car1 класса Car.

Ввод:

car1 = Car() 
print(car1.speed) 
car1.speed = 20 
print(car1.speed) 
Вывод:

0 
20 
"""
# class Car:
#     def __init__(self):
#         self.__speed = 0
    
#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self,value):
#         self.__speed = value

# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20
# print(car1.speed) 

"""
Разбор 

Публичные - доступны в самом классе, в его дочерних классах и вне класса.

attr1(), method1()

Защищенные - не доступны вне класса, но при этом доступнв в самов классе и в его дочерних классах.

_attr2, _method2()

Приватные - доступны только в самом классе.

__attr2, __method2()


Методы:
- getter  - метод, установливающий значение.
- setter -  метод, получающий значение.

"""
# class Stabilizer:
#     __voltage = 220

#     @property
#     def voltage(self):
#         return self.__voltage

#     @voltage.setter
#     def voltage(self, new_voltage):
#         if new_voltage > 300:
#             raise ValueError('Превышено максимальное значение')
#         self.__voltage = new_voltage

    
# stab1 = Stabilizer()
# voltage = 230
# stab1.voltage

"""

"""
# class A:
#     attr1 = 'a'
#     _attr2 = 'b'

# a1 = A()
# print(a1.attr1)  # a
# print(a1._attr2) # b

"""
2. Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня
заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 %
заряда при каждом обращении.
Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
разряжен).
Также предусмотрите возможность заряжания батареи.

1s - 10%
"""
# class Telephone:

#     def __init__(self,imei,ios, battery = 100):
#         self.__imei = imei
#         self.__ios = ios
#         self.__battery = battery
    
#     def get_info(self):
#         if self.__battery ==0:
#             raise BaseException('Telephon is discharged.Please put it on a charge')
#         self.__battery -= 0.5
#         return f'{self.__imei} {self.__ios}'

#     def listen_music(self):
#         if self.__battery == 0:
#             raise BaseException('Telephon is discharged.Please put it on a charge')
#         self.__battery -=5
#         return f'{self.__battery} % left'
    
#     def watch_video(self):
#         if self.__battery >=10:
#             self.__battery -= 7
#             return f'{self.__battery} % left'
#         elif self.__battery ==0:
#             raise 'Telephon is discharged.Please put it on a charge'
#         else:
#             return f'There is less than {self.__battery} left'
            
        
    
# telephone = Telephone(imei = 345673564, ios = 11)
# print(telephone.listen_music())
# print(telephone.watch_video())
# print(telephone.listen_music())
# print(telephone.get_info())
# print(telephone.listen_music())
# print(telephone.watch_video())
# print(telephone.listen_music())
# print(telephone.listen_music())
# print(telephone.listen_music())
# print(telephone.watch_video())
# print(telephone.watch_video())
# print(telephone.watch_video())
# print(telephone.watch_video())
# print(telephone.watch_video())
# print(telephone.watch_video())
# print(telephone.watch_video())
# print(telephone.watch_video())
# print(telephone.listen_music())
# print(telephone.get_info())
# print(telephone.get_info())
# print(telephone.get_info())
# print(telephone.get_info())

