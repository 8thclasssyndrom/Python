"""
День 1. Неделя 5. 15 ноября
Тема: Повтор тем
"""

"""
Разбор с Жаннатом

Стоит разобрать дома
Не совсем поняла                 /     /
Точнее вообще не догнала |:->()|-------
                                 \     \
"""

# data_base = list()
# data_base_profile = {}
# id = 0

# def registr(email:str, password:str, name="AnonymusUser", *args, **kwargs): #логика регистрации 
#     email_list = ['@gmail.com', '@yandex.ru', '@mail.ru']
#     count = 0

#     data = data_base_email(flag=True)

#     for user in data:
#         if user['email'] == email:
#             raise ValueError('Пользователь с таким email существует') 

#     for email_name in email_list:
#         if email.endswith(email_name):
#             count += 1
#             break
    
#     if not count:
#         raise ValueError(f'email должен быть зареган на таких сервисах {email_list}')

#     if len(password) >= 8:
#         if password == kwargs['password_confirm']:
#             print(data_base_email(email=email, password=password, name=name))
#             print(f'Пользователь с email-ом: {email} был создан')
#         else:
#             raise 'Пароли не совпадают'
#     else:
#         raise 'Длина пароля должно быть не меньше 8 символов'


# def data_base_summa(id_user, summa): #базаданных профиля кошелка
#     global id
#     data = data_base_email(flag=True)
#     for user in data:
#         if user['id'] == id_user:
#             if user['login']:
#                 data_base_profile.update({'id': id, 'id_user': id_user, 'summa': summa})
#                 return 'Ваш профиль был успешно создан'
#             else:
#                 return 'эээ Дурак залогинься'
#         else:
#             raise f'нет такого пользователя с id: {id_user}'


# def data_base_email(flag=False, **kwargs): #базаданных email
#     global data_base, id

#     if flag:
#         return data_base
#     else:
#         data_base.append({"id": id, "email": kwargs.get('email'), 'password': kwargs.get('password'), 'first_name': kwargs['name'], 'login': False})
#         id += 1
#         return f'Пользователь был добален с id: {id}'


# def login(*args): #логика авторизации 
#     try:
#         email = args[0]
#         password = args[1]
#     except IndexError:
#         print("Ты не полностью передал входные данные")
#     else:
#         data = data_base_email(flag=True)
#         print(data)
#         for user in data:
#             if user.get('email') == email and user.get('password') == password:
#                 user['login'] = True
#                 id = user['id']
#                 return f'Ты успешно залогинелись ваш id: {id}'


# dict_acction = {
#     1: registr,
#     2: data_base_email,
#     3: login,
#     4: data_base_summa
# }


# def main(): #главная функция
#     TEXT = 'Здорово смотри есть такое, как \n1) регистрация\n2) Вывод базыданных '
#     print(TEXT)
#     while True:
#         number = int(input('Введите выбор: '))
#         if number == 0:
#             break
#         elif number == 1:
#             result = dict_acction[1]
#             result(email='test@mail.ru', password='12345678', password_confirm='12345678')
#         elif number == 2:
#             result = dict_acction[2]
#             print(result(flag=True))
#         elif number == 3:
#             result = dict_acction[3]
#             print(result('test@mail.ru', '12345678'))
#         elif number == 4:
#             result = dict_acction[number]
#             print(result(0, 15500))
#         elif number == 5:
#             print(data_base_profile)


# if __name__ == '__main__':
#     main()


"""
Функция
"""

# def get_formated_name(name: str,middle_name = None,last_name = 'Uchiha'):
#     """ Выводит фамилию и имя """
#     if middle_name:
#         return name + ' ' + middle_name + ' ' + last_name
#     return name + ' ' + last_name

# print(get_formated_name('itachi', middle_name= 'izuna').title())


# m = list(map(int, ['1','2','3']))
# print(m)


# f = list(filter(lambda x:x %2 ==0,[1,2,3,4,5]))
# print(f)


# d = dict(zip([1,2,3],['a','b','c']))
# print(d)

"""
Task
"""

#2

# def season(month):
#     if  month not in range(1,13):
#         raise  ValueError('Укажите правильный месяц')

#     if month in range(3,6):
#         return 'Весна'
#     elif month in range(6,9):
#         return 'Лето'
#     elif month in range(9,12):
#         return 'Осень'
#     else:
#         return 'Зима' 
    
# month = int(input('Enter month: '))
# print(season(month))

#3

# def date(day,month, year):
#     if day in range(1,32) and month in range(1,13) and year in range(0,2022):
#         return True
#     else:
#         return False

# print(date(2,2,2003))

#4

# a = [i for i in range(70,100) if i%2==1]
# print(a)

#5

# names = ['Valentin','Petr','Anna','Sam','Raychel','Bob','Emily','Kate','Joahn','Federick']
# list_ = [i for i in names if len(i) <5 ]
# print(list_)

#6

# nums  =[1,77,12,3,0,112,-978]
# num = [x**2 if x<5 else x-2 for x in nums]
# print(num)

#7

# x = int(input('Enter the number: '))
# list_ = [i**2 for i in range(0,x)]
# for i in list_:
#     print(i)


#8

# list_ = ['четное' if i %2==0 else i for i in range(1,10)]
# print(list_)


#9

# fruits = {'apple': 25, 'banana': 40, 'mango': 17, 'orange': 12}
# dict_ = {key: value for key,value in fruits.items() if value %2 ==0}
# print(dict_)

#10

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {key: list(range(value+1)) if value >1 else value for key,value in a.items() }
# print(dict_)

"""
Эстафета
"""
"""
Задание 1
"""

# import math
# def m(a):
#     p = 4*a
#     s = a**2
#     d = a* math.sqrt(2)
#     print(p,s,d)
# m(4)


"""
Задание 2
"""
# a=1
# b=2
# c=3
# a,b,c = (a+b),(c-b),(a+b+c)
# print(a,b,c)


"""
Задание 3
"""
# a = input('Введите четырёхзначное число: ')
# if not sorted(a) == list(a):
#     print('Yes')
# else:
#     print('No')

"""
Задание 4
"""
# list_of_numbers0 = [ i for i in range(10000,99999) if i %2 ==0]
# list_of_numbers1 = [i for i in list_of_numbers0 if int(str(i)[2])%2==1]
# list_of_numbers2 = [i for i in list_of_numbers1 if sum(list(map(int,str(i))))%4 ==0]
# print(list_of_numbers2)

"""
Задание 5
"""
# a = input('Введите четырёхзначное число: ')
# a = list(a)
# if a[0] > a[-1]:
#     a[0] = a[-1]
#     a[-1] = a[0]
# print(''.join(a))


"""
Задание 6
"""
# geo_logs = {'visit2':['Дели', 'Индия'], 'visit3':['Владимир','Россия'],'visit9':['Курск','Россия']}
# geo_logs ={key:value for key,value in geo_logs.items() if 'Россия' in value}
# print(geo_logs) #{'visit3': ['Владимир', 'Россия'], 'visit9': ['Курск', 'Россия']}


"""
Задание 7
"""
# x = int(input('Введите сколько килограмм конфет стоят a рублей: '))
# a = int(input('Введите сколько стоит x килограмм конфет: '))
# price_for_kg = a/x
# y = int(input('Введите кг конфет, чтобы посчитать их цену: '))
# print(price_for_kg*y)
# k =int(input('Введите цену, чтобы узнать сколько кг конфет можно купить: '))
# print(k/price_for_kg)


"""
Задание 8
"""
# for i in range (1, 50):
#     if i% 3==0 and i % 5 ==0:
#         print('FizzBuzz')
#     if i % 3 == 0:
#         print('Fizz')
#     if i % 5 == 0:
#         print('Buzz')



