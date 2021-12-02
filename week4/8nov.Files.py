"""
День 1. Неделя 4. 8 ноября
Тема: Работа с файлами

Работа с файлами. Модули
Файл — это всего лишь набор данных, информация хранится в "куче" данных (структура данных) и имеет название «имя файла». 
Текстовые файлы - это файлы с человекочитаемым содержимым. В них хранятся последовательности символов, которые понимает человек. 


Текст может храниться в двух форматах: (.txt) — простой текст и (.rtf) — «формат обогащенного текста».

Открытие файла

В Python есть встроенная функция open(). С ее помощью можно открыть любой файл на компьютере.

f = open(имя файла, режим) 
f - это переменная где будет хранится результат нашей работы с файлом

имя файла - имя открываемого файла

режим - режим открытия файла. Он может быть: для чтения, записи и.т.д. 
По умолчанию используется режим чтения r, если другое не указано.

"""

"""
Начало практики

"""
# file1 = open('makers.txt','r')
# print(file1.read())

# file1 = open('/home/ananas/Desktop/python_15/week2/text.txt','r')
# print(file1.read())

"""
r - read
r+ - read + write
w -write
w+ = write + read
a - append(дозапись)
a+ - append + read
x - write(for non-existence file)

b - bynary(двоичная)
t -text(текствая)
rt - > r (стоит по умолчания)
rb -> b

"""

# file1 = open('makers.txt','r')
# data = file1.read()
# print(type(data)) # str

# file1 = open('makers.txt','r')
# data = file1.read(10)
# print(data) #hello worl

# file1 = open('makers.txt','r')
# print(file1.read(10)) #20 сентябр
# file1.seek(0)
# print(file1.read(5)) #20 се



"""
seek ()- ставит курсор в любое место строки 

file1.seek(4)


"""
# file1 = open('makers.txt','r')
# print(file1.read(21))
# file1.seek(20)
# print(file1.read(10))

"""
readline()

"""

# file1 = open('makers.txt','r')
# for line in file1:
#   print(file1.readline()) # получим весть текст

"""
readlines() -

"""

# file1 = open('makers.txt','r')
# list_ = file1.readlines()
# list_ = [line.replace('\n','') for line in list_]
# print(list_)

"""
write -

"""
# file2 = open('bootcamp.txt','a')
# print(file2.write('Bootcamp'+'\n'))

# file2 = open('nakers2.txt','x')
# print(file2.write('Bootcamp'))

"""


"""
# file2 = open('bootcamp.txt', 'w')
# file2.write("It's such a beatiful day")
# file2.write('Today is my birthsday' + '\n')

# list_motos = ['Just do it.','Good day for cofee!','Gotcha...',
# 'Become a star@']
# list_motos = [motto +'\n' for motto in list_motos]
# file2.writelines(list_motos)


# file2 = open('bootcamp.txt', 'w')
# dict_ = {'name':'July','age':18}
# file2.writelines(dict_)

"""


"""

# file3 = open('file11.txt', 'w')
# list_mottos = ['Just do it.\n','Good day for cofee!\n','Gotcha...\n',
# 'Become a star@\n']
# file3.write('My mottos: \n')
# for motto in list_mottos:
#   file3.write(motto)
# file3.close()
# print(file3.closed)

"""
with - оператор который автоматически закрывает файл

"""

# with open('file11.txt','r+') as my_file:
#   print(my_file.read())
#   my_file.write('This is end')
# print(my_file.closed) #True

"""
Модуль - содержит коллекцию функций и методов

math,random,datetime
Чтобы использовать сторонние библеотеки

"""




"""
Классная работа
Classwork

1) Создайте файл numbers.txt и напишите скрипт, который запишет в этот файл числа от 1 до 20. 
Затем создайте файл squares.txt. Напишите скрипт, который будет считывать числа из файла numbers.txt и 
записывать квадраты этих чисел в файл squares.txt
"""
# писать код здесь

# with open('numbers.txt','w') as file1:
#     for number in range(1,21):
#         file1.write(str(number) + '\n')
# with open('squres.txt','w') as file2:
#     with open('numbers.txt') as file1:
#         data = file1.read()[:-1].split('\n')
#         new_data = list(map(int, data))
#         for number in new_data:
#             file2.write(str(number**2)+'\n')
            


"""
2) Создайте файл usernames.txt. Напишите скрипт, который будет запрашивать у пользователя имена, а эти имена будут 
помещаться в файл usernames.txt. При этом напротив каждого имени будет записано количество букв в юзернейме. 
Программа запрашивает имена до тех пор, пока пользователь не введёт слово: End.
"""
# писать код здесь

# with open('usernames.txt','w') as my_file:
#     while True:
#         username = input('Enter username: ')
#         if username.lower() == 'end':
#             break
#         my_file.write(f'{username} - {len(username)} \n')



"""
Task
Таски


1.Откройте файл task1.txt. В нём записаны числа от 1 до 10 в столбец. Выведите первые 5 элементов в вашем файле в терминал

Примерный вывод:

1 
2 
3 
4 
5 
(Подсказка: используйте метод для построчного считывания).

"""

# with open('task1.txt','r') as f:
#     for line in f.readlines(8):
#         print(line)


"""
2.Откройте файл task2.txt. В нём записаны числа от 1 до 10 в столбец. Распечатайте все числа, не используя методы.

Вывод в терминале должен быть:

1 
2 
3 
4 
5 
6 
7 
8 
9  
10 

"""

# with open('task2.txt','r') as file1:
#     for line in file1:
#         print(line)


"""
3.Откройте файл task3.txt в режиме записи. Запишите в него числа от 0 до 9 через символ *. 
Затем вернитесь в начало файла и распечатайте записанные числа. Вывод должен быть:

0*1*2*3*4*5*6*7*8*9*

"""

#только этот принимает 

# with open('task3.txt','w') as file1:
#   file1.write('0*1*2*3*4*5*6*7*8*9*')
# with open('task3.txt','r') as file1:
#     print(file1.read())

"""
Откройте файл task4.txt. В нём в нескольких строках записан текст. Прочтите содержимое и распечатайте количество строк.

К примеру, если там записано:

Hey there, Delilah

What's it like in New York city?

I'm a thousand miles away

But, girl, tonight you look so pretty

Yes, you do

Выводом будет:

5 

"""

# with open('task4.txt','r') as file1:
#     res = 0
#     for i in file1.readlines():
#         res+=1
#     print(res)

"""
5.Откройте файл task5.txt. В нём записаны целые числа. Прочтите эти числа, затем найдите максимальное затем минимальное число. 
Затем запишите эти числа в новый файл task6.txt через символ - (сначала минимальное, потом максимальное)

В task5.txt записаны:

45 
21 
67 
291 
13 
45 
166 
12 
1 
456 
86 
42 
45 
12 
90
В файле task6.txt должна быть такая запись:

1 - 456 

"""

# with open('task6.txt','w+') as file2:
#     with open('task3.txt','r') as file1:
#         numbers = file1.readlines()
#         numbers = [int(item.replace('\n','')) for item in numbers]
#         file2.write(f'{min(numbers)} - {max(numbers)}')
#         file2.seek(0)
#         print(file2.read())

