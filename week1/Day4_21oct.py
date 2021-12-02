"""
Закончен, но тасков здесь нет
Начинаем практику по теме строки в Python
Сегодня мы будем изучать строки, методы строк и операции со строками
"""
# string1='Make
# string2='Bootcamp'
# print(string1,string2)
"""
В Python при использовании кавычек в самом предложении мы будем использовать ", если мы используем для строки ' 
И если в предложении есть ', то используем "
Также для строк можно использовать три кавычки для комментрирования
Ниже представлены примеры:
"""

#  string3="Maker's Bootcamp"
# print(string3)
# string = 'Maker"s Bootcamp'
# print(string)

# sentence= "John said:'I can code"
# print(sentence)
# sentence = "I love Maker\"s Bootcamp"
# print(sentence)
"""
Символ / можно использовать как разделить строки, чтобы переместить предложение в следующую строку
Сочетание /n осуществялется перенос на следующую строку
Сочетание /r осуществляет перенос на следующую строку и начинает предложение с конца последней строки, создавая своебразную лесенку
Сочетани /t осуществляет табуляцию
"""
# string = 'Dear friend,\n\nWelcome to Makers Bootcamp!\nEnjoy ypur time here with us'
# print(string)

"""
Пример для сравнения с использованием трёх кавычек
"""
# string= """Dear friend,
# Welcome to Makers Bootcamp!
# Enjoy ypur time here with us"""
# print(string)

# languages = 'Languages:\n\t'
# description = 'Python: backend language\n\t Java Script: fronted language'
# print(languages, description)

"""
Будем проходить потом это цикл и использование слэша с ним
"""
# loop = 'for i in range(5):\n\tprint(i)'
# print(loop)
"""
Сочетание /v разделяет строку по вертикали 
"""
# sentence = "Hello\v Makers\v Bootcamp\v John"
# print(sentence)
"""
Пример с url, где имеются большое количество слэшей и может возникнуть ошибка, в таком случае используем сочетание r''.
С её помощью мы сможем вывести строку без ошибок
"""
# url = r'https://kaktus/\news/topics/\read'
# print(url)
"""
Пример кода с использованием разделения по вертикали и умножением строки на число
"""

# string = 'makers'
# print('string\v'*100)
"""
Вычисляем длину строки с помощью функции len()
"""
# string = 'makers Bootcamp'
# print(len(string))

# length = len ('John')
# print(length)
"""
Срез в строках. Примеры:
При использовании [::2] мы получаем символы каждый второй символ + 1 символ, если хотим без первого символа используем [1::2]
При использовании [:-1] получаем обратную нашей строки результат

"""
# sentence = 'Strings are ordered'
# print(sentence[0])
# print(sentence[6])
# print(sentence[7])
# print(sentence[-1])


"""
[:y]
"""
# string = 'Makers Bootcamp'
# print(string[::3])

# part_string = string[:-3]
# print(string[-2:3])
# print(string[1:3])
# print(string[1::-3])
"""
Пример среза с выделением определенного символа и сложением с остальной частью слова
"""

# word = 'dream'
# # word[0] = 'c'
# word = 'c' + word[1:]
# print(word)
"""                                   Методы строк            """
"""find(string)-поиск символа или слова в строке и дальнейший ее вывод в терминал"""

# string = 'Makers Bootcamp Boot Boot'
# print(string.find('Make'))

"""
index(string), rindex(string)- возвращает номер первого вхождения
"""

# string = 'Makers Bootcamp Boot Boot'
# print(string.rindex('camp'))


""" 
replace(patter, replace_pattern)- меняет
"""

# string = 'Makers Bootcamp Makecamp'
# print(string.replace('camp', 'rock', 2))
 
#  split(symbol) -> list 
# string='#Makers#Bootcamp#cool'
# print(string[1:-1].split('#',3))

# full_name = input('Enter name and last name: ').split(,)
# name = full_name[0]
# last_name = full_name[-1]
# print(name)
# print(last_name)


# isdigit(), isalpha(), is alnum(), islower(), isupper()
# isspace(),istitle() -> return bool(T or F)

# string = 'asss'
# print(string.isalpha())
# print(string.isalnum())
# print(string.isspace())
# print(string.istitle())


"""
upper()- используется для преоброзования строк в верхний регистр.
lower()- используется для преобразования строк в нижний регистр.
"""
# string = 'Makers'
# print(string.upper())
# print(string.upper())
"""
startswith()- для выяснения начинается ли строка с определенной буквы или нет, enswith()
"""
# string='Makers'
# print(string.endswith('M'))

# join(list) only list type 
# list_ = ['m', 'a', 'k','r','e', 's' ]
# print('!'.join(list_))



"""
capitalize() - меняет первый символ на верхний регистр. 
Отличается от title тем, что не меняет каждое, начинающее слово на верхний регистр, а только первый в строке
"""

# string = 'bootcamp makers'
# print(string.capitalize())

"""
count()- возвращает количество вхождений подстроки
"""
# string = 'Makers rrr '
# print(string[:-6].count('r'))
"""

lstrip(), rstrip(), strip()- delete space symbol from left, right and all sides

"""
# password = '  qweerty   '
# print(len(password))
# print(password.lstrip())

# partition('patter') - возвращает в  виде кортежа tuple
# string = "Hello lovely Makers Bootcamp"
# print(string.partition('Mkers'))


# swapcase() - меняет верхний регистр на нижний и наоборот

# string = 'CameCase'
# print(string.swapcase())


# zfill(width) заполяет все недостойщуе символы нулями впереди

# string = 'makers'
# print(string.zfill(100))

# ljust(width, fillchar), rjust(width, fillchar) заполняет  недостающие элементы 
# символами, которые мы указываем 

# string = 'makers'
# print(string.ljust(13,'%'))
# print(string.rjust(10,'4'))


# format() 
"""
Форматирование строк
"""
"""
1.%
% Чекнуть в видео практику. Этот момент я неправильно написала

"""

# name = input ()
# last_name = input()
# age = int(input())
# some_variable = "Welcome, %s %s, age %d" %(name, last_name)
# print(some_variable)

""" 
2. format()
Здесть вместо процентов на месте нужных нам переменных мы оставляем пустые скобки {}

"""
# name =input()
# last_name=input()
# variable = 'Hello,{1} {1}'. format(last_name, name)
# print(variable)

"""
 3.f''
Самый удобный и простой, будет использоваться чаще. Суть этих f'' строк в том, что в самe строку вписать 
переменную посредством заключения их в фигурные скобки {} и получить более простой и наглядный результат.
"""
# name = input()
# last_name = input()
# age = input()

# variable = f'Hello {name} {last_name}\nYour age is {age}'
# print(variable)

# string1 = 'Makers'
# string2 = 'Bootcamp'
# print(f'I study at {string1} {string2}')
# print(f'I study at {string1} {string2}')
"""
Classwork
Классная работа
"""
"""
1) Напишите программу, которая будет запрашивать пользовательские данные: имя, фамилию, возраст. Далее программа должна проделать следующие операции: в имени убрать все буквы ‘a’(если они есть), в фамилии - разделить все буквы разделителем *. В конце программа выдает вам объединенную строку, состоящую из полученных имени и фамилии, при этом данная строка должна повторяться столько раз, сколько составляет возраст пользователя.

Например:
Ввод: Введите имя, фамилию и возраст через пробел: John Snow 4
Вывод: JоhnS*n*o*wJоhnS*n*o*wJоhnS*n*o*wJоhnS*n*o*w

"""
#писать код здесь
# import dataclasses
# data = input('Введите имя, фамилия и возраст через пробел:\n').split()
# name = data[0]
# print(type(name))
# last_name = data[1]
# age = data[-1]

# name = name.lower().replace('a','').title()
# print(type(name))
# last_name = '*'.join(list(last_name))
# print((name + last_name)*int(age))



"""
2) Напишите программу, которая высчитывает количество гласных букв в введенной пользователем строке. И программа выдает вам следующее предложение: В вашей строке насчитано n гласных букв.

Например:
Ввод: Введите строку: I love Makers Bootcamp!
Вывод: В вашей строке насчитано 8 гласных букв

Примечание: не использовать конкатенацию

"""
# string = input('Enter a string: ')
# a = string.count('a')
# o = string.count('o')
# i = string.count('i')
# u= string.count('u')
# y = string.count('y')
# e = string.count('e')

# print(f'In your string counted {a+o+i+u+e+y} гласных букв')

"""
3) Напишите программу, которая просит пользователя ввести свой юзернейм (одним словом) и генерирует пароль из юзернейма,
добавив в конец строки символ $, в середину символ &, и заменив строчные буквы на заглавные и наоборот.

Например:
Ввод: Введите юзернейм: JohnSnow
Вывод: Вам сгенерирован пароль: jOHN&sNOW$
"""
# username = input('Enter your username: ')
# center = int(len(username)/2)
# new_username = username[:center] +'&' + username[center:] + '$'
# password = new_username.swapcase()
# print(f'You passwaord was generted: {password}')

# Библиотека - хранит модули
# Фрэймворк -сборник библиотеки
# Модуль -весь функционал : методы, функции и типы