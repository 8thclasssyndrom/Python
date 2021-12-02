"""
Требования:
1) Есть список слов, из которых будет выбираться рандомом(случайным
образом) одно для угадывания.
2) Сразу же будет печататься длина слова знаками "*"
3) Дальше участнику нужно ввести какую-либо букву и если она есть, то "*"
заменяются на эту букву, а если ее нет, то количество попыток снижается на 1.
Все эти операции будут проходить в цикле while, где условием закрытия
программы будут:

● угадывание слова (победа)
● либо количество попыток == 0.

Например:
● Слово: "Книга"
● Печатается: "*****"
● По мере угадывания появляются буквы: "*нига"
● Также, параллельно принтится количество попыток

"""
# import random
# list_of_words = ['яблоки','апельсин','вишня','виноград','манго','груша','персик','абрикос']
# # random_word = random.choice(list_of_words) 
# random_word = "santa"
# print(random_word)
# print('Давайте начнём игру "Виселица". Вам дан список слов из категории фруктов.')
# random_word_new = len(random_word)*('*')
# print(f'А вот и ваше загаданное слово: {random_word_new}.\nЖелаю удачи')
# count =0
# while True:
#     letter = input('Введите букву: ').lower()
#     count+=1
#     if letter in random_word:
#         letter_new=random_word.index(letter)
#         random_word_new=random_word_new[:letter_new] + letter + random_word_new[(letter_new+1):]
#         print(random_word_new)
#         if random_word_new == random_word:
#             print('Молодец вы выиграли игру!')
#             print(f'Количество ваших попыток: {count}')
#             break
#     elif not letter in random_word:
#         print('Вы не угадали букву, попробуйте снова!!!')
    



# import random
# turns = 10
# print(f"Hello, let's play Hangman. You will have " + str(turns)+'turns')
# print('')
# wordlist = ['puppy','flower','python','space','mammals']
# word = random.choice(wordlist)
# print(word)

# guesses = ''
# while turns>0:
#     spaces = 0

#     for char in word:
#         if char in guesses:
#             print(char)
#         else:
#             print('_')
#             spaces+=1
#         if spaces == 0:
#             print('You won')
#             break
#         guess = ''
#         if len(guess)<1:
#             guess = input('Guess a char: ')[0]
        
#         if guess not in word:
#             turns = 1
#             print('WRONG')
#             print(f'You have {turns} turns left')
#         if turns == 0:
#             print('You lose')


# import requests
# from bs4 import BeautifulSoup
# import lxml




# def get_info(url):
#     dict_new = {}
#     source = requests.get(url).text
#     soup = BeautifulSoup(source,'lxml')
#     names = soup.find_all('h3',attrs= {'class':"feature-cards-card-info-title"})
#     images = ['assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png',
#     'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a0abffabfd5_5a615b4.png',
#     'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a54c1fabfd3_1db079d.png',
#         'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a2686fabfd7_79c8646.png']
#     descriptions = soup.find_all('div', attrs = {'class':'feature-cards-card-info-subtitle'})
#     for name in names:
#         name = name.text
#         dict_new['name'] = name  
#     for description in descriptions:
#         description =description.text
#         dict_new['description'] = description
#         continue
#     for image in images:
#         dict_new['image_link'] = image
#         continue
#     return dict_new


# print(get_info('https://www.makers.kg')) 

    

import requests
from bs4 import BeautifulSoup
import lxml

def get_info(url):
    list_ = []
    dict_new = {}
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    names = soup.find_all('h3',attrs= {'class':"feature-cards-card-info-title"})
    images = ['assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png',
    'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a0abffabfd5_5a615b4.png',
    'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a54c1fabfd3_1db079d.png',
        'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a2686fabfd7_79c8646.png']
    descriptions = soup.find_all('div', attrs = {'class':'feature-cards-card-info-subtitle'})
    for name in names:
        name = name.text
        dict_new['name'] = name  
    for description in descriptions:
        description =description.text
        dict_new['description'] = description
    for image in images:
        image = url +image
        dict_new['image_link'] = image
    return dict_new


print(get_info('https://www.makers.kg')) 