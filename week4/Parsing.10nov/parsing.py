"""
День 3. Неделя 4. 10 ноября
Тема: Parcing

Создание виртуального окружения и файла для парсинга:

1. Создать папку для проекта
2. Создать виртуальное окружение, используя команду:

python3 -m venv "название окружения"

3.Активировать окружение в терминале

'source <название окрдуния>'/bin/acticate'

4. Для VSCode:
Ctrl+Shift+P -> Python: Select Interpreter -> Find... в открывашемся окне находим папку с проектом, 
в ней находим окружение и в папке bin выбираем версию Python.

5.Для деактивации используется команда deactivate

6.pip install -r requirements.txt 

Открытие файла:

1. Перед началом работы с парсингом нужно импортировать модули:

requests
lxml
BeautifulSoup

Вводим в VisualStudo  и вводит их импорт


Методы для получения чего-то со страницы:

find() - обращение к одному элементу.
find_all() - обращение к нескольким однотипным элементам.
get() - обращение к атрибутам элементам.
text() - обращение к тексту



1.Как отключить виртуальное окружение ?
ответ:
 deactivate
 exit
 quit
 diactivate

2.Что значит ошибка 404 ?
Error Not Found
Page Not Found
Serer Not Found
Life Not Found


"""
"""
Таким образом можно получить все элементы с span.
"""
# import requests
# from bs4 import BeautifulSoup

# url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
# soup = BeautifulSoup(response, 'lxml')
# quotes = soup.find_all('span', class_='text')
# print(quotes)

"""
Используя цикл for и метод text можно получить только готовый текст
"""


import requests
from bs4 import BeautifulSoup
url = 'https://quotes.toscrape.com/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'lxml')
quotes = soup.find_all('span', class_='text')

for quote in quotes:
    print(quote.text)

"""
Для поиска и вывода всех авторов можно использовать следующий код. 
Работаем по тому же принципу — сперва нужно вручную изучить страницу. 
Можно обратить внимание на то, что каждый автор заключен в тег <small> с классом author. 
Дальше используем функцию find_all() и сохраняем результат в переменной authors. 
Также стоит поменять цикл, чтобы перебирать сразу и цитаты, и авторов.

"""
# import requests
# from bs4 import BeautifulSoup

# url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('span', class_='text')
# authors = soup.find_all('small', class_='author')
# tags = soup.find_all('div', class_='tags')

# for i in range(0, len(quotes)):
#     print(quotes[i].text)
#     print('--' + authors[i].text)
#     tagsforquote = tags[i].find_all('a', class_='tag')
#     for tagforquote in tagsforquote:
#         print(tagforquote.text)
#     print('\n')

"""
Скрапинг с учетом пагинации
Ссылка выше ведет на одну страницу коллекции, включающей на самом деле несколько страниц. 
На это указывает page=1 в адресе. Скрипт Beautiful Soup можно настроить и так, чтобы скрапинг происходил 
на нескольких страницах. Вот код, который будет извлекать данные со всех связанных страниц. Когда все URL захвачены, 
скрипт может выполнять запросы к каждой из них и парсить результаты.

"""
# import requests
# from bs4 import BeautifulSoup

# url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

# for n, i in enumerate(items, start=1):
#     itemName = i.find('h4', class_='card-title').text.strip()
#     itemPrice = i.find('h5').text
#     print(f'{n}:  {itemPrice} за {itemName}')

"""
Этот код можно оптимизировать для более продвинутых читателей:


"""

# import requests
# from bs4 import BeautifulSoup

# url = 'https://scrapingclub.com/exercise/list_basic/'
# params = {'page': 1}
# # задаем число больше номера первой страницы, для старта цикла
# pages = 2
# n = 1


# while params['page'] <= pages:
#     response = requests.get(url, params=params)
#     soup = BeautifulSoup(response.text, 'lxml')
#     items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

#     for n, i in enumerate(items, start=n):
#         itemName = i.find('h4', class_='card-title').text.strip()
#         itemPrice = i.find('h5').text
#         print(f'{n}:  {itemPrice} за {itemName}')

#     # [-2] предпоследнее значение, потому что последнее "Next"
#     last_page_num = int(soup.find_all('a', class_='page-link')[-2].text)
#     pages = last_page_num if pages < last_page_num else pages
#     params['page'] += 1

# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.kinopoisk.ru/lists/top250/'
# r = requests.get(url)

# soup = BeautifulSoup(r.text,'lxml')
# soup.find('div',class_ ="desktop-rating-selection-film-item")

# print(r.text)


"""
Начало разбора

"""
"""
Пример сложного div

<div class =='list'>
    <div class = 'list-inner'>
    <div class =='item'><div>
"""


# from bs4 import BeautifulSoup
# import lxml
# import requests


# MAIN_URL = 'https://www.kivano.kg/mobilnye-telefony'
# PAGE_COUNT = 5

# from save_data import write_to_json,write_to_csv

# def open_page(url):
#     '''Принимает адрес страницы, открывает её и возвращает содержимое страницы'''
#     response = requests.get(url)
#     return response.text

# def analyze_page_content(page_content):
#     '''Анализирует содержимое и подготавливает к получению данных'''
#     soup = BeautifulSoup(page_content,'lxml')
#     return soup

# def get_product_cards(soup):
#     listing = soup.find('div',id="w0")
#     product_cards = listing.find_all('div',class_ = 'item')
#     return product_cards

# def get_data_from_card(card):
#     # image = i just want to go home and have a bit of rest
#     image =card.find('img').get('src')
#     title = card.find('div', class_="listbox_title").find('a').text
#     description = card.find('div',class_ = 'product_text').text.replace('title','').strip()

#     price = card.find('div',class_ = 'listbox_price').find('strong').text

#     return {'image':image,'title':title,'description':description,'price':price}


# def parse():
#     total_product_cards = []

#     '''Итерирует каждую страницу для поиска чего-то и создает новый url с указанием номера страницы'''

#     for page in range(1,PAGE_COUNT + 1):
#         page_url = f'{MAIN_URL}?page={page}'
#         content = open_page(page_url)
#         soup = analyze_page_content(content)
#         product_cards = get_product_cards(soup)
#         total_product_cards.extend(product_cards)
#     data = []
#     for card in total_product_cards:
#         data.append(get_data_from_card(card))

#     write_to_csv(data)


# if __name__ == '__main__':
#     parse()


# TODO: сохранять данные в JSON, CSV
# TODO: использовать user-agent


# import lxml
# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.kivano.kg/mobilnye-telefony'
# response = requests.get(url)
# soup = BeautifulSoup(response,'lxml')
# product_card = soup.find('div',attrs = {'data-key':'69899'})
# a = product_card.find('div', clas_='listbox_price').find('strong').text
# print(a)


"""
Selenium - используется для парсинга сайтов
Библиотека, которая имитирует действия пользователя
"""


# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
# url = 'https://www.eldorado.ru/c/noutbuki/'

# import requests
# from selenium import webdriver
# import selenium
# import time
# from bs4 import BeautifulSoup

# # response = requests.get(url,headers = {'User-Agent': user_agent})


# driver = webdriver.Chrome()
# driver.get(url)
# time.sleep(5)

# html = driver.page_source
# soup = BeautifulSoup(html,'lxml')

# res = soup.find('div',id = 'listing-container')
# listing = res.find('ul')
# product = listing.find('li',{'data-id':'71557427'})
# price = product.find('span',{'data-pc':'offer_price'}).text


# import csv
# def write_to_csv(data):
#     with open('data.csv','w') as file:
#         columns = ['title','description']
#         writer = csv.DictWriter(file, columns)
#         writer.writeheader()
#         for prod in data:
#             writer.writerow()


"""
Task
Таски

1.Нужно получить статус запроса доступа к странице:

https://stackoverflow.com/questions

присвойте результат запроса к переменной source и выведите эту переменную в консоль.

Примерный вывод в консоли:

200 
"""
# import requests
# url = 'https://stackoverflow.com/questions'
# source = requests.get(url).status_code
# print(source)

"""
2.Спарсите тэги h1, p и ссылку с тэга a из веб-страницы:

http://www.example.com/

и выведите результат в консоль в таком виде:

h1:  Example Domain

p:  This domain is for use in illustrative examples in documents. 
You may use this domain in literature without prior coordination or asking for permission.

a:  https://www.iana.org/domains/example
"""
# import requests
# from bs4 import BeautifulSoup
# import lxml

# url = 'http://www.example.com/'
# source = requests.get(url).text
# soup = BeautifulSoup(source,'lxml')
# s = soup.find('a').get('href')
# print(f"h1: {soup.h1.text}\n")
# print(f"p: {soup.p.text}\n")
# print(f"a: \n{s}")

"""
3.Выведите с главной страницы википедии:

https://www.wikipedia.org/

сколько всего статей есть немецком языке.

Вывод в консоль должен быть таким:

Deutsch

2 590 000+ Artikel 
"""
# import requests
# from bs4 import BeautifulSoup
# import lxml

# url = 'https://www.wikipedia.org/'
# source = requests.get(url).text
# soup = BeautifulSoup(source , 'lxml')
# lang = soup.find('a',id ="js-link-box-de").text
# # inf = soup.find_all('a',id='js-link-box-de').get('small').text
# print(lang)

"""
4.Напишите программу которая проверяет имеет ли страница заголовок(тэг h1) или нет.

Для этого напишите функцию getTitle() которая будет принимать url страницы и возвращать заголовок если он есть, 
если же его нет то будет возвращать "Title could not be found"

 print(getTitle('http://www.example.com/'))
Output:

 <h1>Example Domain</h1>
"""

# import requests
# from bs4 import BeautifulSoup
# import lxml

# def getTitle(url):
#     source = requests.get(url).text
#     soup = BeautifulSoup(source,'lxml')
#     title = soup.find('h1')
#     if title:
#         return title
#     else:
#         return "Title could not be found"


# print(getTitle('http://www.example.com/'))


"""
5.На странице:

https://www.makers.kg

есть названия курсов которые предлагает Makers.

Спарсите названия курсов и выведите в консоль:

Founders  
Coding Bootcamp  
Junior Club  
Studio 
"""
# import requests
# from bs4 import BeautifulSoup
# import lxml

# url ='https://www.makers.kg'
# source = requests.get(url).text
# soup = BeautifulSoup(source,'lxml')
# course = soup.find_all('h3',attrs= {'class':"feature-cards-card-info-title"})
# for i in course:
#     print(i.text)

"""
6.Выведите ссылки на все картинки к каждому из курсов:

Founders

Coding Bootcamp

Junior Club

Studio

В HTML страницы путь к картинке указан неполный:

"./assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png" 
вам нужно сделать так, чтобы ссылка была выведена в виде:

https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png  
при переходе по ссылке, она должна быть рабочей и выводить картинку
"""
# import requests
# url = 'https://www.makers.kg/'

# source = requests.get(url).text

# image1 = url+'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png'
# image2 = url+'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a0abffabfd5_5a615b4.png'
# image3 = url+'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a54c1fabfd3_1db079d.png'
# image4 = url+'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a2686fabfd7_79c8646.png'

# print(image1)
# print(image2)
# print(image3)
# print(image4)

""" Этот способ тоже принимает"""

# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.makers.kg/'
# source = requests.get(url).text
# images = ['assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png',
# 'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a0abffabfd5_5a615b4.png',
# 'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a54c1fabfd3_1db079d.png',
# 'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a2686fabfd7_79c8646.png']
# for image in images:
#     image_new = url + image
#     print(image_new)

"""
7.Теперь спарсите и выведите в консоль описание к каждому курсу.

Например:

Обучаем SMM и digital маркетингу на реальном проекте.  Курс охватывает глубокие знания маркетинга и продаж.
"""

# import requests
# from bs4 import BeautifulSoup
# import lxml

# url ='https://www.makers.kg'
# source = requests.get(url).text
# soup = BeautifulSoup(source,'lxml')
# description = soup.find_all('div', attrs = {'class':'feature-cards-card-info-subtitle'})
# for i in description:
#     print(i.text)


"""
8.Создайте функцию get_info() которая принимает url:

https://www.makers.kg

Функция должна записывать заголовок, описание к курсу и ссылку на картинку в список list_ в виде словаря для каждого курса.

Ключами в словарях должны быть строки 'name','description', 'image_link', а значениями сами заголовки, описания и ссылки на картинки(ссылка также должна быть полной и рабочей).

Выведите данный список в консоль:

print(get_info('https://www.makers.kg')) 
Примерный вывод:

[{'name': 'Founders', 'description': 'Обучаем SMM и digital маркетингу на реальном проекте. Курс охватывает глубокие знания маркетинга и продаж.', 'image_link': 'https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png'}, 

{'name': 'Coding Bootcamp', 'description': 'Первый bootcamp по программированию в Кыргызстане. Обучение идет на реальных проектах 5 дней в неделю по 8 часов на протяжении 3 месяцев.', 'image_link': 'https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a0abffabfd5_5a615b4.png'},

{'name': 'Junior Club', 'description': 'Обучение программированию для продвинутых разработчиков. По окончанию лучшие выпускники могут получить работу в компаниях-партнерах', 'image_link': 'https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a54c1fabfd3_1db079d.png'}

{'name': 'Studio', 'description': 'Разработка сайтов, приложений и ПО для бизнеса и организаций. Консультация по внедрению IT решений.', 'image_link': 'https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a2686fabfd7_79c8646.png'}] 
"""


# import requests
# from bs4 import BeautifulSoup
# import lxml
# def get_info(url):
#     source = requests.get(url).text
#     soup = BeautifulSoup(source, "lxml")
#     info = soup.find("div", class_="feature-cards-wrapper")
#     cards = info.find_all("div", class_="feature-cards-card-wrapper")

#     list_ = []
#     for card in cards:
#         name = card.find("a").find("h3").text
#         description = card.find("div", class_="feature-cards-card-info-subtitle").text
#         image_link = url + card.find("img").get("src")[1:]
#         dict_ = {"name": name, "description": description, "image_link": image_link}
#         list_.append(dict_)
#     return list_


# list_ = get_info("https://www.makers.kg")
# print(list_)

"""
9.Напишите код который сохраняет все названия категорий со страницы:

https://enter.kg/

в список category_list.

После, напишите функцию которая имеет два параметра - список категорий - categories и ключевое слово - keyword.

Функция должна производить поиск по ключевому слову в списке заголовков category_list и возвращать список  
заголовков которые содержат данное слово (независимо от регистра).

К примеру:

print(find_category(category_list, 'Ноутбуки')) 
Вывод будет:

['Ноутбуки, Ультрабуки, Гот. решения (1281)', 'Ноутбуки (1235)', 'Ноутбуки, Ультрабуки, Гот. решения(1281)', 'Ноутбуки и ультрабуки'] 
"""
# import requests
# from bs4 import BeautifulSoup
# import lxml

# url = 'https://enter.kg/'
# source = requests.get(url).text
# soup = BeautifulSoup(source, 'lxml')
# list_ =[]
# category = soup.find('div',class_="moduletable")
# category_list = category.find_all('li',class_="VmClose")

# def find_category(category_list,keyword):
#     for categories in category_list:
#         categories = categories.text.strip()
#         if keyword in categories:
#             list_.append(categories)
#     return list_


# print(find_category(category_list, 'память'))
