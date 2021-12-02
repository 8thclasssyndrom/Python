"""
Закончен
День. Неделя вторая. 25 октября
Тема: Список в Python
Список - это изменяемый упорядоченный набор произвольных элементов.
Поэтому это не почти не массив

a = []
a =list()

"""
# numbers = []
# numbers2 =list()
# print(type(numbers))
# print(type(numbers2))


""" 
Элементы списка можно изменять удалять, изменить и заменять.
Порядок в списках нужно для упорядоченности и правильному выполнению действий
В других языках это массив.
"""

#list1 = ['Meat', 'Milk', 'bread', 'ffr']


# numbers4 = [1,2,3,4,5]
# numbers5 =list(numbers4)
# print(type(numbers5))
# print(numbers5)

"""
Размножение списков c помощью умножения *

"""

# numbers =[7,7,7,7,7,7]
# numbers2 = [7]*6
# print(numbers)
# print(numbers2)

"""
range() - 
"""

"""
1. range(end)- она обязательна должна принимать один элемент при этом 
этот элемент в список не включается

"""


# numbers = list(range(10))
# print(numbers)

"""
2.range(start,end) - включает первый элемент, но не включает последний

"""
# numbers = list(range(1,10))
# print(numbers)
"""
3.range(start,end,step) - в список попадает каждый элемент  с шагом step

"""

# numbers= list (range(1,10,2))
# print(numbers)

# numbers = list(range(10,0,-2))
# print(numbers) 


"""
in - проверка на вхождение

"""
# list = [12,34,45,56,65]

# value1 = 12
# value2 =23

# print(value1 in list) #True
# print(value2 in list) #False


"""
for item in range()
in - проверка на вхождение
i(Итерация)-первое вхождение

"""

# for i in range(1,11):  # => 1,2,3,4,5,6,7,8,9,10,11
#     print(i**2)



"""
Сравнение списков
Два списка считаются равными, если все их элементы равны

"""
    
# numbers1 = [1,2,3,4,5]
# numbers2 = [1,2,3,4,5]

# print(numbers1 == numbers2) #True

# numbers1 = [1,2,3,4,5,11]
# numbers2 = [1,2,3,4,5]

# print( numbers1 > numbers2 ) #True

# numbers1 = [1,2,3,4,5,11]
# numbers2 = [1,2,3,4,5,9,100]

# print(numbers1 > numbers2) 
"""
True, так сравниваются сперва первые элементы,потом дальше сравниваются, 
но так как 11>9, то выходит, что numbers1>numbers2

"""

"""
list не должен содержать только однотипные объекты
Могут храниться разные типы данных

"""

# numbers = [1, True, 'Makers', 'hello', 8.9,(1,2)]
# print(numbers)
"""
Индексация - обращение по индексу объекта
Итеруемый объект -это объект, каждый элемент, которого можно перебрать

"""

# numbers = [1, True, 'Makers', 'hello', 8.9,(1,2),['hello']]

# # print(numbers[0])
# # print(numbers[2])
# # print(numbers[4])
# # print(numbers[-1])
# # print(numbers[-2])
# # print(numbers[-3])

# print(numbers[7])

"""
Замена элемента в списке  с помощью присваивания по обращению к индексу элемента

"""
# numbers = [1, True, 'Makers', 'hello', 8.9,(1,2),['hello']]

# numbers[3] = 'Bootcamp'
# print(numbers)
# numbers[-1] = {1:'a'}
# print(numbers)
# numbers[7] = False #IndexError: list assignment index out of range
# print(numbers)

# string = 'Makers'
# string[-1] = '5'
# print(string) 
"""
TypeError: 'str' object does not support item assignment.
Так функция строк это неисчясляемый тип данных

"""
"""


"""

# users = ['Alice', 'Sam', 'Carly']

# for user in users:
#     print(f'Hello {user}')

# for letter in 'Makers':
#     print(letter)

"""
 Методы списков:

"""

"""
1.append(element)- метод добавления объекта в конец списка. Принимает только один элемент

"""

# users = ['Alice', 'Cat', 'Itachi']

# user = 'Tom'
# users.append('Sasuke')
# print(users)



# guests = []
# list_length = int(input('Enter the number of guest: '))

# for i in range(list_length):
#     guest = input('Enter guest name: ')
#     guests.append(guest)

# print(guests)

# a = [[1,2,3], 5]
# a[0] #[1,2,3]
# a[0].append(4)



"""
extend(list) - добавляет элементы другого списка в конец текущего.
Таким образом один список расширяется за счёт другого, но взятый для расширения список сам не изменяется
То есть текущий список, который мы расширяем изменяется, а второй нет
"""


# users1 = ['Alice', 'Bob', 'Sam']
# users2 = ['Asiha', ' Helena']

# users1.extend(users2)
# # print(users1) #['Alice', 'Bob', 'Sam', 'Asiha', ' Helena']
# print(users2) #['Asiha', ' Helena']
 
"""
Конкатенация списков отличается от метода расширения extend, тем что исходные списки сами не изменяются. 
Тут список2 = const и список2 = const, а выше только список 2 равно константе

"""
# print(users1 + users2)
# print(users1)
# print(users2)

"""
2.insert(index, item) - добавляет объект по индексу в список 
Он как бы отодвигает список и вставляет по индексу нужный нам элемент
К примеру, по индексу 0 вставляется в начало, а -1 в конец, но можно использовать
append вместо index в этом случае.


"""

# users =['John', 'Itachi', 'Saiki']

# users.insert(1, 'Uchiha')
# print(users)

# a = [1,2,3,4,5]
# # a.append(6)
# # print(a) #[1,2,3,4,5,6]
 
# # #a.inser(5,6)
# a.insert(8,6)
# print(a.insert(8,6))  #None

"""
3.remove(element)- удаляет объект и при этом только первое его вхождение

"""

# users = ['Sam', 'Itachi', 'Helena', 'Hh', 'cooot','Hh']
# # users.remove('Hh')
# # print(users)

# # users.remove('Raychel Uchihq')  #list.remove(x): x not in list
# # print(users)

# if 'Raychel Uchihq' in users:
#     users.remove('Raychel Uchihq')
# else:
#     pass #пропускает какое-то действие

# a = ['a', 'b', 'c', 'd']
# a.remove('b')
# print(a) #['a', 'c', 'd']

"""
Удаляет по первому вхождению
"""
# list = [1,2,3,4,222,4,5,6,7,1,1,1,1]
# list.remove(1)
# print(list) #[2, 3, 4, 222, 4, 5, 6, 7, 1, 1, 1, 1]


"""
4.clear()- удаляет все элементы из списка.Но при этом это объект продолжает существовать и не выдает ошиббку при обращении к нему.

"""

# users = ['Sam', 'Cat', 'Carly']
# print(id(users))
# users.clear()
# print(id(users))

"""
del item - удаляет полностью объект и при обращение к нему выдает ошибку, 
что этот объект не существует

"""
# users = ['Sam', 'Cat', 'Carly']
# print(id(users))
# del users
# print(users)  #NameError: name 'users' is not defined

"""
Можно удалить определенный объект из списка при использовании среза.

"""
# users = ['Sam', 'Cat', 'Carly']
# print(id(users))
# del users[-1]
# print(users)  #['Sam', 'Cat']



"""
5.index(element) - возращает  индекс первого вхождения в списке.

"""

# a = [1,2,3,4,5,6,7]
# print(a.index(2))

# my_list = ['Hello', 'Makers', 'Gogp', True, False, 0, 2]
# print(my_list.index(2))

"""
6.pop(index), default - удаляеет элемент по индексу. Если индекс элемента не указан,
то удаляет последний элемент 

"""
 
# list1 = [1,2,3,4,5,6,7,]
# list1.pop()
# # print(list1) #[1, 2, 3, 4, 5, 6]


# numbers = [1, 2, 3, 4, 5, 5,6 ]
# numbers.pop()
# number2 = numbers.pop()
# print(numbers) #[1,2,3,]
# print(number2) 

"""
7.count(element) -  возвращает (количество вхождений)число, сколько раз встречается элемент с указанным значением.

"""

# numbers = [2,3,434,444,22,4,4,0,2,2,2]
# users = ['Ann', 'Alice', 'Sam', 'Ann']
# print(numbers.count(2))
# print(users.count('Ann'))


"""
8.sort(key) - сортирует список по возрастанию.
sort(key = ..) сортирует по заданному параметру по возрастанию

"""
# users = ['Alice', 'Thomas', 'Cat', 'Fox']
# users.sort(key=len)
# print(users)

# list = [1,2,3,5,78,76,98]
# sorted(list)
# print(list)

# list = [...,...,.....]
# my_func = 
# sorted(list, key = my_func)


"""
9.reverse()- возвращает в обратном порядке(по уменьшению) и  элементы списка сохраняются в другом порядке!!!
reverse(key = ...)
"""
# a = [1,34,56,54]
# a.reverse()
# print(a)


# a = a[::-1]
# print(a)

"""
10.copy() - копирует один список в другой, но отличается от = тем, что у них разное id() и при изменение одного второй не меняется.

"""

# users1= ['Tim', 'Alice', 'Trever']
# users2 = users1.copy

# print(id(users1))
# print(id(users2))

# users1.pop()
# print(users1)
# print(users2)


# a = [1,2,3]
# b = a 
# a[0] = 10
# print(b)



""" 
Функции

"""


""" 
len() - возвращает длину списка, каждый элемент списка засчитывается за один.
"""

# users = [11,3,4,5]
# print(len(users))  #4


""" 
max()- 
min()- 
"""
# list = [1,2,3,5,78,76,98]
# print(max(list))
# print(min(list))

""" 
sum() - общую сумму объектов списка

"""
# numbers = [4,5,6,76,75,-56,-54,1000] 
# print(sum(numbers))  #1056


""" 
sorted()- получаем отсортированный список, но не менять его исходное состояние.
"""
# list = [1,2,3,5,78,76,98]
# print(sorted(list))

""" 
Срезы (slice) - это какие-то части чего-либо


"""
# list = [1,2,3,5,78,76,98]
# #list[x:y] - список от х а конец будет y, но y не будет включен.
# print(list[1:4])   # [2,3,5]

# list = list[1:4]
# print(list)


# queue =['John', 'Alice', 'Emily', 'Kira']

# queue[0] #John
# queue[1:3]

# my_list =[1,2,3,4,5,6,7,8]
# print(my_list[2:-1:2])



""" 
Генератор - это способ уместить цикл for, блок if и присваивание в одну строку. 
Другими словами, вы можете отображать map и фильтровать списки одним выражением.

Обычный список в ячейке памяти несколько ячеек памяти
А генератор занимает только одну ячейку.

"""
# a = [1,2,3,4,5]
# b = range(1,6)

# a = range(6).__iter__()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a)) #StopIteration, количество принтов превооходит количество элементов в списке


""" 
while - многократная проверка условие ( цикл исполняется до тех пор пока выполняется условие)

"""
# a = [1,2,3,4,5,6,7,]
# while  1 in a:
#     print(a)
    


""" 
for -  цикл для обхода последовательностей(iterable): строки, списки, кортежи, словарь, множества, range(). 
Цикл выполняется до тех пор, пока в последовательности не исчерпают элементы.

"""
#Дана последовательность, необходимо обойти все элементы и распечатать каждый элемент.

# list1 = [1,2,3,3,4,5,7,8,8,56]

# for number in list1 :
#     print(number) 

 
# list1 = [1,2,3,3,4,5,7,8,8,56]

# for item in list1:
#     print(item**2)

# list1 = ['tim', 'john', 'jack']
# new_names = []
# for name in list1:
#     new_names.append(name.capitalize())

"""
Обращаем строки в список

"""

# str1 = 'My string'
# print(list(str1))

# a = '123456'
# for char in a:
#     print(char)

# str1 = 'My string'
# print(list(str1[0]))


"""
Объединенное использование цикла и условных операторов

"""
# a =[12,34,453,563,535,53452,5245,53,4,4,3,4,3,4234]

"""
в новый список собрать числа. которые кратны 3


"""
# res = []
# for num in a:
#     if num %3 == 0:
#         res.append(num)
# print(res)

# a = [[1,2,3,4], [4,5,6,7], [5,56,6]]
# for item1 in a:
#     for item2 in item1:
#         print(item2)



""" 
break - принудетельная остановка цикла.
continue - пропуск итерации.
Итерация - один проход(запуск) цикла.
"""

# list1 = [1,43,21,3,5,5,6,6,4,0,22,1]

""" 
Распечатать сумму всех чисел, которые идут до нуля.
"""

# total = 0
# for i in list1:
#     if i ==0:
#         break
#     else:
#         total += i
# print(total)


""" 
Пройтись по списку и посчитать сумму всех чисел, которые кратны 3 
"""

# a =[12,34,453,563,535,53452,5245,53,4,4,3,4,3,4234]

""" 
Вариант 1 :
""" 
# total = 0
# for num in a:
#     if num % 3 == 0:
#         total+= num
# print(total)

""" 
Вариант2 с помощью continue
"""

# total = 0
# for num in a:
#     if num % 3 != 0:
#         continue
#     total += num
# print(total)



# names = ['Alina', 'Timur', 'Alib', 'Aium']
# for name in names:
#      if not name.startswith('A'):
#          print(name)
# for name in names:
#     if name.startswith('A'):
#         continue
#     print(name)
    
# a = ['string']
# a[0] #'string'


"""
Обращение к списку в другом списке
"""
# users = [
#     ['Tom', 23],
#     ['Noi',34],
#     ['Emily', 45]
# ]
# print(users[0])
# print(users[1])
"""
Обращение к элементу списка в списке:
Можно по срезу, а можно с помощью цикла for
"""
# print(users[0][0])

""" Мы вытащили каждый элемент списка в списке"""

# for list_ in users:
#     for element in list_:
#         print(element)
""" 
Разделение с помощью |
"""

# for list_ in users:
#     for element in list_:
#         print(element, end=' | ')    

""" 
Получается своебразная таблица
"""

# for list_ in users:
#     for element in list_:
#         print(element, end=' | ')  
#     print()    

"""
Classroom
Классная работа

"""
"""
1) Напишите программу, которая запрашивает с ввода семь чисел через запятую, добавляет их в список.
На экран выводит первое и последнее число списка. Затем удаляет последнее число и вместо него вставляет слово “Makers”.
Например: 
Ввод: Введите цифры через запятую: 5, 7, 8, 1, 3, 0, 8
Вывод: 5 8
[5, 7, 8, 1, 3, 0, ‘Makers’]
"""
# писать код здесь
# numbers_str = input('Введите цифры через запятую: ').split(',')
# numbers_int =[]
# for number in numbers_str:
#     numbers_int.append(int(number)) 
# print(numbers_int[0], numbers_int[-1])

# numbers_int.pop()
# numbers_int.append('Makers')
# print(numbers_int)


"""
2) Напишите программу, которая генерирует 10 случайных чисел, добавляет их в список и возвращает вам список этих чисел в
отсортированном виде в порядке возрастания.
"""
# писать код здесь
# from random import sample
# numbers = sample(range(0,15),k =10)
# print(sorted(numbers))


"""
3) Напишите программу, которая заполняет список словами, введенными с клавиатуры, 
измеряет длину каждого слова и добавляет полученное значение в другой список. 
Например, список слов – ['yes', 'no', 'maybe', 'ok', 'what'], список длин – [3, 2, 5, 2, 4]. 
Оба списка должны выводиться на экран.
"""
# писать код здесь

# list_length = int(input('Enter list length: '))

# words = []
# words_length = []
# for i in range(list_length):
#     word =input('Enter word: ')
#     words.append(word)
# print(words)


"""
Task
Таски
"""

#1
# name_of_friends = ['Alice', 'Bob', 'Michael', 'Jane', 'Patrick']
# for items in name_of_friends:
#     print(items)

#2

# labels = ['Honda', 'Toyota', 'Ferrari', 'Royals Royce']
# for items in labels:
#     print(f'I like brand {items}')

#3
""" 
Это мое решение, которое я не довела до конца
"""
# name_of_list = ['Helloworld!']
# name_of_list = 
# print(name_of_list)
# len_iteam1 = len(name_of_list) / 2 
# print(len_iteam1)
# len_iteam2 = len_iteam1
# if len(name_of_list)%2 != 0 :
#     len_iteam1 = len_iteam2 + 1
#     iteam1 = list(name_of_list[::(len_iteam1)])
#     iteam2 = list(name_of_list[(len_iteam2)::])
#     print(iteam1)
#     print(iteam2)
#     # for iteam1 in name_of_list:
#     #     print(iteam1)
#     # for item2 in name_of_list:
#     #     print(iteam2)
# else:
#     len_iteam1 = len_iteam2
#     iteam1 = list(name_of_list[::(len_iteam1)])
#     iteam2 = list(name_of_list[(len_iteam2)::])
# # print(name_of_list)


"""
А это решение, которое мне скинули 
Нужно обязательно его пересмотреть
"""
# name_of_list =['Helloworld!']
# letter = name_of_list[0]
# newlist = []
# 
# length = len(letter)
# seredina = length //2
# 
# if length %2:
#     seredina +=1
# f_part = letter[: seredina]
# s_part = letter[seredina:]
# newlist.append(list(s_part))
# newlist.append(list(f_part))
# new_list = s_part +f_part
# 
# print(list(new_list))



"""
4.Создайте список list_, состоящий ровно из двух строк.
Переставьте эти строки местами.
Результат запишите в новый список new_list и выведите в консоль получившийся результат
Например, если list_ выглядит так:

['world', 'hello'] 
результат будет:

['hello', 'world'] 
"""
    
# list_ =  ['Itachi', 'Uchiha']
# list1 = list_[0]
# list2 = list_[1]
# new_list =[list2,list1]
# print(new_list)

"""
5.Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст: suitcase = []. Однако он может вместить всего 5 вещей.

Положите 5 вещей в чемодан с помощью метода append()
Вы передумали, и решили убрать последнюю вещь. Вспомните, какой метод помогает удалить последний элемент.
Вы решили положить в чемодан другую вещь, только в первое место (т.е. по индексу 0). Вспомните метод, который ставит элементы по индексу.
Распечатать чемодан
Пример:

# положили 5 вещей 
['футболка', 'шорты', 'сланцы', 'очки', 'кепка'] 

 
#решили убрать последнюю 
['футболка', 'шорты', 'сланцы', 'очки'] 

 
#в начале, добавили новую вещь 
['панама', 'футболка', 'шорты', 'сланцы', 'очки'] 
"""
# suitcase =[]
# items1 = 'hat'
# items2 = 'kepka'
# items3 = 'ddd'
# items4 = 'ff'
# items5 = 'gg'

# suitcase.append(items1)
# suitcase.append(items2)
# suitcase.append(items3)
# suitcase.append(items4)
# suitcase.append(items5)

# print(suitcase)
# suitcase.pop(-1)
# print(suitcase)
# item6= 'fff'
# suitcase.insert(0,item6)
# print(suitcase)

"""
6.Создать список чисел nums.
Используя цикл и метод списка, запишите все числа меньше 5 в новый список.
Распечатайте результат. Например, если в nums выглядит так:
nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
результат будет:

[1, 1, 2, 3]

"""
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# nums_new= []
# for iteams in nums:
#     if iteams < 5:
#         nums_new.append(iteams)
# print(nums_new)


"""
7.Вы принимаете от пользователя последовательность чисел, разделенных запятой.
Составьте список list_ и кортеж tuple_ с этими числами и распечатайте их.
"""
# str = input()
# list_ = str.split(',')
# print(list_)
# tuple_ = tuple(str.split(','))
# print(tuple_)

"""
8.Создайте список чисел list_.
Пройдитесь по элементам списка и преобразуйте все числа в строку.
Результат запишите в новый список new_list и выведите в терминал.
К примеру, если в list_:

 [1, 2, 3, 4, 5]
то в new_list получим:

['1', '2', '3', '4', '5']
используйте встроенную функцию str()
"""
# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for i in list_:
#     new_list.append(str(i))
# print(new_list)


"""
9.Создайте список чисел list_.
Переберите элементы циклом и вместо четных чисел, поставьте строку четное, а вместо нечетных нечетное.
Результат записать в новый список new_list и вывести в терминал.
К примеру, если в списке хранятся такие числа:

[1, 2, 3, 4, 5]
результат будет:

['нечетное', 'четное', 'нечетное', 'четное', 'нечетное']

"""
# list_ = [1, 2, 3, 4, 5]
# new_list =[]
# for number in list_:
#     if number % 2 == 0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')
# print(new_list)


"""
10.Используя функцию range() создайте список list_ из 20 произвольных чисел.
Распечатайте результат
Примерный вывод:

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 
"""
# list_ =list(range(0,21))
# print(list_)

"""
11.При помощи функции range() создайте список list_ из чётных чисел от 0 до 100 (включительно).
Распечатайте результат.
Примерный вывод:
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 
24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 
50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 
76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100] 
"""
# list_ =list(range(0,101,2))
# print(list_)

"""
12.Создайте два списка list1, list2 со случайным набором чисел.
Объедините эти списки.
Затем, выведите сумму всех чисел в консоль.
К примеру, если в перемнных хранятся такие списки:

[11, 23, 45, 7, 9] 
[21, 4, 16, 8, 10] 
Объединив их и распечатав сумму всех чисел, получим:

154 
"""
# list1 = [11, 23, 45, 7, 9] 
# list2 = [21, 4, 16, 8, 10] 
# list_ = sum(list1+list2)
# print(list_)

"""
13.Написать программу, которая будет принимать от пользователя числа через запятую.
   числа поместить в список list_ и вывести в отсортированном виде.
Код работает, но платформа не приняла её. Нужно спросить, что не так
"""

# numbers_str = input('').split(',')
# list_ = []
# for number in numbers_str:
#     list_.append(int(number))
# list_.sort()
# print(list_)



"""
14.Создать три числа в списке list_.
Вывести на экран yes, если среди них есть одинаковые, иначе вывести ERROR.
Например, для списка [1, 1, 3], вывод будет:

yes 
а для списка [1, 2, 3]:

ERROR 
"""
# list_ = [1, 26, 26]
# if list_[:1] == list_[1:2] or list_[:1] == list_[2::] or list_[2::] == list_[1:2] :
#     print('yes')
# else:
#     print('ERROR')
    
    
"""
15.Записать в список list_ все числа в промежутке от 54 до 9184 делящиеся на 5 без остатка.
Распечатайте результат.
"""
# list_ =[]
# for i in range(54,9184):
#     if i%5 == 0:
#         list_.append(i)
# print(list_)

"""
Молодец!!!
Тема пройдена :)
"""