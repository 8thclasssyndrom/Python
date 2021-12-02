"""
1) Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, 
с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник.
"""
# from datetime import datetime

# class Clock:
#     def show_time(self):
#         return f'Текущее время: {datetime.now()}'

# class Alarm:
#     def on(self):
#         return 'Будильник включен'

#     def off(self):
#         return 'Будильник выключен'

# class AlarmClock(Clock, Alarm):
#     def set_alarmclock(self):
#         self.on()
#         print(self.on())
#         print('Будильник запущен')


# alarm = AlarmClock()
# print(alarm.show_time())
# alarm.set_alarmclock()

"""
2) Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, класс, и 
оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
"""
# class Student:
#     def __init__(self, name, last_name, klass, scores):
#         self.name = name
#         self.last_name = last_name
#         self.klass = klass
#         self.scores = scores
#         self.mid_scores = sum(list(self.scores.values())) / len(list(self.scores.values()))
    
#     def __gt__(self,other):
#         print(self.mid_scores)
#         if self.mid_scores > other.mid_scores:
#             return f'Средний балл студента {self.name} больше, чем средний балл студента {other.name}' 
#         else:
#             return f'Средний балл студента {self.name} меньше, чем средний балл студента {other.name}' 

# student1 = Student('Jane', 'Foster','7', scores = {'math': 100, 'history': 89, 'literature': 88})
# student2 = Student('Kate', 'Foster','7', scores = {'math': 100, 'history': 100, 'literature': 100})
# print(student1 > student2)

    

"""
3) Напишите класс учеников Makers, который будет содержать 4 атрибута: 

- атрибут экземпляра name (имя студента)
- атрибут класса students_count (количество учеников)
- атрибут экземпляра класса language (язык, которому обучается студент)
- атрибут экземпляра класса kpi (оценка студента)

Также класс должен содержать следующие методы:

- метод, который будет создавать нового ученика, и при этом увеличивать количество студентов на 1.
- метод который будет выводит имя и язык, выбранный учеником.
- а также метод, который будет устанавливать оценку ученику.
"""
# class Makers:
#     students_count = 0

#     def __init__(self, name, language):
#         self.name = name
#         self.language = language
#         self.kpi = 0

#     @classmethod
#     def new_students(cls, name, language):
#         cls.students_count +=1
#         return cls(name, language)
    
#     def get_info(self):
#         return f'Студент {self.name} выбрал {self.language} для изучения'
    
#     def set_kpi(self, kpi):
#         self.kpi = kpi
#         return f'У студента {self.name} KPI равен {self.kpi}'

# student1 = Makers.new_students(name = 'Itachi', language ='Java')
# student2 = Makers.new_students('Sasuke', 'Python')
# print(student1.get_info())
# print(student1.set_kpi(100))
# print(student2.students_count)

"""
4) Dollar.
Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
долларизованный формат:

dollarize(123456.78901) -> "$123,456.80"
dollarize(-123456.7801) -> "-$123,456.78"
dollarize(1000000) -> "$1,000,000"

Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
- init - инициализирует значение атрибута amount
- update - задаёт объекту новое значение amount
- repr - возвращает значение float
- str - метод, который реализует логику функции dollarize()

//Вывод должен выглядеть следующим образом:
cash = MoneyFmt(12345678.021)
print(cash) -- выводит "$12,345,678.02"
cash.update(100000.4567)
print(cash) -- выводит "$100,000.46"
cash.update(-0.3)
print(cash) -- выводит "-$0.30"
repr(cash) -- выводит -0.3
"""

# class Dollar:
#     @staticmethod
#     def dollarize(money):
#         if  money > 0:
#             money = '${:,.2f}'.format(money)
#             return money
#         else:
#             money = abs(money)
#             money = '${:,.2f}'.format(money)
#             return f'-{money}'
# class MoneyFmt(Dollar):
#     def __init__(self, amount):
#         self.amount = amount
    
#     def update(self, new_amount):
#         self.amount = new_amount
    
#     def __repr__(self) -> str:
#         return f'{self.amount}'
    
#     def __str__(self) -> str:
#         return self.dollarize(self.amount)

# cash = MoneyFmt(12345678.021)
# print(cash) 
# cash.update(100000.4567)
# print(cash) 
# cash.update(-0.3)
# print(cash) 
# repr(cash) 