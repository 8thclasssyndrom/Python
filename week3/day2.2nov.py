"""
Закончен         
День 2.Неделя 3. 2 ноября
Тема: Области видимости и пространства имён.

Cинтаксис
name =' Makers'

Пространство имён - это совокупность определённых в настоящим момент символических имён и 
информации об объектах, на которые они ссылаются.
Имена объектов(ключи) : объекты(значения)

Типы пространств:
1) Встроенное пространство - содержит все имена, встроенных объектов, которые всегда доступны при работе с Python
вызывается dir(-bultins-)


2) Глобальное пространство - содержит все имена, определенные на уровне основной программы и создается сразу при запуске тела этой программы.

name1  = 'Makers' #глобальное пространство #3
name2 = 'Bootcamp'


3) Замкнутое пространство -Если x не находится в локальной области, но появляется в функции, располагающейся внутри другой функции, 
то интерпретатор ищет его в области видимости объемлющей функции.

4) Локальное пространство - интерпритатор создает новое пространство при каждом выполнении функции.

def dunc1:
    name3 = 'boo' #замкнутое пространство #2

    def func2():
        name4 = 'helloworld' # локальное пространство #1

Область видимости переменной - Наличие нескольких отличных пространств имен означает, что в процессе выполнения программы Python несколько разных 
экземпляров одного имени могут существовать одновременно. Пока каждый из них находится в собственном пространстве, все они обслуживаются по отдельности, 
и путаницы не происходит.

Локальное-> замкнутое->глобальное-> встроенное

 * locals() - словарь локального пространства имён
 * globals() -словарь глобального пространства имён

Начало практики! 1.04 минуты

builts-in - 
global -
enclosed -
local - 

"""


# this_var_is_visible = 'You can see me inside and outside the function' #global


# def var_visibility():
    # this_var_is_not_visible = 'You can see me only inside the function' 
    # print(this_var_is_visible)

# # print(this_var_is_visible)
# var_visibility()

# variable = 'makers'

# print(variable) 

"""
builts-ins
"""
# print(dir(__builtins__))


"""
'ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 
'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 
'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 
'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 
'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', '
OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 
'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 
'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 
'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', 
'__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 
'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 
'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 
'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 
'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
"""

"""
global
"""
# name = 'Makers'
# name = 'Bootcamp' #перезаписывает глобальное значение
# print(name)


"""
local()
"""
# word = "I'm global" #2

# def func_a():
#     # word = "I'm local" #1
#     print(word)
   
# func_a()
# # print(word)

"""
enclosed
"""
# word = "I'm global" #3

# def outer2():
#     def inner():
#         # word = "I'm local" #2
#         print(word)
    
#     inner()

# def outer():
#     # word = "I'm enclosed" #1
#     print(word)

    

# outer()
# print(word)

"""
globals() - функция, возращает словарь глобального пространство имён.
"""
# dict_ = {'name': 'Makers','name':'Bootcamp'}


# name = 'Makers'
# name2 = 'Bootcamp'
# print(globals())

"""
locals() - функция, возращает словарь локального пространство имён.

"""
# def func(company):
#     name = 'Bootcamp' 
#     print(locals() # {'company': 'Makers', 'name': 'Bootcamp'}

# func(company = 'Makers')


# def info(name,age,height):
#     name = 'Alice'
#     age = 30
#     height =187
#     print(locals()) #{'name': 'Alice', 'age': 30, 'height': 187}

# info(name = 'Carly', age =25,height =165) 

# print(globals())
# print(locals())



"""
Изменение переменных вне зоны их видимости

nonlocal - работает для замкунтого пространства
"""
# def outer():
#     name = 'Makers'
    
#     def inner():
#         nonlocal name
#         name = 'Bootcamp'
#         print(name)

#     inner()
#     print(name)

# outer()


"""
Начало разбора
"""

# a = 'Это глобальная переменная'
# def func():
#     a = 'Это закрытая переменная'
#     print(a)
#     def inner_func():
#         a = 'Это локальная переменная'
#         print(a)
#     inner_func()

# func()
# print(a)


# num1 = 5
# num2 =4

# def sum(a,b):
#     global num1
#     print('a',a)
#     print('b',b)
#     print('num1',num1)
#     num1 = a+b
#     return a+num1

# print(sum(num1,num2))
# print(sum(num1,num2))
# print(sum(num1,num2))
# print(sum(num1,num2))


# def outter_func():
#     print('OUTTER')

#     def inner_func():
#         print('INNER')
#         return 5
    
#     return inner_func

# # print(outter_func)
# # print(outter_func())
# # print(outter_func()())
# inner_func = outter_func()
# inner_func()


# def func():
#     c = 2
#     def inner_func():
#         d = 4
#         print(locals())
#     print(locals())
#     inner_func()

# func()
# print(globals()(['a'])

# def func():
#     c = 2
#     def inner_func():
#         d = 4
#         print('2')
#     print('hello')
#     inner_func()
# func()


# x = 0

# def counter():
#     global x
#     print(x)
#     x+=1
# counter()
# counter()
# counter()
# counter()
# counter()


# def func1(a):
#     a= a+ 10
#     def func2():
#         nonlocal a
#         a = a + 100
#         def func3():
#             nonlocal a
#             a = a+1000
#             return a
        
#         return func3()   
    
    
#     return func2()

# print(func1(5))
# func1(5) -> 115

"""
Classwork
Классная работа
"""
"""
1) Есть глобальная переменная, которая обозначает размер самой главной первой матрешки. 
Напишите функцию, в которой к размеру главной матрешки прибавляется размер второй матрешки, который определен в этой функции. 
То же самое сделайте и с третьей функцией внутри второй. Верните результат сложения.
"""
# писать код здесь

# a = 100
# def func2():
#     global a
#     a2 = 50
#     a=a+a2
#     def fenc3():
#         global a
#         a3=25
#         a= a+a3
#         return a
#     fenc3()
# func2()
# print(a)
    
"""
2) Есть глобальная переменная, которая содержит пустой список. 
Вам необходимо написать функции, одна из которых add() - добавляет в этот список имена, которые вводит пользователь. 
А другая функция remove() - удаляет эти имена из списка по индексу, который вводит пользователь. 
Вызовите функции в рандомном порядке 10 раз и в конце выведите список.
"""
# писать код здесь


# a = []
# def add():
#     global a
#     names = input('Enter the name: ')
#     a.append(names)
# def remove():
#     global a
#     index = int(input('Enter the index of names, which you want to delete: '))
#     a.pop(index)
#     print(a)
#     return a

# add()
# add()
# add()
# add()
# remove()
# add()
# add()
# add()
# remove()
# add()



"""
Task
Таски
"""
"""
1.Вам дана вложенная функция:

def foo():
    var = 'переменная foo'
    def bar():
 
        . . .
 
    bar()
print("переменная в foo: ", var)
Внесите изменения в функции bar таким образом чтобы при вызове функции foo и при попытке распечатать переменную var 
в глобальной области видимости, выводился сдедующий результат:

foo()
print("переменная в foo: ", var)
Output:

переменная в foo:  переменная foo
переменная в foo:  переменная bar
"""

# def foo():
#     var = 'переменная foo'
#     def bar():
#         global var 
#         var = 'переменная bar'
#     print("переменная в foo: ",var)
#     bar()
# foo()
# print("переменная в foo: ", var)





"""
2. вас есть глоабльная переменная x со значением Я глобальная переменная!. 
Напишите функцию my_func()которая изменяет значение этой переменной на Я могу изменяться, 
т.е если вы после вызова функции распечатаете переменную x вне функции она должна возвращать вам значение Я могу изменяться.

Пример:

my_func()
print(x)
Output:

Я глобальная переменная!
Я могу изменяться
Затем чтобы удостовериться что вы изменили именно глобальную переменную выведите в консоль словарь глобальных имен.
"""

# x = 'Я глобальная переменная!'

# def my_func():
#     global x
#     x = 'Я могу изменяться'
# print(x)
# my_func()
# print(x)
# print(globals())

"""
3.Дана глобальная переменная num со значением 3. Напишите функцию mul которая будет возвращать квадрат этой переменной и записывать результат 
в глобальную переменную num. Вызовите функцию три раза, и распечатайте переменную num.

mul()
mul()
mul()
print(num)
Output:

6561
тaк кaк num перезаписали на 9(3*3 = 9) затем на 81

(99 = 81) и после на 6561(8181 = 6561)
"""
# num = 3
# def mul():
#     global num
#     num = num**2
# mul()
# mul()
# mul()
# print(num)

"""
4.Напишите небольшую программу для подсчета доходов и расходов.

У вас есть глобальная переменная balance = 0 общий счет.

Программа должна состоять из трех функций: 
get_salary(amount) - функция для увеличения баланса, которая принимает в 
аргументы amount - заработная плата и увеличивает переменную balance на число переданное в amount.

pay_bills(amount, log_name) - уменьшает баланс на количество amount , 
log_name - принимает строку - на что были потрачены деньги и распечатывает результат, например если мы вызвали pay_bills(300, 'интернет')

функция распечатывает строку в виде

"Вы заплатили 300 сом за интернет"
И функция get_balance(), которая будет распечатывать вам строку:

У вас на счету `n` сом
где n - это текущее значение глобальной переменной balance.

Вызовите функции в данном порядке:

get_salary(1000)
get_balance()
pay_bills(400, 'кабельное тв')
get_balance()
Результат в консоли:

У вас на счету 1000 сом
Вы заплатили 400 сом за кабельное тв
У вас на счету 600 сом
"""
# balance = 0

# def get_salary(amount):
#     global balance
#     balance +=amount
    
# def pay_bills(amount,log_name):
#     global balance
#     balance -=amount
#     print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     global balance 
#     n = balance
#     print(f'У вас на счету {n} сом')


# get_salary(1000)
# get_balance()
# pay_bills(400,'кабельное тв')
# get_balance()

"""
5.В Python есть встроенная арифметическая функция pow(), pow принимает два обязательных аргумента x, y и один необязательный z и
возвращает результат в виде x**y % z - возводит первое число в степень y и если передано третье число, делит результат на третье число и 
возвращает остаток.

Пример использования pow:

print(pow(2,3))
# 8 - тaк кaк 2**3 = 8
print(pow(2, 3, 3))
# 2 - т.к 2**3 = 8, а остаток от деления 8 % 3 = 2
У вас есть глобальная переменная result = 0. Напишите функции pow_first(x,y), отвечает за первую часть встроенной функции pow и pow_second(z), 
отвечает за вторую часть pow(z). Вызовите эти функции, а затем выведите переменную result.

Пример:

pow_first(2, 3)
pow_second(3)
print(result)
Output:

2
"""
# result = 0
# def pow_first(x,y):
#     global result
#     result = x**y
# def pow_second(z):
#     global result
#     result =result %z
#     print(result)
# pow_first(2,3)
# pow_second(3)

"""
6.Мурат с друзьями на выходных решил собратся и пойти в ночной клуб.Но в ночной клуб пропускают только тех, кому 17+. 
Создайте словарь ключами которого являются имена Мурата и его друзей, а значениями являются их возраст.

a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
Напишите программу которая определяет кого пустить в ночной клуб а кого нет.

Output:

Мурат, Вы можете войти в клуб
Эржан, Вы можете войти в клуб
Чынгыз, Вы можете войти в клуб
Алтынай, Вы можете войти в клуб
Асема, извините, Вы не проходите по age-control
"""
# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def age_control():
#     global a
#     for key,value in a.items():
#         a[key]=value
#         if value >=17:
#             print(f'{key}, Вы можете войти в клуб')
#         else: 
#             print(f'{key}, извините, Вы не проходите по age-control')
# age_control()
      
        
"""
7.Вам дан список a из нескольких имён в нижнем регистре. Напишите программу которая превращает имена из списка в имена, 
где первая буква имени в верхнем регистре.Запишите результат в новый список b и выведите переменную b.

Пример:

 a: ['pipi', 'papa', 'mama']
 
 b: ['Pipi', 'Papa', 'Mama']
"""
# a = ['pipi', 'papa', 'mama']
# def capital():
#     global a
#     b =[]
#     for i in a:
#         b.append(i.capitalize())
#     return b

# b =capital()
# print(b)

"""
8.Напишите функцию count_symbols() которая принимает строку и возвращает количество гласных, согласных букв и остальных символов.
Используйте только кириллические символы. Распечатайте вызов функции.

Пример:

print(count_symbols('Мурат супер!'))
output:

Количество гласных: 4, согласных: 6, остальных символов: 2
"""

# def count_symbols(string):
#     res1 =0
#     res2 = 0
#     res3 =0
#     vowels = ['у','е','а','о','э','я','и','ю','ы']
#     consonants = ['й','ц','к','н','г','ш','щ','з','х','ъ','ф','в','п','р','л','д','ж','ч','с','м','т','ь','б']
#     symbols = ['!','"','№',';',':','?','*',',','(',')','_','-','=','+','/','.',' ']
#     for i in string.lower():
#         for v in vowels:
#             if i == v:
#                 res1 += i.count(v)
#         for c in consonants:
#             if i == c:
#                 res2+=i.count(c)
#         for s in symbols:
#             if i ==s:
#                 res3+= i.count(s)
#     print(f'Количество гласных: {res1},согласных: {res2}, остальных символов: {res3}')
# count_symbols('Мурат супер!')
        

"""
7.Вам дан список a из нескольких имён в нижнем регистре. Напишите программу которая превращает имена из списка в имена, 
где первая буква имени в верхнем регистре.Запишите результат в новый список b и выведите переменную b.

Пример:

 a: ['pipi', 'papa', 'mama']
 
 b: ['Pipi', 'Papa', 'Mama']
"""
# a = ['pipi', 'papa', 'mama']
# def capital():
#     global a
#     b =[]
#     for i in a:
#         b.append(i.capitalize())
#     return b

# b =capital()
# print(b)

"""
8.Напишите функцию count_symbols() которая принимает строку и возвращает количество гласных, согласных букв и остальных символов.
Используйте только кириллические символы. Распечатайте вызов функции.

Пример:

print(count_symbols('Мурат супер!'))
output:

Количество гласных: 4, согласных: 6, остальных символов: 2
"""
# def count_symbols(string):
#     res1 =0
#     res2 = 0
#     res3 =0
#     vowels = ['у','е','а','о','э','я','и','ю']
#     consonants = ['й','ц','к','н','г','ш','щ','з','х','ъ','ф','в','п','р','л','д','ж','ч','с','м','т','ь','б']
#     symbols = ['!','"','№',';',':','?','*',',','(',')','_','-','=','+','/','.',' ']
#     for i in string.lower():
#         for v in vowels:
#             if i == v:
#                 res1 += i.count(v)
#         for c in consonants:
#             if i == c:
#                 res2+=i.count(c)
#         for s in symbols:
#             if i ==s:
#                 res3+= i.count(s)
#     print(f'Количество гласных: {res1},согласных: {res2}, остальных символов: {res3}')
# count_symbols('Мурат супер!')


# этот принимает на платформе

# def count_symbols(string):
#     res1 =0
#     res3 = 0
#     vowels = ['у','е','а','о','э','я','и','ю','ы', 'ё']
    
#     for i in string.lower():
#         if i in vowels and i.isalpha():
#             res1 += 1
#         elif not i.isalpha() :
#             res3 += 1
    
#     res2 = len(string) - res1 - res3
    
#     return f'Количество гласных: {res1},согласных: {res2}, остальных символов: {res3}'

# print(count_symbols('Мурат супер!'))
        

"""
9.Создайте пустой список a. Напишите программу которая должна записывать в ваш список числа от 0 до 10. 
Распечатайте переменную a.
"""
# a = []
# def add():
#     global a
#     for i in range(0, 11):
#         a.append(i)

# add()
# print(a)

"""
10.Определите перемнную a в котором будут хранится список из целых чисел.

a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
Напишите программу которая выводит все элементы этого списка, которые меньше 7.
"""
# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# def func():
#     global a
#     for i in a:
#         if i<7:
#             print(i)
# func()

"""
Молодец!!!
Тема пройдена.
"""