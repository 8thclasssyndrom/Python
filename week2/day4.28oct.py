"""
Закончен
День 4. Неделя 2.28 октября.
Тема: List, dictionary comprehension. 

Comprehension - специальная конструкция, с помощью которой можно по определленным правилам создавать списки и словари.

Используется, когда необходимо обойти последовательность(строка, список, кортеж,словарь, range), 
сделать опредёленное действие и результат сохранить в новый список

* list comprehension - позволяет генерировать списки 
более компактным образом нежеле традиционным цикл for

my_list2 = [i for in range(50)]
print(my_list2)

*dictionary comprehension - вместо итерации по одной группе значений, 
словарь генерирует итерации по двум группам в тандеме, группе ключей и 
группе значений.

Преимещества по сравнения с циклами:
 1.Короткий и удобный синтаксис
 2.Понятный и читаемый синтаксис
 3.Быстрота выполнения

"""
"""
Начало практики:
Длится 1.6 минут

"""
"""
for 

"""
# list_ = []
# for num in range(1,21):
#     list_.append(num *2)
# print(list_)

"""
1 Способ: 
"""
# a = [1,2,3,4,5,6,7,8]

# res =[]
# for i in a:
#     res.append(i*10)
# print(res)

"""
2 Способ:
"""
# res = [i*10 for i in range(1,9)]
# print(res)



"""
list comprehension
[item for item in range(num1,num2)]

"""
# list_ =[num*2 for num in range(1,21)]
# print(list_) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

# list_users = ['Sam', 'Alex', 'Sandy', 'Ben', 'John']
# invitations = ['You are invited ' + name for name in list_users]
# print(invitations)


"""
list comprehension + if

"""
# list1 = [10,5,-6,-8,-12,20,3,14,4]
# list2 = [num for num in list1 if num %2 ==0]
# print(list2) #[10, -6, -8, -12, 20, 14, 4]

# list1 = [10,5,-6,-8,-12,20,3,14,4]
# list3 = [num for num in list1 if num %2 ==0 and num>0] 
# print(list3) ##[10, 20, 14, 4]


"""
string 

"""
# strings = ['1998','2001г', '2008rод', '2020']
# list_ =[ year for year in strings if year.isdigit() ]
# print(list_)  #['1998', '2020']


"""
len(string)

"""
# list_ = ['Raychel','JOhn','Alice','Sam']
# list_ = [len(name) for name in list_ if len(name)>3]
# print(list_) #[7, 4, 5]


"""
Ветвление if,else в list comprehension
Здесь if стоит до list comprehension, поэтому генератор здесь не работает как фильтр

"""
# list_ = [-4,-12,-34,45,0,98,6]
# list_ = [x if x<0 else x**2 for x in list_]
# print(list_) #[-4, -12, -34, 2025, 0, 9604, 36]
"""
Здесь сперва срабатывает фильтр генератора, если числа удовлетворяют условию после for x in list_
Они проходят ветвление в начале строки 
"""

# list_ = [-4,-12,-34,45,0,98,6]
# list_ = [x if x<0 else x**2 for x in list_ if x %2== 0]
# print(list_) #[-4, -12, -34, 0, 9604, 36]

"""
Считать количество символом в строке
"""
# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# filtered_names = [ x + 'MAKERS' if len(x) >= 5 else x + 'makers' for x in names if x.isalpha()]
# print(filtered_names) #['rauchelMAKERS', 'johnmakers', 'peterMAKERS', 'jessicaMAKERS', 'kamestMAKERS', 'potterMAKERS']

"""
Тот же самый пример только с циклом for

"""
# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# filtered_names = []
# for x in names:
#     if x.isalpha():
#         if len(x) >=5:
#             result = x + 'MAKERS'
#             filtered_names.append(result)
#         else:
#             result = x+ 'makers'
#             filtered_names.append(result)
# print(filtered_names) #['rauchelMAKERS', 'johnmakers', 'peterMAKERS', 'jessicaMAKERS', 'kamestMAKERS', 'potterMAKERS']


"""
Так как по PEP 8 наша строка с list comprehension считается некрасивой, то Python предоставляет нам возможность сделать ее красивой
Вот таким вот способом

"""
# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# filtered_names = [ 
#     x + 'MAKERS' 
#     if len(x) >= 5 
#     else x + 'makers' 
#     for x in names 
#     if x.isalpha()
#     ]

# print(filtered_names) #ошибки не выдает, но он более читаем и соответсвует стандартам PEP8
"""
Каждый list comprehension можно перезаписать в виде циклов
Но не каждый цикл можно записать в виде генераторов лист, так как есть ветвления типо elif

Пример использования цикла и генераторов
"""
# john = {'name':'John','age':22}
# raychel = {'name':'Raychel', 'age': 23}
# peter = {'name':'Peter','age':17}

# users = [john,raychel,peter]

# ages = [user.get('age',None) for user in users]
# # print(ages) #[22, 23, 17]

# bigger = 0
# smaller = 0
# count = 0

# for age in ages:
#     if age >=18:
#         bigger+=1
#     else:
#         smaller +=1
#     count+=1

# bigger = bigger * (100/count)
# smaller = smaller *(100/count)

# print(f'Процент пользователей с возрастом больше 18: {round(bigger)} процента')

# print(f'Процент пользователей с возрастом меньше 18: {round(smaller)} процента')


"""
Если цена товара меньше 100, то нужно снизить цену на 5 процентов, если больше, то на 10
Округлить результат до 2 знаков после запятой
"""
# a = { 'Milk':48,'Eggs':99,'Meat':500,'Sugar':48,'Oil':160 }

# res ={k : round(v * 0.9,2) if v >100 else round(v*0.95,2) for k,v in a.items()}

# print(res) #{'Milk': 45.6, 'Eggs': 94.05, 'Meat': 450.0, 'Sugar': 45.6, 'Oil': 144.0}



# list1 = [[1,2,3],[4,5,6],[7,8,9]]

# # new = []
# # for item in list1:
# #     inner_list = []
# #     for num in item:
# #         inner_list.append(num*10 )
# #     new.append(inner_list) 

# # print(new) #[[10, 20, 30], [40, 50, 60], [70, 80, 90]]


# new =[[num*10 for num in item]for item in list1]

# print(new) #[[10, 20, 30], [40, 50, 60], [70, 80, 90]]




# list1 = [[1,2,3],[4,5,6],[7,8,9]]

#[10,20,30,40,50,60,70,80,90]

# new = []
# for item in list1:
#     inner_list = []
#     for num in item:
#         new.append(num*10) 

# print(new)

# new = [num*10 for item in list1 for num in item]

# print(new)

"""
Матрица 
matrix

"""
# matrix = [
#     [0,2,5,6],
#     [7,3,0,7],
#     [5,7,1,6]
# ]

# # uncompress = [n for row in matrix for n in row] # такой код менее читабельный, но он работает быстрее

# uncompress = []
# for row in matrix:
#     for n in row:
#         uncompress.append(n)

# print(uncompress) #[0, 2, 5, 6, 7, 3, 0, 7, 5, 7, 1, 6]
"""
Покажем пример, где генератор списков работает быстрее чем цикл и проверим, что быстрее с помощью функции datetime

Создадим список с помощью цикла, потом с помощью генератора
"""
# from datetime import datetime

# start = datetime.now()

# list_ = []
# for i in range(100000):
#     list_.append(i)

# print(datetime.now() - start) #0:00:00.010018


# list_ = [i for i in range(100000)]
# print(datetime.now()-start) #0:00:00.004274

"""
Таким образом мы можем увидеть, что генератор списков пашет быстрее из-за отсутсвия метода append

"""






"""
Dictionary comprehension
Генераторы словарей

"""
# dict_abc = {'a':1,'b':2,'c':3}
# dict_123 = { value:key for key,value in dict_abc.items()}
# print(dict_123) #{1: 'a', 2: 'b', 3: 'c'}



# dict_abc = {'a':1,'b':2,'c':3}
# dict_123 = { key:value+2 for key,value in dict_abc.items()}

# print(dict_123) #{'a': 3, 'b': 4, 'c': 5}



# dict_abc = {'a':1,'b':2,'c':3,'d':-4,'e':-7}
# new_dict = { key.upper() : value**3 for key,value in dict_abc.items()}
# print(new_dict) #{'A': 1, 'B': 8, 'C': 27, 'D': -64, 'E': -343}

"""
Вложенные словари 
"""
# a ={
#     'fruites': 
#     {'apple':100,'orange':60},
#     'vegatables':
#     {'cucumber':34,'tomato':45}

#     }

# b = { key : 
#     {inner_k: inner_v + 3 for inner_k,inner_v in value.items()} 
#     for key , value in a.items() }
# print(b) # стали дороже на 3 сома













"""
Set comprehension 
Генераторы множеств

"""

# list_ = [-2,-4,-5,3,8,-2,3,7]
# set_ = {num for num in list_}
# print(set_) #{3, 7, 8, -5, -4, -2}



# list_ = [-2,-4,-5,3,8,-2,3,7]
# set_ = {num**2 for num in list_}
# print(set_) #{64, 4, 9, 16, 49, 25}



# dict_ = {'a':1,'b':2,'c':3}

# new = {value **2 for value in dict_.values()}
# print(new) #{1, 4, 9}

"""
Итоги:
мы используем генераторы, чтобы сделать создание структур быстрее и проще иногда

"""













"""
Classroom
Классная работа
"""
"""
1) Создайте список имён. 
Далее создайте отфильтрованный список имён, где будут содержаться имена, начинающиеся с гласных букв. 
Используйте list comprehension.
"""
# писать код здесь

# names = ['Alice','John','Jina','Inna','Vods','Yets','Olga']
# list_ = ['a','o','i','e','y','u']

# filtered_names = [name for name in names if name[0].lower() in list_]
# print(filtered_names) #'Alice', 'Inna', 'Yets', 'Olga']


"""
2) Создайте вложенный словарь, в котором ключами будут имена студентов, а значениями - другой словарь, 
в котором ключи - названия предметов, а значения - баллы за предмет данного студента. 
Далее с помощью dictionary comprehension обновите этот словарь, присвоив по 2 экстра балла каждому студенту по каждому предмету.
Например: 
a = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
Результат:
{'Sam': {'math': 97, 'literature': 90}, 'Alice': {'math': 72, 'literature': 100}}
"""
# писать код здесь

# a = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
# filtered_names = {key:{inner_k: (inner_val +2) for inner_k,inner_val in value.items()} for key,value  in a.items() } #{'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
# print(a)

"""
3) 
Создайте список чисел от 1 до 10. 
Создайте множество, в котором поместите квадраты этих чисел, если число делится на 2 без остатка, 
в противном случае поместите в список утроенные значения чисел.
"""
# писать код здесь

# list_ = [i for i in range(1,10)]
# set_ = [i2**2 for i2 in list_ if i2%2==0 ]
# print(set_) #[4, 16, 36, 64]





"""
Task
Таски

"""
"""
1.Создайте список list_ из целых чисел от 1 до 100 (включительно). Нужно использовать comprehension.

"""
# list_ = [item for item in range (1,101)]
# print(list_)


"""
2.Создайте список list_ из нечётных целых чисел в промежутке от 1 до 50. Нужно использовать comprehension.

"""
# list_ = [item  for item in range(1,50) if item%2 ==1]
# print(list_)


"""
3.Создайте список используя

list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
и запишите в новый список int_list

только четные числа, которые больше нуля. Нужно использовать comprehension.

"""
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [item for item in list_ if item%2==0 and item > 0]
# print(int_list)


"""
4.Создайте список list_ из квадратов всех чисел от 1 до 25 (включительно). 
В результате, список list_ должен выглядеть так:

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625] 
Нужно использовать comprehension.

"""
# list_= [item**2 for item in range (1,26)]
# print(list_)


"""
5.Используя данный список:

str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
создайте новый список int_list, где все элементы, строки старого списка str_list, будут преобразованы в числовой тип данных:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
Нужно использовать comprehension.

"""
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(item) for item in str_list]
# print(int_list)


"""
6.Создайте список list_ из чисел от 1 до 10 (включительно), заменяя четные числа - квадратом числа(число умноженное само на себя), нечетные добавьте без изменений.

В результате должны получить:

[1, 4, 3, 16, 5, 36, 7, 64, 9, 100] 
Нужно использовать comprehension.

"""
# list_ = [num**2 if num%2 == 0 else num for num in range(1,11) ]
# print(list_)


"""
7.Пройдитесь по промежутку чисел от 1 до 10 и запишите в список list_ True вместо числа, если число чётное и False вместо числа, если число нечетное.

Результат будет таким:

[False, True, False, True, False, True, False, True, False, True] 
1 - нечетное число, не делится на 2 без остатка, вместо числа записывается - False

2 - четное число, 2 деленное на 2, будет 1 без остатка, записывается - True

3 - нечетное, т.к 3 деленное на 2, даст остаток 1, значит вместо числа будет False

и так далее . . .

Нужно использовать comprehension.

"""
# list_ = [True if num%2 == 0 else False for num in range(1,11) ]
# print(list_)


"""
8.Создайте список из 10 произвольных имён list_name.

Затем пройдитесь по данному списку и если длина имени меньше или равна 4 буквам создайте список new_list имя на shorter, а если больше на longer.
Пример:

list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
Вывод в терминале:

['shorter', 'shorter', 'longer', 'longer', 'shorter', 'longer', 'shorter', 'longer', 'longer', 'shorter'] 
Нужно использовать comprehension.

"""
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 

# new_list = ['shorter' if len(name) <= 4 else 'longer' for name in list_name ] 

# print(new_list)

"""
9.Создайте словарь dict_ из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты. Нужно использовать comprehension.

"""
# dict_ = {key : key**2  for key in range(1,10)}
# print(dict_)


"""
10.Запросите у пользователя число от 1 до 10. 
Затем пройдитесь по промежутку чисел от 1 до 500(включительно) 
и запишите в словарь dict_, только те числа, которые кратны числу n (делятся на число n без остатка), 
введенное пользователем. 
Ключом будет само число, а значением его квадрат.

К примеру, пользователь ввел число:

9 
Получаем словарь:

{9: 81, 18: 324, 27: 729, 36: 1296, 45: 2025, 54: 2916, 63: 3969, 72: 5184, 81: 6561, 90: 8100, 99: 9801, 108: 11664, 117: 13689, 126: 15876, 135: 18225, 144: 20736, 153: 23409, 162: 26244, 171: 29241, 180: 32400, 189: 35721, 198: 39204, 207: 42849, 216: 46656, 225: 50625, 234: 54756, 243: 59049, 252: 63504, 261: 68121, 270: 72900, 279: 77841, 288: 82944, 297: 88209, 306: 93636, 315: 99225, 324: 104976, 333: 110889, 342: 116964, 351: 123201, 360: 129600, 369: 136161, 378: 142884, 387: 149769, 396: 156816, 405: 164025, 414: 171396, 423: 178929, 432: 186624, 441: 194481, 450: 202500, 459: 210681, 468: 219024, 477: 227529, 486: 236196, 495: 245025} 
Из списка чисел от 1 до 500, числа 9, 18, 27, 36, 45 ... и.т.д делятся на 9 без остатка, записываем их как ключи.

Значениями записываем квадраты(число умноженное само на себя ) - 81, т.к 9 х 9 = 81, 324, т.к 18 х 18 = 324, и.т.д

Нужно использовать comprehension.

"""
# n = int(input())
# dict_ = { num:num**2 for num in range (1,501) if num%n ==0 }
# print(dict_)


"""
11.Дан словарь a в котором значениями являются целые числа. 
Пройдитесь по элементам и запишите в dict_ значения на список чисел от 1 до числа, которое является значением. 
Нужно использовать comprehension.

Например:

 a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
 
 -> 
 
{'a': [1], 'b': [1, 2, 3, 4, 5], 'c': [1, 2, 3, 4], 'd': [1, 2, 3]}

"""
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = { key: [value for value in range(1,(value+1))] for key,value in a.items() }
# print(dict_)



"""
12.Создайте словарь dict_ где ключами будут строки, а значениями произвольные числа. 
Затем пройдитесь по элементам и запишите в a вместо значения строку 'even', если значение четное, а если нет то 'odd'.

Например, если у нас есть словарь:

dict_ = {'first': 1, 'second': 2, 'third': 3} 
То результатом будет:

{'first': 'odd', 'second': 'even', 'third': 'odd'} 

"""
# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {key :'even' if value%2 == 0 else 'odd'  for key,value in dict_.items()}

# print(a)
"""
13.Дано предложение

string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
Получите список чисел list_ из этого предложения.

Вывод будет таким:

['1984', '13', '1000'] 
Нужно использовать comprehension.

"""
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [ num for num in string_.split(' ') if num.isdigit() == True ]

# print(list_)



"""
14.Дан вложенный словарь dict_ (словарь состоящий из других словарей) в котором ключом является имя студента, а значением словарь с его оценками по 3 предметам.

Распечатайте новый словарь, где вместо оценкок будет название предмета, по которому студент имеет высший балл. Нужно использовать comprehension.

Например:

 dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
Результат:

 {'Timur': 'math', 'Olga': 'math', 'Nik': 'literature'}

"""
# dict_ = {  'Timur': {'history': 90, 'math': 95, 'literature': 91},
#             'Olga': {'history': 92, 'math': 96, 'literature': 81},
#             'Nik': {'history': 84, 'math': 85, 'literature': 87}
#         }


# res = {name : subject  for name,marks in dict_.items() for subject, score in marks.items() if score == max(marks.values())}
# print(res)

"""
15.Дан словарь my_dict значениями в котором являются другие словари.

Создайте новый словарь dict_, оставив те же ключи, но заменив значения, значениями внутренних словарей.

Например:

my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 

dict_ = {'first': 1, 'second': 2} 
Нужно использовать comprehension.

"""
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 

# dict_ = {key1 : value2  for key1,value1 in my_dict.items() for value2 in value1.values()}

# print(dict_)

"""
Экстра задание 1
* Создайте список list_ от 0 до 10 включительно c помощью специальной функции которая генерирует последовательно чисел,
* отфильтруйте список оставив в нем только четные элементы,
* затем разделите каждый элемент на 2 и выведите результат,
* нужно работать только с одним списком, нельзя создавать доп. списки.
* Необходимо использовать list comprehension
Распечатайте результат.
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0]'
"""
# list_ = [(number/2) for number in range(0,11) if number%2 ==0]
# print(list_)

"""
Экстра задание 2
Создайте словарь в котором ключами будут числа, а значениями строки,
Перебирите словарь циклом и если ключ четный, нужно заменить его значение
На длину этого значения, если ключ нечетный то возвести длинну его значения в 3 степень,
Нужно работать только с одним словарем, нельзя создавать доп. словарь.
Необходимо использовать dict comprehension
Распечатайте результат.

"""
# dict_ = {1:'hello',2:'world', 3:'John'}

# dict_ = { number :len(letter) if number%2 ==0 else (len(letter))**3 for number,letter in dict_.items()}

# print(dict_)

"""
Экстра задание 3
Создайте 2 сета set1 и set2 из 10 рандомных элементов
Затем объедините их (специальным методом) в перменную full_set,
И если их длина меньше 20, то вы должны вывести сообщение:
"В этом сете было 3 повторения, его длина составляет 17",
3 это количество элементов, которые были не уникальны,
Если же длина равна 20 то выведите сообщение "Ваш обьединенный сет полностью уникальный!"
Необходимо использовать set comprehension, на этапе создания сетов.
Так же используйте генератор последовательности в comprehension чтобы создать множества из 10 элементов.
Необходимо использовать set comprehension, на этапе создания сетов.
Например после использования set comprehension 
в set1 храниться множество: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
B set2: {8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
Результат работы программы будет следующий:
"В этом сете было 2 повторения, его длинна составляет 18"
"""

# set1 = {i for i in range(2,12)}
# set2 = {i for i in range(8,18)}

# full_set = set1.union(set2)
# if len(full_set)<20:
#     print(f'В этом сете было {len(set1.intersection(set2))} повторения, его длинна составляет {len(full_set)}')
# elif len(full_set)==20:
#     print(f'Ваш обьединенный сет полностью уникальный!')

"""
Тема пройдена!!!
"""