"""   
Незакончена классворк и таски не все
День 5.Неделя  1
Тема: Логические операции  

"""

"""Простейшее булевое выражение"""
# print(4>3)
"""
считаются порядковые значению для сравнения строк. Можно посмотреть по Unicode. 
"""
# print('makers' > 'bootcamp')
""" Заглавные буквы имеют порядкое значени меньше, чем строчные"""  
# print('m'> 'M')

"""
ord() производит сравнению по первой букве, 
Python смотрит только на первую, на остальне внимания обращает, пока первые символы различны. 
Учитывается порядковое значение, которое считается с помощью функции ord
Но если первые числа равны, то считываются другие пока питон не найдет различие и не сравнит эти символы
"""
# print(ord('b'))

"""
chr() -(character) функция, выполняет противоположную функциrd(),
 передаем порядковый номер и получаем букву
 """

# print(chr(98))


""" in - проверка на вхождение"""
""" is - проверка на идентичность.Но нельзя сравнивать два числа, 
но можно использовать для сравнения объекта их расположения с помощью функции id()
Списки тоже можно тоже сравнивать используя эту функцию
"""

# list_ = [11,42.64,59]

# if not 20 in list_: #True
#     print('YES')  

# if not 20 in list_ and 11 in list_: # True
#     print('YES')


# if not 20 in list_ or not 11 in list_: # True
#     print('YES')

# a = None
# if a is not None:
#     print('...)

# if a:
#     print('...')  


"""isupper(), islower(),startwith
# isinstance()- функция, проверяющая относится ли объект к определленому классу
a= 20
# isinstance(a,int) #True 
# isnistance(a,str) #False
"""

"""
issubclass(class1, class2)- проверяет, является ли class1 потомком class2
Типо множества и подмножества. Потомок-подмножество который class 2

""" 
# class A:
#     pass
# class B(A):
#     pass

# class C:
#     pass

# issubclass(B,A) #True
# issubclass(C,A) #False



"""
Проверяем тип данных. Булевый тип данных имеет только два значения: True и False
Которые равны 1 и 0 соответсвенно, можно проверить это с помощью ф-ции int()
"""

# print(type(True))
# print(type(False))

# a = True
# b = False
# print(int(True))
# print(int(False))

"""
Преобразуем из одного типо данных в булевое с помощью функции bool()
Все, что не является 0 и не равно пустотой - True
False - это 0, "",[],{}, set(), frozenset(), None(), False
То есть пустота, 0 и пустые списки, кортежи и т.д. 
"""
# print(bool(3.4))
# print(bool(-200))
# print(bool(0))
# print(bool(' '))
# print(bool(""))

"""
Логические операторы:
> < <= >= == =! 
Проверим их
Заметка == и = нельзя путать!!!
== это для сравнения, а = - это присваивание

"""
# a=10
# b=7
# print(a+b>15) #False
# print(a<20 -b) #True
# print(a<=20 -b ) #True
# print(a!=b) True
"""Сперва выполнятся == сравнение, а потом ="""

# c = a == b False
# print(c)

#  and, or
"""
and-Логическая операция, выдает соотвествующее значени T или F, если оба или больше условия 
выдают истину или ложь соответсвенно
or -выполняется если одно из двух выдает истину, то выводит False
match case(swith case)-

""" 


# a=15
# b=25
# # print(a >=15 and b<30 ) #True because two of them are True
# # print (a< 10 or b>30) #False, because two of them are False
# print(a>=10 or b>=30) #True, because one of them is True
"""
# not
Унарный оператор True => False, False => True, отличается от бинарного and или or
"""
# x=20
# print(not x >10) #False, because it was True and we converted it in False
# print(not x == 10) #True, because it was False and became True 

# match case(swich case)

# num = 100
# match num:
#     case 10:
#         ....
#     case 20:
#         ...
#     case 30:
#         ...
#     case _:
#         ...

# if num == 10:
#     ...
# elif num==20:
#     ....
# elif num == 30:
#     ....



"""
Пример
"""
# a = True
# b = False
# print(not a)
# print(not b)

"""
Условные операторы if, elif, else

 if condition is True:
     some code 1
some code 2

Самое простое использование условных операторов

if condition is True:
    some code 1
elif condion id True:
    some code 3    
else:
    some code 2
Если использовать данную конструкцию, то сработает только одно условие

"""
# a=20
# if a>20: # False, return nothing because a=20, but not greater than it
#     print('a is greater than 20')
# elif a==20: # True, so print this string, because a=20
#     print('a is equal to 20')
# else:
#     print('a is less than 20') # false, but return nothing but a>20

# a=23
# if a>30 : 
#     if a>40: 
#         print('a is greater than 40')
#     else:
#         print('a is greater 20')
# elif a==20: 
#     print('a is equal to 20')
# elif a>20 and a<40:
#     print('a is greater than 20, but less than 40') 

# else:
#     print('a is less than 20') 


# a = 10
# b = 5 
# c =20

# if a > b and b > c : 
"""" 10 > 5 it return True, 5 > 30 is false, because we use and it all returns False"""
#      print('MAKERS')
# else: 
#     print('makers')


# if a > b and b < c :
#     print('MAKERS')
"""
all condions was satisfied, we get MAKERS 
"""
# else: 
#     print('makers')


# if a > b or b > c : 
#     print('MAKERS')
# else: 
#     print('makers')
"""
one condion was satisfied
"""

# if not( a > b and b < c): 
#     print('MAKERS')
# else: 
#     print('makers')
"""
we get 'makers', because not convert True to False and we get second condition

"""
# num =158
# if num >0 and num <40:
#     value(' очень слабо')
# else:
#     if num>=40 and num <80:
#         print('слабо')
#     else:
#         if num>= 40 and num <= 80:
#             value('средне')
#         else:
#             if num>=80 and num <= 120:
#                 value('нормально')
#                 else:
#                     if num> 120 and num < 140:
#                         value('сильно')
#                     else:
#                         print('dangerous')






# можем проверять не пустаz ли строка, кортеж или список 

# a = (1,2,3,4,5,6)
# if len(a) > 0:
#     print('not 0')

# if bool(a):
#     print('...')

# if a:
#     print('...')





"""
Тернарный оператор - является выражением и является сочетанием   if и else
Записывается одной строкой вместо длииной конструкции с if
""" 

# expression_true if condion else expression_false

# Стоит помнить, что использовать тернаhный оператор 
# при использовании нескольких if или больших конструкциях, так как 
# код станет нечитаемым.

# a = True #True, because a = True
# print( a if True else False)

# a = 'MAKERS'
# b = 10


# print (a if b >0 else 'makers') 

# # MAKERS because first condion was cotented(удовлетворенно)
# a = 'MAKERS'
# b = 10

# print (a if b else 'makers') # так как b в буллевом значение 
# #не равно нулю или пустоте мы получаем первое условие
# print(bool(b))


"""Альтернативная форма тернарного оператора:
(expression_false,expression_true) [condition]
Иммет такой вид 
В круглых скобках мы имеем кортеж, в котором два элемента
, то в квадратных скобках это индекс
Идет обращение по индексу 0, если ложь и 1, если истина
"""
# a = 10
# print(('negative','positive') [a >= 0]) # positive, if a>10 and we have true
# # negative, if a =< 10 and we have false

"""
NoneType - имеет нулевое или нейтральное значение

"""
# print(type(None)) #class NoNeType
# null_variable = None
# not__null_variable = 'MAKERS'

# if null_variable is None: #This is None
#      print('This is None')
# else: 
#     print('This is not None')

# print(id(null_variable))
# print(id(None))

# if not__null_variable is None: #This is not None
#      print('This is None')
# else: 
#     print('This is not None')


# if null_variable : #This is not None
#      print('This is None')
# else: 
#     print('This is not None')

# if not null_variable : #This is None
#      print('This is None')
# else: 
#     print('This is not None')

""" 
range(num1, num2) - последовательность чисел.Можно задавать даже шаг к примеру range(0,100,2)

""" 

"""
Classwork
Классная работа 
По теме: Логические и условные Операторы
"""
"""
1) Создайте программу, которая будет требовать пароль и проверять, 
содержатся ли в нем только числа, при этом длина пароля не должна быть менее 8 символов . 
Если все эти условия выполняются, то программа выдает вам сообщение ‘Ваш пароль сохранен’, если же нет - то программа должна 
указать необходимое условие для сохранения вашего пароля.

Например:
Ввод: Введите пароль: Makers12345
Вывод: Ваш пароль должен хранить только числа

Ввод: Введите пароль: a12345
Вывод: Ваш пароль должен содержать не менее 8 символов
Ваш пароль должен содержать только буквы

"""
#писать код здесь
# password = input('Введите пароль: ')

# if password.isdigit() and len(password) >=8:
#      print('Ваш пароль со')

# if not password.isdigit():
#     print('Ваш пароль должен содержать только числа')

# if not len(password) >=8:
#     print("Ваш пароль должен быть не менее 8 символов")

    

"""
2) Напишите программу, которая должна рассчитывать средний балл по следующим предметам: математике, английскому языку и литературе. 
Проходной балл составляет более 69 баллов. 
Если ученик набрал проходной балл, то ему выдается сообщение о том, что он допущен к экзаменам. 
Если он не набрал нужное количество баллов, то ему выдается сообщение о том, что у него недопуск к экзаменам.

Например: 
Ввод: Введите свои баллы по математике, английскому языку и литературе через запятую: 78, 90, 67
Вывод: Вы допущены к экзаменам. Ваш средний балл составляет 78.3 

"""
#писать код здесь
# point = input(' Введите свои баллы по математике, английскому языку и литературе через запятую: ').split(,)





"""
3) Напишите мини-игру Камень-Ножницы-Бумага. Вы играете с компьютером. Для этого используйте встроенный модуль random.

Например:
Ввод: Ваш выбор: Камень
Выбор компьютера: Ножницы
Вывод: Вы выиграли!

Ввод: Ваш выбор: Бумага
Выбор компьютера: Ножницы
Вывод: Вы проиграли!
"""




# Task8.Logical

# x = int(input())
# y = int(input())
# if x % y > 0:
#     print(f'x не делится на y')
# else:
#     print(f'x делится на y')


#Task9

# print(f'Частное: {x//y}')
# print(f'Остаток:{x%y}')
# year = int(input())
# if year%4 == 0 and year%400 ==0 and year%100 != 0:
#     print('YES')
# else:
#     print('NO')

#Task10


# nums = [1,2,3,4,5,7]
# target =int(7)
# if target in nums:
#     print('Да')
# else:
#     print('Нет')

#Task 11

# num = int(input())
# if str(chr(num)).isalpha() == True :
#     print(f'Это буква "{chr(num)}"')   
# else:
#     print(f'Это не буква, а символ "{chr(num)}"')

# count = 0
# number =input()
# if (number).isdigit() == True :
#     print(count == int(number))