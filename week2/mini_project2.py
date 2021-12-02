"""
ТЗ “Угадай число” 
Напишите мини-проект “Угадай число”. 
Для этого, вам понадобиться стандартный ввод/вывод данных, тип данных числа и условные операторы. 
Также не забудьте использовать библиотеку random. 
Требования: 
1. Ваша программа должна запрашивать имя пользователя. 
   Программа должна запросить у пользователя хочет ли он играть или нет. 
   Если ответ будет ‘нет’, то программа должна завершиться. 
2. Далее пользователь должен угадать число. 
   Также вы должны сделать счетчик попыток, и показать пользователю сколько 
   попыток ему потребовалось, чтобы отгадать число. 
3. Если пользователь угадал число, запросить у него хочет ли он пройти игру еще раз, если ответ будет “нет”, 
   программа должна завершиться
"""
      
# import random
# print( 'Начнём игру "Угадай число!"')
# name = input('Введите своё имя: ')
# question = input('Хотите ли вы сыграть ?\nВведите Да или Нет: ') 
# tries=0
# while True:
#    if question.lower() == 'нет' or question.lower() == 'no':
#       print('Программа завершена')
#    else :
#       number_random = random.randint(0,21)
#       number=int(input('Введите число: '))
#       try:
#          if number == number_random:
#             print('Вы угадали число.\nПоздравляем!')
#             break
#          elif number!= number_random:
#             print('Вы не угадали число:(\nПопробуйте снова!!!\nДаю вам подсказку число от 0 до 21')
#             continue 
#          tries+=1
#          print(f'Количество ваших попыток:{tries} ')
#       except ValueError:
#          print('Введите число!!!')







# import random   

# name = input('What is you name ?: ')
# answer = input('Do you want to play? (Y/N) : ')

# secret = random.randint(1,15)
# print(secret)

# attempt = 0

# while True:
#    attempt += 1
#    if attempt > 6:
#       print(f'Sorry, {name}. You have lost.')
#       secret = random.randint(1,15)
#       answer = input('Do you want to try one more time(Y/N): ')
#    if answer.lower().strip() == 'y':
#       try:
#          guess = int(input(f'Guess the number. You have five lives. This your {attempt} attempt.'))
#       except ValueError:
#          print('Sorry, please enter the number')
#          continue

#       if guess == secret:
#          print(f'Congratulations, {name}.')
#          secret = random.randint(1,15)
#          answer = input('Do you want to test your luck one more time ? (Y/N): ')
#          print(secret)
#          attempt = 0
         
         

#    elif answer.lower().strip() == 'n':
#       print(f'Game is over, {name}')
#       break
#    else:
#       print("I don't understand")
#       break



         
