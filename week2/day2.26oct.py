"""
Не закончен классворк 
День 2. Неделя 2                              
Тема: Множества, кортежи и цикл while               

Множества - неупорядоченнвй изменяемы набор уникальных неизменяемых объект
set()  -
создается с помощью функции set или с использованием {}

изменяемые типы:
- списки
- словари
- множества 

неизменяемые типы:
- числа(цулые и дробные)
- строки
- кортежи
- boolean()
- frozenset()
- None

"""

# empty_set() = set()
# empty_dict = {}
# print(type(empty_set))
# print(type(empty_dict))

# SyntaxError: cannot assign to function call
# Так как нельзя задавать пустое множество


"""
Получаем неупорядоченную последовательность при принте каждый раз,
так как это свойство множеств

"""

# a = {'makers', 4, 9, True, False}
# print(a) #{False, True, 4, 9, 'makers'} 
# b = set('makers')
# print(b)  # {'m', 'e', 'a', 'k', 'r', 's'}
# c = set(range(1,10,2)) #{1, 3, 5, 7, 9}
# print(c)


"""
Множества изменяемый тип данных, но его элементы должны быть 
неизменяемым типом данных, если поместить изменяемый тип данных выйдет ошибка

"""
# my_set = {'hello',1, False} #{False, 'hello', 1}
# print(my_set)
# my_set = {'hello',1, [1,2,4]}
# print(my_set) #unhashable type: 'list'

"""


"""
# set1 = {1,5,6,7}
# set2 = {1,6,7,5}
# print(set1 ==set2) #True


# set1 = {1,5,6,7,9}
# set2 = {1,6,7,5}
# print(set1 ==set2) #False

# set1 = {1,5,6,7,0}
# set2 = {1,6,7,5,8}
# set3 = {1,5,6,7,0,8,9,8,8,8,6,7}
# print(set3) # {0, 1, 5, 6, 7, 8, 9}
# # print(set1 ==set2)
# print(set3==set2)

"""
Так как True = 1 и при запуске print, если True стоит на первом месте, что он выводит True
И так как в примере 1.0 = 1 и равен True, то множество принимает их за дубликаты и удаляет

"""
# my_set = {1.0,True,1} 
# print(my_set)


"""
Так как функция set удаляет все дупликаты, то при принте считает только уникальные 
элементы!!!
При создании множеств добавляйте только уникальные элементы

"""
# set3 ={1,2,3,4,5,5,5,2,4}
# print(set3) #{1, 2, 3, 4, 5}
# print(len(set3)) #5

"""
Методы множеств:

"""


"""
add()- добавляет элемент в множество(в любое место, так как множество - неупорядоченное)
add(element)

"""
# guests = {'Tom', 'Sam','Helen'}
# print(guests) #{'Sam', 'Tom', 'Helen'}
# guests.add('Raychel') #{'Sam', 'Raychel', 'Tom', 'Helen'}
# print(guests)

"""
update() -расширяет одно множество за счет другого
В скобках пишем название множества, элементы, которого мы добавляем
в наше исходное множество, при этом само множество не изменяется, то есть
set1.update(set2) = {....}
set2 - const
"""
# numbers1 = {1,2,4,5,6}
# numbers2 = {7,8,9}

# numbers1.update(numbers2)
# print(numbers1) #1, 2, 4, 5, 6, 7, 8, 9}
# print(numbers2) #{8, 9, 7}, осталось неизменной

"""
remove()- убирает элемент из множества, но выдает ошибку, если элемента в списке нет

"""
# guests = {'Cat', 'Alice', 'Jane'}
# guests.remove('Alice')
# print(guests)  # {'Jane', 'Cat'}

# guests = {'Cat', 'Alice', 'Jane'}
# guests.remove('John')
# print(guests) #KeyError: 'John'


"""
discard()- удаялет элемент из множество, но если элемента в множестве нет, 
этот метод не выдает ошибку

"""
# guests = {'Cat', 'Alice', 'Jane'}
# guests.discard('John')
# print(guests) #{'Alice', 'Cat', 'Jane'}


"""
pop() -удаляет элемент из множества, но удаяет каждый раз рандомный 
элемент

"""
# guests = {'Cat', 'Alice', 'Jane', 'Bob', "Ben"}
# guests.pop()
# print(guests) #{'Ben', 'Cat', 'Jane', 'Bob'} or  {'Bob', 'Jane', 'Alice', 'Cat'}
 
"""
clear()- очищает множество, а del полностью удаляет

"""
# guests ={'Bob', 'Jane', 'Alice', 'Cat'}
# guests.clear() #set()
# # del guests
# # print(guests) #NameError: name 'guests' is not defined
# print(id(guests)) #140424857774336
 
"""
copy()- копирует одно множество в другое

"""
# guests ={'Bob', 'Jane', 'Alice', 'Cat'}
# guests1 = guests.copy()
# guests.add('Raychel')
# print(guests) #{'Bob', 'Cat', 'Alice', 'Raychel', 'Jane'}
# print(guests1) #{'Jane', 'Cat', 'Bob', 'Alice'}

"""
intersection() - находит пересечения двух множеств, при этом он не изменяет 
сами элементы множеств, а просто возвращает элемент пересечения

"""
# music_students = {'Sam', 'Alice','Ben', 'Kate'}
# art_students = {'Raychel', 'Sam', 'Alex','John','Cathrine'}
# print(music_students.intersection(art_students)) #Sam

"""
& - может показывать пересение нескольких множеств и возращать элемент пересечения между ними.
"""
# music_students = {'Sam', 'Alice','Ben', 'Kate'}
# art_students = {'Raychel', 'Sam', 'Alex','John','Catherine'}
# print(music_students & art_students) #Sam
"""
union()- объединяет два множества и убирает все деубликаты (A U B) \ AB =
Может объединять несколько множеств в одно, если прописывать их через запятую
c = c.union(a,b)
"""
# music_students = {'Sam', 'Alice','Ben', 'Kate','John'}
# art_students = {'Raychel', 'Sam', 'Alex','John','Catherine'}

# print(art_students.union(music_students)) #'John', 'Ben', 'Sam', 'Catherine', 'Raychel', 'Alex', 'Kate', 'Alice'}

# a ={'John', 'Ben', 'Sam'} 
# b ={'Catherine', 'Raychel'}
# c ={'Alex', 'Kate', 'Alice'}
# print(a.union(b,c)) #{'John', 'Raychel', 'Catherine', 'Kate', 'Alex', 'Alice', 'Sam', 'Ben'}

"""
difference() - показывает A\B, где возвращает все элементы A не 
входящие в множество B
"""
# a ={'John', 'Ben', 'Sam'} 
# b ={'Catherine', 'Raychel', 'John'}
# c ={'Alex', 'Kate', 'Alice'}
# print(a.difference(b)) #{'Sam', 'Ben'}
# print(b.difference(a)) #{'Raychel', 'Catherine'}


"""
(-) -оператор минус между множествами может работать как метод differnce 
"""
# a ={'John', 'Ben', 'Sam'} 
# b ={'Catherine', 'Raychel', 'John'}
# c ={'Alex', 'Kate', 'Alice'}
# print(a - b) #{'Sam', 'Ben'}


"""
symmetrical_differnce() - возвращает уникальные для обоих элементы,а пересекающиеся элементы удаляет.
"""
# a ={'John', 'Ben', 'Sam'} 
# b ={'Catherine', 'Raychel', 'John'}
# c ={'Alex', 'Kate', 'Alice'}
# print(a.symmetric_difference(b)) #{'Sam', 'Ben', 'Catherine', 'Raychel'}

"""
isdisjoint() - возращает True или False, 
если есть пересечения False, есди нет - True

"""
# numbers1 ={1,2,3,4,5}
# numbers2 ={6,7,8,9}
# print(numbers1.isdisjoint(numbers2)) #True, так как пересчений нет

"""
issupperset() - возвращает True или False, если множество 1 является 
надмножеством множества 2
issubset() - возвращает True или False, если множество 1 является 
подмножеством множества 2
"""
# numbers1 ={1,2,3,4,5}
# numbers2 ={4,5}
# print(numbers1.issuperset(numbers2)) #True
# print(numbers2.issubset(numbers2)) #True

"""
intersection_update() - изменяет множество к которому применяется 
метод instersection (нахождение перескекающихся элементов и их выдача)

"""
# numbers1 ={1,2,3,4,5}
# numbers2 ={4,5}
# # # numbers1.intersection_update(numbers2)
# # print(numbers1) #{4,5}
# numbers1.update(numbers2)
# print(numbers1)

"""
difference_update()- изменяет множество, к которму 
был применен это метод
"""
# numbers1 ={1,2,3,4,5,6}
# numbers2 ={4,5,2,7,8}
# numbers2.difference_update(numbers1)
# print(numbers2) #{7,8}

"""
symmetrical_differnce_update() - меняется то множество к которому был применен метод.
"""
# numbers1 ={1,2,3,4,5,6}
# numbers2 ={4,5,2,7,8}
# numbers1.symmetric_difference_update(numbers2)
# # print(numbers1) #{1,3,6,7,8}

"""
frozen_set() - неизменяемый тип данных
"""
# my_frozenset = frozenset('makers')
# my_frozenset2 = frozenset('nakers')
# my_frozenset.intersection_update(my_frozenset2) 
# print(my_frozenset) #'frozenset' object has no attribute 'intersection_update'














"""
Кортеж - неизменяемый упорядоченный набор произваольных элементов.
tuple() - представляет последовательность элементов, которая во многом похожа на список за тем исключением, 
что кортеж является неизменяемым (immutable) типом. 
Поэтому мы не можем добавлять или удалять элементы в кортеже, изменять его.
При создании кортежа с одним элементом обязаетельно нужно ставить (,) , если не ставить то это будет не кортеж, 
а строка
Пример ниже:
"""
# a = ()
# b =tuple()
# c = 1,2,3 #1,2,3

# x = 10
# y = 20

# x,y = y,x
# x,y =(20,10)
# #x, y = [20,10]

# a = ('ddd')
# print(type(a))


# my_tuple = ('Alice',3, True,False, [1,2])
# print(type(my_tuple)) #print(type(my_tuple)) 
 
# my_tuple =('Makers',)
# print(type(my_tuple)) #<class 'tuple'>

# my_tuple =('Makers',)
# print(my_tuple)

"""
Так как кортежи это упорядоченный тип данных мы можем 
использовать индиксауию и срезы
Но кортежи неизменяемый тип данных
Поэтому не поддерживает append(), pop(), но поддерживает count()
"""
# my_tuple = (1,2,4,6,8,5)
# # print(my_tuple[1]) #2
# # print(my_tuple[2:5]) #print(my_tuple[2:5]) 
# my_tuple[2] =7 #TypeError: 'tuple' object does not support item assignment


# print(dir(tuple))



"""
Методы кортежей
"""

"""
1.count(value) - считает количество элементом с этим значением

"""
# my_tuple = (1,4,4,7,4,2)
# print(my_tuple.count(4)) #3

"""
2.index(value) - возвращает индекс первого элемента с указанным значением
"""
# my_tuple = (1,True,'makers',9.2)
# print(my_tuple.index('makers')) #2

"""
Kонкатенация
"""
# a =(1,2,4)
# b =(5,6,7)
# print(a + b)  #(1, 2, 4, 5, 6, 7)


"""
Функции при работе с кортежами:
len(), max(), min(), sum()
"""
# numbers =(1,2,3,4,5,7,8,9,54)
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

"""
Кортеж неизменный тип данных, но если его элементы изменяемый тип данных, 
то их можно изменить

"""
# my_tuple = (1,True,2,['hello', 'makers'])
# my_tuple[-1] [0] ='bootcamp'
# print(my_tuple) #(1, True, 2, ['bootcamp', 'makers'])

"""
Кортежи занимают меньше памяти.
Все пустые кортежи в Python занимают одну область памяти
 
empty tuple
"""
# a=()
# b=()
# # print(type(a)) #class tuple
# print(id(a)) #139768908337216
# print(id(b)) #139768908337216
# print(a is b) #True

"""
Перебор кортежей и множеств
Кортежи и множеств являются иттериемыми типами данных, то есть их можно перебрать 

"""

# my_tuple = ('Alice', 'Sam','Cat', 'John')
# for name in my_tuple:
#     print(f'Welcome,{name}!')

# my_set = {6,3,4,5,8,10}
# for number in my_set:
#     print(number**3)















"""
Цикл while - 

while логическое выражение:
    тело
блок кода
"""

# users = {'Alice', 'John', 'Carly','Bob'}

# while users: # можем использовать while users is not None
#     print(users)

"""
^
|
Бесконечный цикл можно остановить клавищами Ctrl+z
"""
# while users: 
#     users.pop()
#     print(users)
# print('Programm is finished')

"""
break -  остановливает
contione - пропускает одну итерацию

"""
# while True:
#     word = input('Enter the word: ')

#     if word.lower == 'exit':
#         break
#     elif not word:
#         print('Type anythong:')
#         break
#     else:
#         print(word[::-1])
#         continue



"""
Example of using while

"""

# money = 100
# while money > 0:
#     n =int(input('How much did you spend: '))
#     money -= n
#     print(f'You have {money} soms left')
# print('You do not have a money')

# a =[1,2,3,4,5,6]
# b = tuple(a)
















"""
Classroom

"""

"""
1) Создайте два множества. Первое множество должно содержать внутри себя ингредиенты для приготовления “Окрошки”, 
а второе - для приготовления салата “Оливье”.
И проделайте следующие действия: 
а) Найдите одинаковые ингредиенты, поместите их в отдельное множество и найдите количество этих ингредиентов; 
б) Найдите уникальные ингредиенты для каждого из блюд
"""
# писать код здесь

# set_okroshka ={'kefir','ogurez','kolbasa','ykrop','kartoshka'}
# set_olivie ={'kartoshka','mayonez','kolbasa','morkovka','yazo'}
# print(set_okroshka.intersection(set_olivie))
# print(set_okroshka.difference(set_olivie))


"""
2) Создайте множество, внутри которого разместите кортежи. 
Внутри кортежей должна храниться информация: имя юзера, язык программирования и опыт 
(Например: (“Alice”, “Python”, 3)). 
Создайте программу, которая будет:
считать, сколько юзеров изучает язык Python и сколько изучает  JavaScript.
находит юзеров, которые изучают оба языка
"""
# писать код здесь

set_ = {('Alice', 'Python',3), ('Peter','Python',5),('Helen','JavaScript',9),('Koshop','JavaScript',16),('Aka','Python',4)}



"""
3) Напишите программу, которая конвертирует доллары в сомы и сомы в доллары. При этом программа должна запрашивать данные у пользователя до тех пор, пока пользователь не захочет завершить программу. 
Например:
Ввод: Введите валюту (сом или доллар): доллар
Ввод: Введите сумму, которую вы хотите перевести в доллары: 3000
Вывод: 35.4 $
Ввод: Хотите продолжить?: Да
Ввод: Введите валюту (сом или доллар): сом
Ввод: Введите сумму, которую вы хотите перевести в сомы: 70
Вывод: 5936.0 сом
Ввод: Хотите продолжить?: Нет
Вывод: Всего хорошего!
"""
# писать код здесь





"""
Task
"""
#13
# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}

# if robert & kail and robert & merri :
#     print('kail merri')
# elif robert & kail:
#     print ('kail')
# elif robert & merri:
#     print('merri')
# else:
#     print('no one')

# if len(robert.intersection(kail))>=1 and len(robert.intersection(merri)) >=1:
#     print('kail merri')
# elif len(robert.intersection(kail))>=1:
#     print ('kail')
# elif len(robert.intersection(merri)) >=1:
#     print('merri')



#14
# tilek = {'Dodo', 'ImperriaPizza', 'Freshbox'}
# timur = {'OchakKebab', 'Freshbpx'}
# alexander = { 'Freshbox', 'KFC'}
# elina = {'Dodo', 'ImperiaPizza', 'Freshbox', 'KFC'}
# print(tilek &timur & alexander)

"""
15.Имеется пицца, ингредиенты которой помещены во множество ingredients. Используйте определенные методы, чтобы проделать все действия. Ингредиенты: сыр чеддар, грибы, соус, шпинат

Данные: 

ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 

Действия: 


* Добавьте "помидор" в данное множество. 
* Уберите ингредиент "колбаса" (если она есть!) 
* Уберите ингредиент "шпинат" (Методом который вызовет ошибку если его нет), вместо него добавьте "базилик" 
* Замените "сыр чеддар" на "сыр моцарелла". 
* Распечатайте результат```
"""


# ingredients = {'сыр чеддар','грибы','соус','шпинат'}
# ingredients.add('помидор')
# ingredients.discard('колбаса')
# ingredients.remove('шпинат')
# ingredients.add('базилик')
# ingredients.remove('сыр чеддар')
# ingredients.add('сыр моцарелла')
# print(ingredients)

"""
Task1.Extra
Создайте переменную a в которой будет хранится список из 3 пустых множеств не словарей. 
Затем запросите у пользователя строку Hello world. Cохраните этот инпут в переменную inp1. 
Затем спросите пользователя число в какое множество он хочет добавить эту строку, он может выбрать от 1 до 3 - этот инпут сохраните в переменную inp2. 
В выбранное множество добавьте эту строку, а в остальные множества добавьте строку "default value". 
В конце выведите получившийся список
"""
# a = [set(),set(),set()]
# inp1 = input()
# inp2 = int(input())

# if inp2 ==1:
#     a[0].update(inp1)
#     a[1].update('default value')
#     a[2].update('default value')
# elif inp2 ==2:
#     a[0].update('default value')
#     a[1].update(inp1)
#     a[2].update('default value')
# elif inp2 ==3:   
#     a[0].update('default value')
#     a[1].update('default value')
#     a[2].update(inp1)
# print(a)

"""
Extra Task3
Создайте два множества set1 и set2 используя comprehensions. 
В set1 должны хранится четные значения(в диаопозоне от 0 до 10), 
а в set2 нечетные(в диаопозоне от 0 до 10) 
Так же необходимо проверить с помощью специального метода пересекаюся они или нет, 
если пересекаюся вывести "Множества пересекаются!", 
если же нет ""Множества не пересекаются!""
"""
# set1 = { i for i in range(1,10) if i%2==0}
# set2 = {i for i in range(1,10) if i%2==1}
# if len(set1.intersection(set2)) ==0:
#     print('Множества не пересекаются!')
# else:
#     print('Множества пересекаются!')

"""
Молодец!!!
Тема пройдена :)
"""