"""
Закончен!!!

День 1. Неделя 3
Тема: Функция
Функция - это именованный блок кода, выполняющий одну определенную задачу и возращающий результат.

В языке программированя Python функции определяются с помощью оператора def

def get_makers():
    string = 'Makers'
    print(string)
    return string
Код, прописанный внутри тела функции будет работать только когда пройзедет вызов этой функции.

#определение функции

deg double():
number = int(input('Enter number: '))
print(number**2)
return number*2

#Вызов функции

double() 
Функция вызывается с помощью ()

В програмировании функции могут не только возвращать данные, но также принимать их, что реализуется с помощью параметров. 
Количество параметров может быть любым.

Параметры представляют собой локальные переменные, которым присваиваются значения в момент вызова функции. 
Конкретные значения, которые передаются  в функцию при  ее вызове называтся её аргументами.


#Для чего используют функции ?

Функции - очень полезный иснтрумент, который позволяет многократно вызывать один и тот же код из разных мест программы, 
при этом не нарушая принцип DRY(don't repeat yourself)
"""
"""
Начало практики:
Синтаксис функции

"""
 # у функции может быть любое имя

# def add(a,b):
#     print(a+b)

# add(3,4) #TypeError


# def name_of_function():
#     some_code
#     return variable

# neme_of_function()

"""
Вызов функции осуществляется с помощью return
Если не написать её, то по default нам выдадут None

""" 
# def function():
#     print('The function is called') # The function is called
#     return 'Makers'

# print(function()) #Makers

"""
print - встроенная функция
return -  ключевое слово, то что возвращает нам функция.

"""
# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1+num2)
#     return num1-num2

# print(substract()) # 15

# substract() #ничего

"""
Функция это объект 1 класса, то есть ее :
1.можно присвоить ее переменной

""" 
# variable = substract()
# print(variable) #15

"""
2. можно передавать в структурах данных

То есть можно вставить функцию в список, кортежи, множества, ...
"""
# list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,substract()]
# print(list_) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

"""
3. можно вызывать их в других функциях.
""" 
# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1+num2)
#     return num1-num2

# def function():
#     print("I'm calling substract function")
#     return substract()
# print(function()) #15 


"""
Функции можно передавать в качестве аргументов
Функция может принимать параметры, то есть все что находится в скобках 
def function(a,b)
a,b - параметры, их значения это и есть аргумент функции(то что вызывают)

По типу математики y = x :
аргумент - значения
параметр - определение

Количество параметров = количество аргументов, если нет то вызывается исключения TypeError

"""
# def multiply(a,b):
#     return a*b

# print(multiply(5,36)) #180



# def multiply(a,b):
#     return a/b

# num1 = 70
# num2 =16
# print(multiply(num1,num2)) #4.375
# print(num1) #70
# print(num2) #16


"""
Передача аргументов с помощью input()
""" 
# def welcome(name, last_name, year):
#     return f'Welcome, {last_name} {name},{year}'

# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')
# year = int(input('Your year of birth: '))
# print(welcome(name,last_name,year))


"""
Передаем одну функцию в качестве аргумента другой

Разбиваем строку на буквы и объединяем ее в новый список, при этом фильтрую список и отбирая только гласные
Дальше эти гласные объединяем в новую строку

"""
# def get_word(word):
#     list_letters = list(word)
#     return list_letters

# def get_vowels(letters):
#     vowels = ['a','o','y','i','u','e']
#     list_vowels = [letter for letter in letters if letter in vowels]
#     result = ''.join(list_vowels)
#     return result 

# my_word = input('Enter word, which you want to filter: ')
# print(get_vowels(get_word(my_word)))


"""
Именнованные аргументы - присваивают аргументам имена переменных
Также в сам параметр можно передать именнованные аргументы и получим результат
""" 

# def info(name ,age ):
#     return f'{name} is {age} years old.'

# print(info('Sam',19)) #Sam is 19 years old.


# def info(name ,age ):
#     return f'{name} is {age} years old.'

# print(info(10,'Jane')) #10 is Jane years old.


# def info(name = 'Sam',age =19):
#     return f'{name} is {age} years old.'

# print(info()) #Sam is 19 years old.


# def info(name = 'Sam',age =19):
#     return f'{name} is {age} years old.'

# print(info(name = 'John',20))  #positional argument follows keyword argumen

# def info(name = 'Sam',age =19):
#     return f'{name} is {age} years old.'

# print(info('John',age =20))

"""
Первым идет позиционный аргумент, далее именованный
Если наоборот, возникает ошибка positional argument follows keyword argument
"""
# def test_func(n1=2,n2=9):
#     return n1+n2
# print(test_func(n1=7,n2=8)) #15

# def test_func(n1=2,n2=9):
#     return n1+n2
# print(test_func(7,n2=8)) #15

# def test_func(n1=2,n2=9):
#     return n1+n2
# print(test_func(n1=8,8)) #positional argument follows keyword argument

"""
Пример
""" 
# def create_profile(name,age,image = 'default.jpg'):
#     return name,age, image

# print(create_profile(name = 'Raychel',age =30, image = 'flower.png')) #('Raychel', 30, 'flower.png')

"""
*args, **kwargs - функциальное средство, позволяют функции принимать какие-то неопределенные аргументы

Их необязательно передавать, но если передать, то они возвращаются в виде кортежа, содержащих позиционные аргументы.
*args - принимает позиционные аргументы, возвращает в виде кортежа.
**kwargs - принимает именнованные аргументы, возвращает в виде словаря.

"""

# def func(required,*args,**kwargs):
#     print(required)

#     if args:
#         print(args)
    
#     if kwargs:
#         print(kwargs)

# func('Itachi Uchiha','status','dead')


"""
Пример с *args и **kwargs
""" 
# def many(*args,**kwargs):
#     print(args) #(1, 2, 3)
#     print(kwargs) #{'name': 'Bill', 'job': 'IT-specialist'}

# many(1,2,3, name = 'Bill', job = 'IT-specialist')

"""

Конец практики!!!
"""

"""
Начало разбора
"""

# def list(*elements, **kwargs):
#     if 'step' in kwargs:
#         step = kwargs.get('step')
#         res = []
#         for index,elements in enumerate(elements):
#            if index % kwargs.get('step') != 0:
#                res.append(elements)
        
#         return res
    
#     else:
#         return[*elements]

# print(list(1,2,3,4,5,6,7,8,9,10,11,12, step = 2)) # [2, 4, 6, 8, 10, 12]

# def hello(age,name = 'Guest'):
#     print(f'Hello, {name}! Your age is {age}')

# hello(12,'Nastya')



"""
Калькулятор с помощью функций:
"""

# def add_func(num1,num2):
#     return num1+num2

# def sub_func(num1,num2):
#     return num1-num2

# def mult_func(num1,num2):
#     return num1*num2

# def div_func(num1,num2):
#     return num1/num2

# def handler(operator,num1,num2):
#     switcher = {'+' : add_func,
#                 '-' : sub_func,
#                 '*' : mult_func,
#                 '/' : div_func}

#     if not switcher.get(operator):
#         return 'Введён некорректный оператор'

#     return switcher.get(operator)(num1,num2) 
#     # switcher.get('-') = sub_func
#     #sub_func (num1,num2)

# num1 = int(input('Enter the first number:'))
# operator = input('Enter the operation from list: +,-,*,/ : ')
# num2 = int(input('Enter the second number: '))

# print(handler(operator,num1,num2))

"""
Задача с переводом букв с русского на английский
"""

# from os import initgroups

# def translate(string):
#     eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
#     ru = "йцукенгшщзхъфывапролджэячсмитьбю"
#     if string[0] in eng:
#         trantab = str.maketrans(eng,ru)
#     elif string[0] in ru:
#         trantab = str.maketrans(ru,eng)
#     return string.translate(trantab)

# string =input('Enter the string:  ').lower()
# print(translate(string))




"""
Classroom
Классная работа
"""
"""
1) Напишите функцию get_info, которая запрашивает у пользователя имя и фамилию, последовательно. 
Далее внутри get_info вызовите другую функцию generate_password, которая будет генерировать пароль 
при помощи конкатенации имени и фамилии пользователя и рандомных 7 чисел (в промежутке от 0 до 9). 
В конце функция get_info возвращает пользователю сгенерированный пароль.
"""
# писать код здесь

# def generate_password(param1,param2):
#     import random
#     random_list = random.sample(range(1,10), k =7)
#     random_list = [str(i) for i in random_list]
#     password = param1 + param2 +''.join(random_list)
#     return password


# def get_info(name = input('Enter your name: '),
#             last_name = input('Enter your last_name: ')):
#     password = generate_password(param1 =name,param2= last_name)
#     return password
    
# print(get_info())



"""
2) Напишите калькулятор на функциях. 
У вас должна быть основная функция get_data, которая запрашивает два числа, и действие (сложение, вычитание, умножение, деление). 
И в зависимости от выбранного действия get_data должна вызывать ту или иную функцию, в которой будет прописан алгоритм выполнения действий. 
В конце выдается результат через функцию result.
"""
# писать код здесь

# def add(a,b):
#     return a+b

# def substract(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

# def division(a,b):
#     return a/b

# def result(param):
#     return param


# def get_data(action):
#     num1 = int(input(f'Enter first number: '))
#     num2 = int(input(f'Enter second number: '))

#     dictionary = {'+': add(num1,num2),
#                     '-' : substract(num1,num2),
#                     '*' : multiply(num1,num2),
#                     '/' : division(num1,num2)                }
    
#     some_result = dictionary[action]
#     return result(some_result)
# action = input('Select action from list below: + - * /' + '\n')
# print(get_data(action))


"""
3) Напишите функцию, которая будет принимать 2 обязательных параметра: вкус мороженого и размер. 
И также функция может принимать необязательные параметры, которые могут выступать в качестве топпинга к мороженому. 
Выдайте результат
"""
# писать код здесь

# def make_icecream(name, size,**kwargs):
#     print(f'Your {name} ice cream, {size} size' +'\n')

#     if kwargs:
#         print('Your toppings: ')
#         for value in kwargs.values():
#             print(value)
    

# make_icecream(name = 'choclate',size = 'medium',toping1 = 'peanuts', toping2 ='coconut')


"""
Task
Таски

""" 
"""
1.Создайте функцию add, которая будет принимать 2 числа, складывать их и возвращать результат сложения.

"""
# def add(num1,num2):
#     return num1+num2

# print(add(3,4))


"""
2.Создайте функцию get_string_length() которая будет принимать строку. Функция должна возвращать длину этой строки.

Пример:

print(get_string_length('hello')) 
Вывод:
5 
""" 
# def get_string_length(str1):
#     return len(str1)

# print(get_string_length(str1 ='hello'))

"""
3.Создайте функцию: get_type() которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.

Пример:
get_type(5, 's') 
Вывод:
<class 'int'> 
<class 'str'> 

"""
# def get_type(a,b):
#     print(type(a))
#     print(type(b))

# print(get_type(a = 5,b = 'str'))

"""
4.Создайте функцию divide() которая должна принимать 2 числа и возвращать результат их деления.

Пример:

print(divide(5, 10)) 
Вывод:

0.5 

""" 
# def divide(num1,num2):
#     return num1/num2

# divide(12,2))

"""
5.Создайте переменную dict_ в котором будет хранится словарь.

Затем создайте функцию

def dictionary()
которая принимает этот словарь. Пройдитесь по dict_ циклом и распечатайте все его ключи внутри функции.


"""
# dict_ = {'a':12,'b':34,'c':43,'d':54}

# def dictionary(d):
#     for key in d:
#         print(key)

# dictionary(dict_)


"""
6.Создайте переменную num = 6. Затем создайте функцию

 check()
которая принимает переменную num в качестве аргумента

 check(num)
и возвращает "It is odd number", если это число нечетное и "It is even number" если переданное число четное.

Пример:

print(check(num)) 
Вывод:

It is even number 

""" 
# num = 6
# def check(num):
#     if num%2 !=0:
#         return "It is odd number"
#     else:
#         return "It is even number"

# print(check(num))
        

"""
7.Создайте функцию:

is_palindrome() 
которая будет принимать строку и проверить является ли она палиндромом.

Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. 
Например, число 101; слова "кок", "топот", "комок" и т.д.
Функция должна возвращать True или False. Пробелы и регистр учитывать нужно.

Пример:
print(is_palindrome('довод')) 
Вывод:

True 
"""
# def is_palindrome(str1):
#     if str1[::-1].lower() ==str1.lower():
#         return True
#     else:
#         return False

# print(is_palindrome(str1 = 'Itaata')) #False


"""
8.Создайте функцию

max_num()
которая принимает от пользователя два числа. Она должна сравнить эти числа между собой и вернуть максимальное значение.

Пример:

print(max_num(10, 12)) 

Вывод:
12 
""" 
# def max_num(num1,num2):
#     if num1>num2:
#         return num1
#     else:
#         return num2

# print(max_num(5,6))


"""
9.Создайте функцию:

multiply_list()
которая принимает список чисел и возвращает их произведение.

Пример:

print(multiply_list([1, 2, 3, 4, 5, 6])) 
Вывод:

720 

"""

# def multiply_list(list1):
#     res =1
#     for num in list1:
#         res*=num
#     return res
        
# print(multiply_list([1,2,3,4,5,6]))


"""
10.Создайте функцию

sum_digits()
которая принимает целое число и возвращает сумму всех его цифр.

Пример:

print(sum_digits(105)) 
Вывод:
6 

""" 
# def sum_digits(num1):
#     c =0
#     num1_string = str(num1)
#     for numbers in num1_string:
#         c += int(numbers)
#     return c
    
# print(sum_digits(276))

        


"""
Молодец!!!
Тема пройдена.
"""

def check_valide(email):

    try:
        username, url = email.split('@')
        website, extension = url.split('.')
    except ValueError:
        print('Please enter your email correctly')
        return False
    if not username.replace('-','').replace('_','').isalnum():
        print('Email cannot contain free spaces')
        return False
    if website.isalnum():
        return False
    if len(extension) > 3:
        print('extension cannot be more than 3 symbols')
        return True

n = input('How many emails do you want to refistrate ? ')

if n.isalpha():
    raise ValueError('Please enter the number correctly!')
else:
    emails = [input('Please enter your emails: ') for email in range(n)]

valid = list(filter(check_valide,emails))
print(f'Validated emails: {sorted(valid)}')