"""
Закончен
День 3. Неделя 3. 3 ноября.
Тема: Встроенные функции

Язык Python включает множество уже определенных, то есть встроенных в него функций. При этом программист не видит этих определений, 
так как они скрыты где-то в недрах языка. Для нас достаточно знать , что эти функции принимают и возвращают. 
То есть их интерфейс.

* Функция map() принимает 2 аргумента. 
Первый аргумент - это функция, второй - итерируемый объект map() применяет к каждому элементу итерируемого объекта, переданного втроым аргументом, 
функцию, которую мы передали первым элементом.

map(cook,[1234]) => [!@#$]

* Lambda - это анонимная функция.
Отличается от обычной функции тем, что является однострочным выражением и не имеет названия

* filter() отвечает за фильтрацию итерируемого объекта. Она принимает два аргумента: первый - это функция, 
второй - итерируемый объект, который необходимо отфильтровать.

filter() оставляет в итерируемом объекте только те элементы, для которых функция, переданная первым аргументом возвращает истину - True.

* reduce() - 

Начало практики:

Встроенные функции:

print()
input()
int(),str(),list(),bool(),dict(),tuple(),set(),frozenset()
sum()
min(),max()
sorted()

"""

"""
#map(func,iterable object) - пермый объектвым элементом передается функция, вторым итерируе

"""
# list_str = ['1','2','3','4','5']
# list_int = list(map(int,list_str))
# print(list_int) #[1, 2, 3, 4, 5]

"""
Пример работы map с функцией:
"""
# def capital(word: str) -> str:
#     return word.title()

# list_names = ['john','raychel','sam','fay']
# new_list = list(map(capital,list_names))
# print(new_list) #['John', 'Raychel', 'Sam', 'Fay']


"""
Пример с функцией
Конвертер доллара в сомы
 -> аннотация типов(необязательно писать)
"""
# def dollars_to_soms(dollars:int):
#     return f'{round(dollars * 84.80)} soms'

# dollars = [100,34,56,78,97,34]

# soms = list(map(dollars_to_soms,dollars))
# print(soms)

"""
lambda - анонимная функция 
Не поддерживает аннотацию типов
"""
# print((lambda x: x**2)(10)) #100

# square = lambda x: x**2
# print(square(46)) #2116

"""
Функция lambda возвращает столько аргументов, сколько объявлено параметров
"""

# print((lambda x,y,z: x + y + z)(1,2,3)) #6

"""
lamda + map

"""
# list1 = [1,2,3]
# list2 = [4,5,6]

# new_list = list(map(lambda x,y : x+y, list1,list2))
# print(new_list) # [5, 7, 9]

"""
Сравним циклы, генераторы и map

"""
# num_list = [2,6,8,7,9,1,4]



# num_list2 = []
# for i in num_list:
#     num_list2.append(i * 2)

# print(num_list2)


# num_list2 = [i*2 for i in num_list]
# print(num_list)


# num_list2 = list(map(lambda i:i*2,num_list))
# print(num_list2)

"""
filter - фильтрует список по тру и фалс

"""
# names = ['john','alice','amber','ayche','sam','arnold']

# new_list = list(filter(lambda name: name.startswith('a'),names))
# print(new_list) #['alice', 'amber', 'ayche', 'arnold']

"""
Пример с числами
"""
# numbers = [4,5,67,3,53,24,34,12,15]
# filtered_numbers = list(filter(lambda num: num%3==0,numbers))
# print(filtered_numbers) #[3, 24, 12, 15]
"""
Пример с словарями
"""
# dict1 = [{'subject':'python','point':98},
#             {'subject': 'javascript','point':89},
#             {'subject':'python','point':100}]
# dict_new = list(filter(lambda x:x ['subject']== 'python',dict1))
# print(dict_new)


# users = [{'username':'Alice123','comment':['I love it']},
#         {'username':'Sam34','comment':[]},
#         {'username':'John','comment':[]},
#         {'username':'Ray12','comment':['hehe']}]
# active_users = list(filter(lambda x: x.get(['comments'],None), users))
# inactive_users = list(filter(lambda x: not x.get(['comments'],None),users))
# print(f'This user are active {active_users}, This users are not active {inactive_users}')


"""
map+lambda+filter

"""
# names = ['Harry Potter','Alic','Sandra','Moly','Tim']
# greetings = list(map(lambda name:f'Welcome, {name}',filter(lambda x: len(x)>=8,names)))

# print(greetings)


"""
reduce(func,iterable object) - возвращает единичное выражение

В данном примере видно. что reduce сперва складывает первые два числа, потом первые два и третее и так далле

Анонимные функции используют, чтобы объявить функцию на месте её использования.
"""
# import functools
# numbers = [1,2,3,4,5]
# sum_ = functools.reduce(lambda x,y: x+y,numbers)
# print(sum_) #15



# import functools
# numbers = [13,4,5,6,7,-100,56,34,2003]
# max_ = functools.reduce(lambda a,b : a if a>b else b,numbers)
# print(max_) #2003


"""
Reduce было вычеркнуто, потому что замедляет программу
"""
# from functools import reduce
# numbers = [5,6,8,1,2]
# multipli = reduce(lambda x,y: x*y,numbers)
# print(multipli) #480


"""
zip() - создает итератор, который объединяет элементы из нескольких источников данных. 

Работает только до тех пор, пока не исчерпается самая короткая последовательность.

"""
# list_a = [1,2,3,4,5,6]
# list_b = ['a','b','c','d','e']
# list_c = ['makers','john','boot','zip','fg']

# zipped_list = list(zip(list_a,list_b,list_c))
# print(zipped_list) #[(1, 'a', 'makers'), (2, 'b', 'john'), (3, 'c', 'boot'), (4, 'd', 'zip'), (5, 'e', 'fg')]

# unzipped = list(zip(*zipped_list))
# print(unzipped) #[(1, 2, 3, 4, 5), ('a', 'b', 'c', 'd', 'e'), ('makers', 'john', 'boot', 'zip', 'fg')]
# list_numbers,list_letters,list_str = list(zip(*zipped_list))
# print(list_numbers)
# print(list_letters)
# print(list_str)


"""
dir(obj) - выдает список и методов.

"""
# print(dir(__builtins__))

"""
enumerate() - функция, которая создает кортеж из нумерации и то-что вы ей даете

"""
# seasons = ['spring','winter','fall','summer']
# enumerated_seasons = dict(enumerate(seasons, start =4*2))
# print(enumerated_seasons)

"""
abs - возвращает абсолютное значение числа(модуль)

"""
# negative = -1234
# absolute =abs(negative)
# print(absolute)

"""
all - являются все элементы True

"""
# list_of_zeroes = [0,0,0,0,0]
# is_true = all(list_of_zeroes)
# print(is_true) #False

"""
any - если хотя бы один элемент возвращает True

"""
# list_ = [0,1,0,0,0]
# is_true = any(list_)
# print(is_true) #True

"""
ascii -  возвращает строковое представление объекта с экранированными не-ASCII символами

"""
# list_1 =['makers','мэйкерс',23,0]
# list_2 = ascii(list_1)
# print(list_2) #['makers', '\u043c\u044d\u0439\u043a\u0435\u0440\u0441', 23, 0]
"""
ord() - возвращает номер символа по таблицк ascii
chr() - по номеру возвращает символ
"""
# print(ord('b'))
# print(chr(98))
"""
divmod() - возвращает(x//y, x%y)

"""
# print(divmod(45,5))


"""
eval - выполнение выражений
"""
# a = 'print(10)'
# eval(a) #10

# a1 = 'raise VallueEror'
# eval(a1)

"""
exec() - проверяет и выполняет блок кода.
"""
# a = 'a1 = (1,2,3,4,5)\nfor num in a1:\n\tprint(num*10)'
# exec(a)

# a = 'a1 = (1,2,3,4,5)\nfor num in a1\n\tprint(num*10)'
# exec(a) #SyntaxError
"""
isinstance() - проверяет принадлежит ли объект экземпляром этого класса

type() - выдает название класса, к которому относится объект

"""
"""

"""

"""
Конец практики!

Classwork
Классная работа

"""
"""
1) Создайте список, который будет содержать различные типы данных. 
Напишите программу, которая будет находить корень чисел, содержащихся в созданном списке. Используйте встроенные функции.
"""
# писать код здесь

# from math import sqrt
# list1 = [25,49,45,'frf',{'f':45},True,False]
# result = list(map(lambda x: round(sqrt(x)), filter(lambda y: type(y)==int,list1)))
# print(result) #[5, 7 ,7]

# from functools import reduce
# list_ = [1, 2, 3, 4]  
# result = reduce(lambda x,y: x+y,list_)
# print(result)


"""
2) Реализуйте следующую программу: есть студенты, которые сдали экзамен. 
Вам необходимо сохранить имена и баллы тех студентов, которые не прошли проходной балл (<60). 
Далее каждому студенту вам необходимо отправить письмо, которое говорит о том, что этого студента собираются отчислить.
"""
# писать код здесь
# list_of_students = [{'name':'Alice','score':90},{'name':'John','score':45},{'name':'Linda','score':59},{'name':'Tim','score':21}]
# list_fool = list(filter(lambda x: x['score']< 60,list_of_students))
# names = list(map(lambda x: x['name'],list_fool))
# points = list(map(lambda x: x['score'],list_fool))
# zipped_list = list(zip(names,points))
# # print(zipped_list)
# result = f'Dear {zipped_list[0][0]}, we want to inform you that with your score {zipped_list[0][1]} behind the average we want to exlude you. Please go to the office if you have any questions.'
# result2 = f'Dear {zipped_list[1][0]}, we want to inform you that with your score {zipped_list[1][1]} behind the average we want to exlude you. Please go to the office if you have any questions.'


# print(f'{result}\n{result2}')
"""
3) Создайте список с буквами. Напишите программу, которая склеит все буквы с вписке в строку. 
Не использовать метод join() и циклы.
"""
# писать код здесь

# from functools import reduce
# list_of_letters = ['a','b','s','f','g','o','z']
# joined_list = reduce(lambda x,y: x+y,list_of_letters)
# print(joined_list)

"""
Таски 
Task

"""
#1

# list_ = [1, 2, 3, 4]  
# result = sum(list_)
# print(result)

"""
2.Создайте переменную list_ и сохраните в нем список из чисел. Проверьте, что все числа больше трёх, результат сохраните в новой переменной result и 
выведите в консоль. Используйте встроенную функцию.

Пример:

list_ = [1, 5, -9, 6, -4] 
Вывод:

False 
Пример:

list_ = [5, 8, 4, 6, 7] 
Вывод:

True 

"""
# list_ = [1, 5, -9, 6, -4] 
# result = all( i>3 for i in list_)
# print(result)


"""
3.Создайте переменную list_ и сохраните в нем список из чисел. Проверьте, что в нём есть отрицательные числа, 
результат сохраните в новой переменной result и выведите в консоль.

Пример:

list_ = [5, 8, 4, 6, 7]
Вывод в терминал:

False 
Используйте встроенную функцию.

"""
# list_ = [5, 8, 4, 6, 7]
# result = any(i<0 for i in list_)
# print(result)

"""
Создайте переменную list_ и сохраните в нем список из чисел. Создайте новый список, состоящий из квадратов этих чисел, 
результат сохраните в новой переменной result и выведите в консоль.

Пример:

list_ = [1, 2, 3, 4]  
Вывод:

[1, 4, 9, 16]  
Используйте встроенную функцию.

"""
# list_ = [1, 2, 3, 4] 
# result = list(map(lambda x: x**2, list_))
# print(result)
"""
5.Создайте переменную list_ и сохраните в нем список из чисел. Отфильтруйте этот список, оставив только чётные числа, 
результат сохраните в новой переменной result и выведите в консоль.

Пример:

list_ = [1, 2, 3, 4] 
Вывод:

[2, 4] 
Используйте встроенную функцию.

"""
# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda x: x%2 ==0, list_))
# print(result)
"""
6.Создайте переменную list_ и сохраните в нем список со строками. Отфильтруйте этот список, оставив только те строки, длина которых больше 7 символов. 
Результат сохраните в новой переменной result и выведите в консоль.

Пример:

list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
Вывод:

['inheritance', 'polymorphism'] 

"""
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda x: len(x)>7,list_))
# print(result)

"""
7.Создайте переменную list_ и сохраните в нем список из чисел. Выведите произведение всех этих чисел.
Результат сохраните в новой переменной result и выведите в консоль. Используйте встроенную функцию.
Пример:

list_ = [5, 6, 7, 8] 
Вывод:

1680 
Используйте встроенную функцию.

"""
# from functools import reduce
# list_ = [5, 6, 7, 8] 
# result = reduce(lambda x,y: x*y,list_)
# print(result)


"""
8.Создайте переменную list_ и сохраните в нем список из чисел. Посчитате количество чётных и нечётных чисел в этом списке. 
Результат сохраните в новой переменной result и выведите в консоль в виде строки:

even: количество_четных, odd: количество_нечетных

Пример:

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
Вывод:

even: 5, odd: 5 
Используйте встроенную функцию.

"""
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# even = list(filter(lambda x: x%2 == 0,list_))
# odd = list(filter(lambda x:  not x%2 == 0,list_))
# result = f'even : {len(even)}, odd: {len(odd)}'
# print(result)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11,13,15 ] 
# even = len(list(filter(lambda x: x%2 ==0,list_)))
# odd = (len(list_) - even)
# result = f'even : {even}, odd: {odd}'
# print(result)

"""
9.Создайте переменную list_ и сохраните в нем список из чисел. Если число в списке меньше 0, замените его на False, если больше, то на True. 
Результат сохраните в новой переменной result и выведите в консоль.

Пример:

list_ = [-1, 2, 3, 5, -3, 7, ] 
Вывод:

[False, True, True, True, False, True] 
Используйте встроенную функцию.

"""
# from functools import reduce
# list_ = [-1, 2, 3, 5, -3, 7, ] 
# result = list(map(lambda x: True if x>=0 else False,list_))
# print(result)

"""
10.Создайте переменную list_ и сохраните в нем список со строками. Найдите самое длинное имя из списка функцией reduce. 
Результат сохраните в новой переменной result и выведите в консоль.

Пример:

list_ = ['Paul', 'George', 'Ringo', 'John'] 
Вывод:

George 
Используйте встроенную функцию.

"""
# from functools import reduce
# list_ = ['Paul', 'George', 'Ringo', 'John']
# result = reduce(lambda x,y: x if len(x)>len(y) else y,list_)
# print(result)

"""
Начало разбора

"""
# result = list(map(lambda x,y: x+y,[1,2,3]))
# print(result)

"""
int - десятиричная система
"""

# a = 20
# print(bin(a)) #0b10100
# print(oct(a)) #0o24
# print(hex(a)) #0x14

# a1 = [3,45,67,3,21]
# a2 = ['Janw','George','Tim','Bob']
# print(sorted (a1, reverse = True))
# print(sorted(a2,key = len))

"""
reversed - расставляет элементы в обратном порядке 

"""
# a = [4,2,1]
# reversed(a)
# a[::-1]



# a = [1,2,3,4,5,6]

# def square(num):
#     return num**2

# res =[]
# for num in a:
#     res.append(square(num))
# print(res) #[1, 4, 9, 16, 25, 36]


# from functools import reduce
# a = ('Tim','Jane','Andy','Kyle','John','Sam')

# min_element = reduce(lambda x,y : x if x<y else y,a)
# print(min_element) #Andy

# print(min(a)) #Andy



"""

"""

"""


"""

"""


"""

"""


"""

