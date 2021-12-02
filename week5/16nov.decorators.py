"""
День 2. Неделя 5. 16 ноябрая
Тема: Декараторы

Декаратор - это паттерн, проектирования в Python, который позволяет пользователю добавлять новые функциональные возможности 
к существующему объекту без изменения его структуры.

~ Функция, которая принимает другую функцию в качестве аргумента.

Декоратор - это основа, а доп функция его аргмент.

@ - это специальный синтаксис для определения функции декоратора.

Синтаксический сахар - это синтаксические возможности, применение которых не влияет на поведение программы, 
но делает использование языка более удобным для человека. 
Декораторы обычно вызываются перед определением функции, которую вы хотите декорировать.

Python позволяет вложенной функции получить доступ к внешней области видимости вмещающей функции.

Встроенные декораторы:

- property
- classmethod
- staticmethod

__name__ - свойство для получения имени функции

*  -  для распоковки списков, кортежей
** -  для распоковки словарей

Начало практики!

"""
# def hello_makers():
#     print('Hello, Makers')
# print(type(hello_makers))
"""
Хранить функции в переменных
"""
# makers =  hello_makers
# print(id(makers)) #139742369292352
# print(id(hello_makers)) #139742369292352

"""
Определить функции внутри другой функции
"""
# def outer_func():
#     def inner_func():
#         print('Hello, Makers')

#     inner_func()
# outer_func() #Hello, Makers

"""
Передавать функции в качестве аргумента и возвращать их из других функций.
"""
# def main_func(func):
#     print(f'Я получила функцию {func} в качестве аргумента')
#     func()
#     return func

# def hello_makers():
#     print('Hello, Makers')

# print(main_func(hello_makers))

"""
Декараторы - это функция, которая оборачивает другую функцию для расширения ее функциональности без изменения самого кода декаратора.

"""
# def func1():
#     print("I'm called inside other function")

# def func2(func):
#     print("I'll do something before func calling")
#     func()

# func2(func1) #I'll do something before func calling
#              #I'm called inside other function


"""
То есть сперва мы вызываем саму функцию func2, а потом значение функции func1
Или как в примере ниже сперва func1, а потом func3()

В данных примерах, func1() - декаратор
"""
# def func1():
#     print("I'm called inside other function")

# def func2(func):
#     print("I'll do something before func calling")
#     func()

# def func3():
#     print('Hello, Makers')

# func2(func3)

"""
Вот такой пример с декораторм и ее специальный синтаксис @
"""
# def decarator(func):
#     print("Я  функция-декоратор")
#     def wrapper():
#         print('Я функция-обертка')
#         print('Мы вызываем обернутую функцию')
#         func()
#         print('Я выхожу из обертки')
#         return func
#     return wrapper

# @decarator
# def hello_makers():
#     print('Hello Makers')

# @decarator
# def hello_bootcamp():
#     print('Hello, Bootcamp')

# hello_makers() #принтятся все строчки сверху вниз и последняя я выхожу из обертки

# hello_bootcamp() # также

"""
Небольшой пример с декаратором
"""
# def check_password(func):
#     def wrapper():
#         return func().strip()
#     return wrapper

# @check_password
# def get_password():
#     password = input('Enter password: ')
#     return password

# def get_email():
#     email = input('Enter email: ')
#     return email


# print(get_password()) #345   i
# print(get_email()) #bermetibr@gmail.com

"""
Пример с бутербродом
"""
# def bread(func):
#     def wrapper(filler):
#         print('</-----\>')
#         func(filler)
#         print('</_____\>')
#     return wrapper

# def ingredients(func):
#     def wrapper(filler):
#         print('#tomato#')
#         func(filler)
#         print("--salad--")
#     return wrapper
# @bread
# @ingredients
# def get_sandwich(filler):
#     print(filler)

# get_sandwich('--ham--') #</----\>
#                         #tomato#
#                         #--ham--
#                         #--salad--
#                         #</_____\>


"""
Тот же самый пример, только с *args
"""

# def bread(func):
#     def wrapper(*args):
#         print('</-----\>')
#         func(*args)
#         print('</_____\>')
#     return wrapper

# def ingredients(func):
#     def wrapper(*args):
#         print('#tomato#')
#         func(*args)
#         print("--salad--")
#     return wrapper
# @bread
# @ingredients
# def get_sandwich(*filler):
#     print(filler)

# get_sandwich('--ham--','**sausages**','&ketchup&') # то же самое, что и в предедущем, только это все в одну строчку

"""
Пример с использование *args и **kwargs
"""
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print(f'See what I got: {args}')
#         print(f'See what I got: {kwargs}')
#         func(*args,**kwargs)
#     return wrapper

# @decorator
# def func_without_params():
#     print("I'm a poor func without params")

# # func_without_params() # получаем пустые аргсы и кваргсы

# @decorator
# def func_with_params(name, last_name):
#     print("I'm a happy func with params")
#     print(f'Hello, {name} {last_name}')


# func_with_params('Itachi', last_name = 'Uchiha') # в арсы вошло имя, а в кваргсы вошел словарь из фамилии : Uchiha

"""
Чем больше вложенных функций, тем меннее читабельный код
Поэтому лучше использовать максимум 2 вложенные функции

Рассмотрим пример с замером времени на парсинг сайта
"""
# def benchmark(iters: int) -> int:
#     def actual_decorator(func):
#         import time
#         def wrapper(*args,**kwargs):
#             total = 0
#             for i in range(iters):
#                 start = time.time()
#                 func_call = func(*args,**kwargs)
#                 end = time.time()
#                 total = total + (end-start)
#             print(f'Average comlete time : {total/iters}') # считаем среднее время для выполнения функции
#             return func_call
#         return wrapper
#     return actual_decorator

# @benchmark(iters =10)
# def get_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage.text # получаем html нашего сайта

# print(get_webpage(url = 'https://yandex.ru/')) #Average comlete time : 0.5131358146667481 и дале сам html text


"""
Начало разбора

Функция - это объект
Функцию можно присвоить в переменную, а также передавать как аргумент и возвращать как результат
Также внутри функций могут определяться локальные функции.

"""
# def func1():
#     print('Hello, world')

# a = func1
# a()


# def func1():
#     print('1 function')

# def func2(func):
#     print('2 function')

# func2(func1)

"""
Локальные функции и их возвращение
"""
# def func1():
#     print('First')
#     def func2():
#         print('Second')
#     return func2
# func1()() # First Second

"""
Декоратор (функция для функции)- функция, которая принимает функцию, наделяет её дополнительным функционалом, 
но при этом исходный код принятой функции не изменяется.

"""
# from datetime import datetime

# def decorator(func):
#     def wrapper():
#         print(f'Текущее время: {datetime.now()}')
#         func()
#         print('Функция окончена')
#     return wrapper

# @decorator
# def func1():
#     print('A')

# @decorator
# def func2():
#     print('B')

# @decorator
# def func3():
#     print('C')

# func1()
# func2()
# func3()


"""
Небольшой пример

Написать декоратор loger, который будет записывать в файл, какая функция вызвана и во сколько и с какими параметрами.
Применить его к 3 разным функциям
"""
# def loger(func):
#     def wrapper(*args,**kwargs):
#         import datetime
#         with open(f'log.txt','a') as file:
#             current = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
#             func(*args,**kwargs)
#             file.write(f'Функция {func.__name__} вызывана в {current}')
#             file.write('-----------------\n')
#     return wrapper

# @loger
# def func1():
#     print('Hello, world')

# @loger
# def func2(x,y):
#     print(x*y)

# @loger
# def func3(list_):
#     print(sum(list_))


# func1() #Hello, world
# func2(15,5) #75
# func3([1,2,3,4,5]) #15


# def func(*args,**kwargs):
#     #args    --> (1,2,3)
#     #kwargs --> {'a':1,'b':2,'c':3}

# func(1,2,3,a=1,b=2,c=3)

"""
Переедача аргументов в параметр функции
"""
# def func(a,b,c):
#     print(a+b+c)

# func(1,2,3) #6
# func(a=1,b=2,c=3) #6
# func(1,2,c=3) #6

# list1 =[1,2,3] #6
# tuple1 = (1,2,3) #6

# func(*list1) #6
# func(*tuple1)#6

# dict1 = {'a':1,'b':2,'c':2}

# func(**dict1) #6

"""
Берем декоратор logger из задания выше
"""
# @loger
# def multiply(x,y):
#     return x*y

# multiply = loger(multiply)
# multiply = wrapper

# multiply(8,10)


"""
Написать декоратор, который замеряет время выполнения функции в милисекундах
"""
# def timer(func):
#     def wrapper(*args,**kwargs):
#         import time
#         start =  time.time()
#         func(*args,**kwargs)
#         end = time.time()
#         working_time = end -start
#         print(f'Время выполнения функции:{working_time*1000}')
#     return wrapper

# @timer
# def func1():
#     print('Hello, world')

# @timer
# def func2(x,y):
#     return x*y

# @timer
# def func3(list_):
#     return sum(list_)

# func1()
# func2(2,3)
# func3([1,2,35])

"""
Написать декоратор, который замеряет среднее время выполнения функции в милисекундах за n выполнений.

"""
# def timer(n):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             import time
#             total_time = 0
#             for _ in range(n):
#                 start =  time.time()
#                 result =func(*args,**kwargs)
#                 end = time.time()
#                 working_time = end -start
#                 total_time += working_time
#             avg_time = total_time/n
#             print(f'Время выполнения функции:{avg_time*1000}')
#         return wrapper
#     return decorator

# @timer(100)
# def func1():
#     print('Hello, world')

# @timer(4)
# def func2(x,y):
#     return x*y

# @timer(78)
# def func3(list_):
#     return sum(list_)

# func1()
# func2(2,3)
# func3([1,2,35])



"""
Chek-list от Кани
"""
"""
1.Написать код, для удаления всех символов, кроме букв в строке с помощью декоратора
"""

# def titles(func):
#     def wrapper(name):
#         name = func(name)
#         return name.title()
#     return wrapper

# def check_symbols(func):
#     def wrapper(name):
#         name_list = list(func(name)) # вернет имя
#         symbols = list('1234567890,./?!@#$%^&*()<>/\|')
#         name_list = [i for i in name_list if i not in symbols]
#         name = ''.join(name_list)
#         return name
#     return wrapper
# @titles
# @check_symbols
# def get_name(name):
#     return name
    
# print(get_name('ita&.(chi#$^&'))

"""
2. Напишите программу, которая будет запрашивать у пользователя, сколько котлет он хочет получить в своем бургере. Также
программа должна запросить, какие дополнительные ингредиенты пользователь хочет добавить в свой бурер через пробел. И в конце
программа должна выдавать получившийся бургер. По умолчания бургер обязательно включает такие ингредиенты, как булочки, салат, 
помидоры и кетчуп.
"""
# def main(iters: int) -> int:
#     def actual(func):
#         def wrapper(*args):
#             print('Верхняя булочка')
#             print('Помидоры')
#             for _ in range(iters):
#                 print('Котлета')
#             func(*args)
#             print('Кетчуп')
#             print('Салат')
#             print('Нижняя булочка')
#         return wrapper
#     return actual

# @main(iters = int(input('Сколько колтлет хотите добавить: ')))
# def get_info(*extra_ingriedients):
#     if extra_ingriedients:
#         for ingr in extra_ingriedients:
#             print(ingr)

# ingriedients = input('Какие дополнительне ингиридиенты вы желаете:\n(перечислите через пробел)').split()
# get_info(*ingriedients)


"""
Classwork
Классная работа

1.Напишите декоратор repeat, который принимает как именованный аргумент num целое число (количество выполнения 
декорированной функции) и запускает декорированную функции указанное количество раз.

Например
```python
@repeat(num=4)
def function(name):
    print(f"{name}")

При вызове function("Python"), вывод должен выглядеть так:
Python
Python
Python
Python
"""
# def repeat(num):
#     def decorator(func):
#       def wrapper(name):
#         for _ in range(num):
#           func(name)
#       return wrapper
#     return decorator

# @repeat(num=5)
# def function(name):
#     print(f"{name}")
  
# function('Bermet Ibraeva')


"""
2.Напишите декоратор countdown, который принимает параметр seconds и отсчитывает секунды до запуска декорированной функции.

Например:
```python
@countdown(seconds=5)
def func():
    print('Hello world')
```
#вывод
5
4
3
2
1
Hello world!
"""

# def countdown(seconds):
#     def timer(func):
#         def wrapper():
#             i = range(1,seconds+1)[::-1]
#             for k in i:
#                 print(k)
#             func()
#         return wrapper
#     return timer
            

# @countdown(seconds=5)
# def func():
#     print('Hello world!')

# func()

"""
Task
Таски

1.Напишите декоратор call_function, который печатает перед вызовом полученной функции строку:

Вызываю функцию <имя_функции>
Затем следует вызов функции. После вызова функции должна печататься строка:

 "Вызов функции <имя_функции> прошёл успешно"
Ввод:

@call_function
def first():
    print("hello world")
    return "hello world"
first()
Вывод:

Вызываю функцию 'first'
hello world 
Вызов функции 'first' прошёл успешно
"""
# def call_function(func):
#     def wrapper():
#         print(f'Вызываю функцию {func.__name__}')
#         func()
#         print(f'Вызов функции {func.__name__} прошёл успешно')
#     return wrapper

# @call_function
# def first():
#     print("hello world")
#     return "hello world"
# first()

"""
2.Создайте декоратор func_start_time, который будет распечатывать дату и время вызова принимаемой функции, 
а затем вызывает саму функцию, например:

@func_start_time
def func():
    print('Hello world')
func()
Вывод:

Функция запущена 26.02.2021 21:51
Hello World
Для этого воспользуйтесь модулем datetime.


"""
# from datetime import datetime
# def func_start_time(func):
#     def wrapper():
#         start = datetime.now()
#         print(f'Функция запущена {start}')
#         func()
#     return wrapper

# @func_start_time
# def func():
#     print('Hello world')
# func()

"""
3.Создайте 3 декоратора, каждый из которых применяет к тексту определённый стиль:

выделение жирным <b>...</b> (декоратор make_bold)

курсив <i>...</i> (декоратор make_italic)

подчеркивание <u>...</u> (декоратор make_underline)

Далее создайте функцию hello которая будет возвращать текст

Hello world
примените к этой функции цепочку декораторов.

@make_bold
@make_italic
@make_underline
def hello():
    return 'Hello world'
 
print(hello())
Вывод должен быть:

<b><i><u>Hello world</u></i></b>
"""
# def make_bold(func):
#     def wrapper():
#         return f'<b>{func()}</b>'
#     return wrapper

# def make_italic(func):
#     def wrapper():
#         return f'<i>{func()}</i>'
#     return wrapper

# def make_underline(func):
#     def wrapper():
#         return f'<u>{func()}</u>'
#     return wrapper

# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'

# print(hello())


"""
4.Создайте декоратор benchmark, замеряющий время выполнения функции в секундах и выводящий строку например:

Время выполнения: 0.05 секунд.
Затем объявите функцию fetch_webpage, которая выполняет GET-запрос на главную страницу Google, 
оберните в декоратор и вызовите её:

@benchmark 
def fetch_webpage(): 
  import requests 
  webpage = requests.get('https://google.com') 
"""
# import time
# def benchmark(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         total = end - start
#         return f'Время выполнения: {total} секунд'
#     return wrapper

# @benchmark
# def fetch_webpage():
#   import requests
#   webpage = requests.get('https://google.com')

# print(fetch_webpage())

"""
5.Создайте словарь users и сохраните в нем несколько пользователей (ключом будет имя пользователя, 
а значением пароль пользователя). Напишите следующую функцию:

def login(username, password):
        print(f'Welcome, {username}')
Допишите к этой функции декоратор validate_password, который будет проверять есть ли в словаре пользователь с таким username и совпадает ли пароль.

Если такого username нет, то функция должна выводить сообщение:

Username is not defined 
Если же не совпадает password, т.е username сохранен с другим значением password, выведите сообщение:

Password is invalid 
"""
# users = {'jaanger': '123312', 'vlad': '46456', 'nazar': '456132', 'tima': '456123'}
# def validate_password(func):
#     def wrapper(username,password):
#         if username in users:
#             if password != users[username]:
#                 print('Password is invalid')
#             else:
#                 func(username,password)
#         else:
#             print('Username is not defined')

#     return wrapper

# @validate_password
# def login(username, password):
#     print(f'Welcome, {username}')
# login('jaanger','2003')

"""
6.Напишите функцию get_user, принимающую в аргументы словарь вида:

get_user({'username': 'john133', 'is_admin': True})
напишите также декоратор is_admin, который проверяет является ли юзер админом, если да выведите сообщение:

Доступ разрешен john133
если же юзер не админ:

Доступ запрещен john133
input:

@is_admindef
get_user(dict):
    return dict
 
get_user({'username': 'john133', 'is_admin': True})
get_user({'username': 'jane133', 'is_admin': False})
Доступ разрешен john133
Доступ запрещен jane133
"""
# def is_admin(func):
#     def wrapper(dictionary):
#         username = dictionary['username']
#         if dictionary['is_admin'] == True:
#             print(f'Доступ разрешен {username}')
#         else:
#             print(f'Доступ запрещен {username}')
#     return wrapper
# @is_admin
# def get_user(dictionary):
#     return dictionary

# get_user({'username': 'john133', 'is_admin': True})
# get_user({'username': 'jane133', 'is_admin': False})

"""
7.Вам дана функция get_page(path), которая принимает в аргументы путь к определенной странице вашего 
вебсайта(https://www.mywebsite.com/).

Напишите декоратор route, который будет выводить абсолютный путь(url), к какой-либо странице:

Например, если передадим строку '/about' или '/products' в нашу функцию:

@route
def get_page(path):
     return path
 
print(get_page('about/'))
print(get_page('products/'))
После обработки декоратора, получим такой результат:

https://www.mywebsite.com/about/
https://www.mywebsite.com/products/
"""
# def route(func):
#     def wrapper(path):
#         url = 'https://www.mywebsite.com/'
#         url = url + path
#         return url
#     return wrapper


# @route
# def get_page(path):
#     return path


# print(get_page('about/'))
# print(get_page('products/'))

"""
8.Напишите функцию prefix_name, которая принимает в аргументы список, состоящий из кортежей:

name_format([('Leo', 'Nimoy', 40, 'M'),
('Carrie', 'Fisher', 35, 'F'),
('Harrison', 'Ford', 38, 'M')])
В каждом кортеже, через запятую хранится имя, фамилия, возраст и пол человека - 'M' - мужской, 'F' женский.

Функция должна возвращать строку - 'Ms. Carrie Fisher', с приставкой Ms. если это человек женского пола, 
и с приставкой Mr. если мужского - 'Mr. Leo Nimoy'.Также напишите декоратор sort_names, который возвратит 
отсортированный по возрасту список 
имен(по возрастанию):

Ввод:

def sort_names(func):
     ...
 
@sort_names
     ...
def prefix_name(person):
     ...
 
print(prefix_name([('Leo', 'Nimoy', 40, 'M'),
      ('Carrie', 'Fisher', 35, 'F'),
      ('Harrison', 'Ford', 38, 'M')]))
Вывод должен быть:

['Ms. Carrie Fisher', 'Mr. Harrison Ford', 'Mr. Leo Nimoy']
"""
# def sort_names(func):
#     def wrapper(person):
#         person= sorted(person,key = lambda x: x[2])
#         result = func(person)
#         return result
#     return wrapper

# @sort_names
# def prefix_name(person):
#     list_of_full_names = []
#     for item in person:
#         if 'M' in item:
#             full_name = 'Mr. ' + item[0] + ' ' + item[1]
#             list_of_full_names.append(full_name)
#         elif 'F' in item:
#             full_name = 'Ms. ' + item[0] + ' ' + item[1]
#             list_of_full_names.append(full_name)
#     return list_of_full_names

# print(prefix_name([('Leo', 'Nimoy', 40, 'M'),
#       ('Carrie', 'Fisher', 35, 'F'),
#       ('Harrison', 'Ford', 38, 'M')]))

"""
9.Напишите функцию sort_phone_nums которая принимает список телефонных номеров в виде строк:

sort_phone_nums(['0700987456', '0555123456', '0770369852'])
функция должна отсортировать по возрастанию список номеров и разделить их символом #.

Напишите декоратор get_full_number, который преобразует телефонные номера в sort_phone_nums, 
добавляя к ним региональный код +996 и убирая лишний ноль в начале номера:

+996 555 123456
+996 770 369852
+996 777 987456
Ввод:

def get_full_number(func):
    ...
@get_full_number
def sort_phone_nums(list_):
    ...
 
sort_phone_nums(['0777987456', '0555123456', '0770369852'])
Вывод:

+996 555 123456#+996 770 369852#+996 777 987456
"""
# def get_full_number(func):
#     def wrapper(list_):
#         list_new = []
#         for number in list_:
#             number_new = '+996' + ' '+ number[1:4] + ' ' + number[4::]
#             list_new.append(number_new)
#         list_ = list_new
#         return func(list_)
#     return wrapper

# @get_full_number
# def sort_phone_nums(list_):
#     list_ = sorted(list_)
#     list_ = '#'.join(list_)
#     print(list_)

# sort_phone_nums(['0777987456', '0555123456', '0770369852'])

"""
10.Напишите декоратор type_check() который принимает в аргументы 
тип данных - str, int, list, dict и.т.д и проверяет подходит ли аргумент декорируемой функции по типу данных, 
к примеру, если у нас есть функция func1:

@type_check(int)
def func1(num):
    print(num*2)
наш декоратор приняв в аргументы int, должен проверить что аргумент функции num принадлежит именно типу данных int:

func1(2)

возвратит результат 4, если же передадим другой тип данных, к примеру словарь:

func1({1: 'какой-то', 2: 'словарь'})
декоратор возвратит строку:

Неверный тип данных :(
Ввод:

def type_check(correct_type):
 
    ...
 
@type_check(int)
def func1(num):
    print(num*2)
 
func1(2)
func1({1: 'какой-то', 2: 'словарь'})
Вывод:

4
Неверный тип данных :(
"""
# 1 variant:

# def type_check(correct_type):
#     def decorator(func):
#         def wrapper(num):
#             if not isinstance(num, int):
#                 print('Неверный тип данных :(')
#             else:
#                 func(num)
#         return wrapper
#     return decorator


# @type_check(int)
# def func1(num):
#     print(num*2)


# func1(2)
# func1({1: 'какой-то', 2: 'словарь'})

"""------------------------------------------"""

#2 variant

# def type_check(correct_type):
#     def decorator(func):
#         def wrapper(string):
#             if not isinstance(string, correct_type):
#                 print('Неверный тип данных :(')
#             else:
#                 func(string)
#         return wrapper
#     return decorator


# @type_check(str)
# def func1(string):
#     print(string)


# func1(2)
# func1('some title')

