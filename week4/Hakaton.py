import requests
from bs4 import BeautifulSoup
import lxml
import csv

def get_info():
    with open('data.csv','w') as file:
        columns = ['Название','Цена', 'Картинка','Описание']
        writer = csv.DictWriter(file, columns)
        writer.writeheader()

        for i in range(15):
            url = 'https://www.mashina.kg/search/opel/all/?currency=2&sort_by=upped_at%20desc&time_created=all'+ f'&page={i}'
            response = requests.get(url).text
            soup = BeautifulSoup(response,'lxml')
            catalog = soup.find_all('div', attrs = {'class':'list-item'})
            catalog = list(filter(lambda x: x.find('a') is not None,catalog))
            
            for item in catalog:
                name = item.find('h2',class_ = 'name').text
                name = ' '.join(name.split())

                price = item.find('p',class_ = 'price').text.split()
                price = ' '.join(price)
                try:
                    images = item.find('img',class_="lazy-image").get('data-src')
                except:
                    images =''

                descr =item.find('div',class_="item-info-wrapper").text
                description = ' '.join(descr.split())
                
                writer.writerow({'Название': name,'Цена':price,'Картинка':images,'Описание':description})


get_info()
        
        
        




