"""
День 2. Неделя 8. 7 декабря.
Тема: ORM

ORM - (Object-relational mapping)- это технология программирования, которая позволяет преобразовывать несовместимые типы 
моделей в ООП, в частности, между хранилищем данных и объектами программирования.

ORM - это прослойка между базой данных и кодом, который пишет программистю

ORM используется для упрощения процесса сохранения объектов в реляционную базу данных и их извлечения.

Ключевой особенностью ORM является отображение, которое используется для привязки объекта к его данным в БД.

ORM автоматизирует трансфер данных, хранящихся в таблицах вашей БД в объекты, которые используются в программном коде.

Для языка Python существуют:
1. peewe
2. sqlalchemy
3. ponyORM
4. django ORM


ORM концепция                       Концепция базы данных

Класс модели                        Таблицв базы данных

Поле класса(атрибут класса)         Колонка в таюлие базы данных

Экземпляр модели(объект)            Строка в таблице базы данных


Плюсы и минусы использования ORM:
+ Использование ORM в проекте избавляет разработчика от необходимости работы с SQL и написания большого количества кода.
- Потеря производительности.

Начало практики:
1.psycopg:
- Установка, подключение
- Создание таблиц, составление запросов
2. ORM SQLAlchemy
- Преимущества SQLAlchemy
- Установка, подключение
- Создание таблиц, составление запросов.



"""
"""
Для подключнения к psycopg2 - нужно установить виртуальное окружение

"""
# import psycopg2

# connection = psycopg2.connect(
#     database = 'db_practice',
#     user = 'ananas',
#     password = '1',
#     host = 'localhost', 
#     port = '5432'
# )
# print('Database succesufully opened')

# cursor = connection.cursor()



'''
#1
После выполнения создания таблицы
Лучше закомментировать, а лучше удалить код ниже
'''
# cursor.execute(
#     '''
#     CREATE TABLE company(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100) NOT NULL,
#         city VARCHAR(50) NOT NULL)
#     '''
# )
# print('Table sucessfully created')
# connection.commit()
# connection.close()


'''
#2
Также закрываем, чтобы она не срабатывала дважды

'''
# cursor.execute(
#     '''
#     INSERT INTO company(name,city) VALUES
#     ('IBM', 'Los Angeles'), ('Apple', 'Cupertino'),
#     ('HP', 'New York'), ('Dell', 'New Jersey')
#     '''
# )
# connection.commit()
# print('Inserted successfully')
# connection.close()



'''
#3
Как видно в примере ниже можно использовать сразу несколько exucute()
'''

# cursor.execute(
#     '''
#     INSERT INTO company(name, city) VALUES ('Samung', 'Seul')
#     '''
# )
# cursor.execute(
#     '''
#     INSERT INTO company(name, city) VALUES ('Samung', 'Seul')
#     '''
# )
# connection.commit()
# print('Inserted successfully')
# connection.close()


'''
#4
Извлекаем данные
Здесь мы не используем commit -  так как он отвечает за сохранение изменения в нашу базу данных, а мы их сейчас не проводим

'''
# cursor.execute(
#     'SELECT  * FROM company'
# )
# # print(cursor.fetchall()) #[(1, 'IBM', 'Los Angeles'), (2, 'Apple', 'Cupertino'), (3, 'HP', 'New York'), (4, 'Dell', 'New Jersey'), (5, 'Samung', 'Seul'), (6, 'Samung', 'Seul')]
# data = cursor.fetchall()
# for item in data:
#     # print(f'id: {item[0]}, name: {item[1]}, city: {item[2]}')
#     print(*item)
# connection.close()



'''
#5 Получаем один объект используя fetchone()
'''
# cursor.execute(
#     'SELECT name,city FROM company WHERE id=2'    
# )
# data = cursor.fetchone()
# print(data)
# connection.close()


'''
#6. Update
'''
# cursor.execute(
#     '''
#     UPDATE company SET city = 'Tokio' WHERE id = 6
#     '''
# )
# connection.commit()
# cursor.execute('SELECT * FROM company')
# data = cursor.fetchall()
# for item in data:
#     print(*item)
# connection.close()

'''
#7
Удалени строки
'''
# cursor.execute(
#     '''
#     DELETE FROM company WHERE id = 5
#     '''
# )
# connection.commit()
# print(f'Total count of deleted: {cursor.rowcount}')
# cursor.execute(
#     'SELECT * FROM company ORDER BY id'    
# )
# data = cursor.fetchall()
# for item in data:
#     print(*item)
# connection.close()


"""
SQLAlchemy -  ORM, а psycopg2-это драйвер
Преимущества ORM SQLAlchemy:
- Безопасность
- Производительность
- Переносимость


"""
# from sqlalchemy import create_engine
# from sqlalchemy.sql.expression import insert

# engine = create_engine('postgresql+psycopg2://ananas:1@localhost:5432/db_practice')
# '''\c db_practice'''
# print('Database connected')

# from sqlalchemy import Column, Table, Integer, String, MetaData

# metadata = MetaData()
# students_table =  Table(
#     'students', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('last_name', String)
# )
'''Комменируем после запуска программы'''
# students_table.create(bind=engine)
# print('Sucessfully created')

'''После запуска вставки, комментируем'''
# inserted_data = students_table.insert().values(name='Mark', last_name = 'Twan')

# engine.execute(inserted_data)
# print('Successfully inserted')

'''SELECT  данные из таблицы'''
# from sqlalchemy import select
# query = select([students_table.c.name, students_table.c.last_name])
# data =  engine.execute(query).fetchall()
# for item in data:
#     print(*item)

"""
Ещё один способ создания таблиц используя SQLAlchemy
"""
# from sqlalchemy import create_engine
# from sqlalchemy.sql.expression import insert

# engine = create_engine('postgresql+psycopg2://ananas:1@localhost:5432/db_practice')

# from sqlalchemy import Column, Table, Integer, String, MetaData

# metadata = MetaData()
# company_table =  Table(
#     'company', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('city', String)
# )
# metadata.create_all(engine)

# class Company:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

#     def __str__(self):
#         return f'Company {self.name} in {self.city} city'

# from sqlalchemy.orm import mapper
# mapper(Company, company_table)
# print('Succefuuly created table')




"""
Другой способ
Более простой
"""
# from sqlalchemy import create_engine
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import session, sessionmaker
# from sqlalchemy.sql.expression import select
# engine = create_engine('postgresql+psycopg2://ananas:1@localhost:5432/db_practice')


# Base = declarative_base()

# class Company(Base):
#     __tablename__ = 'company'
#     id = Column(Integer, primary_key = True)
#     city = Column(String)

#     def __init__(self,name, city):
#         self.name = name
#         self.city = city

#     def __str__(self):
#         return f'Company {self.name} in {self.city} city'

# Base.metadata.create_all(engine)
# print('Table created')

# Session = sessionmaker(bind=engine)
# session = Session()
# apple = Company(name = 'Apple', city = 'Cuppertino')
# # session.add(apple)
# # session.commit()

# query = session.query(Company.city)
# print(query)

# samsung = Company('Samsung' 'Seoul')
# session.add(samsung)
# session.commit()





"""
Начало разбора

psycopg2
sqlalchemy


"""
import psycopg2
from sqlalchemy.sql.sqltypes import DECIMAL, Numeric
connection = psycopg2.connect('dbname = practice user=ananas password = 1 host = localhost port=5432')
print(connection)


'''Cursor - промежуточная памятб для сохранения запросов'''

cursor = connection.cursor()

#SELECT
cursor.execute('SELECT * FROM products;')
results = cursor.fetchall()
print(results)

#получаем одну запись
cursor.execute('SELECT * FROM  products WHERE id = 1;')
product = cursor.fetchone()
print(product)


max_price =55000
cursor.execute('SELECT *FROM product WHERE  price < %s;', (max_price, ))
results = cursor.fetchall()

min_price = 20000
max_price = 50000


cursor.execute('SELECT * FROM  products WHERE price BETWEEN  $s AND %s;', (min_price, max_price))
results = cursor.fetchall()


new_product = {'name': 'Hisense 43 Smart TV', 'price': 20000, 'category': 'tv'}
cursor.execute('INSERT INTO products(name, price, category) VALUES (%(name)s, %(price)s, %(category)s)', new_product)

connection.commit()


from sqlalchemy import create_engine,Column, SmallInteger, String, NUMERIC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://ananas:1@localhost:5432/practice')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Product:
    __tablename__ = 'products'

    id = Column(SmallInteger, primary_key=True)
    name = Column(String)
    price = Column(Numeric(10,2))
    category = Column(String(30))

#SELECT
products = session.query(Product).all()
#INSERT
#UPDATE
#DELETE


"""


"""


"""

"""


"""

"""


"""

"""


"""

"""

"""



"""





"""


"""


"""

"""


"""

"""


"""

"""


"""

"""

"""



"""



"""


"""


"""

"""


"""

"""


"""

"""


"""

"""

"""



"""



"""


"""


"""

"""


"""

"""


"""

"""


"""

"""

"""



"""



"""


"""


"""

"""


"""

"""


"""

"""


"""

"""

"""



"""

