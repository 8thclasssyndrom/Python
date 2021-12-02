from _typeshed import NoneType
import requests
import lxml
from bs4 import BeautifulSoup, element
import csv


url = 'https://www.mashina.kg/search/opel/all/?currency=2&sort_by=upped_at%20desc&time_created=all'
source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')
table = soup.find('div',class_ = 'table-view-list')
catalog = table.find_all('div', attrs={'class': 'list-item'})


def get_elements(catalog):
    for element in catalog:
        if element is NoneType:
            pass
        else:
            elements = element.find('a')
            name = elements.find('h3',class_ = 'name').text
            print(name)
