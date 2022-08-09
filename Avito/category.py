# coding=utf-8
from bs4 import BeautifulSoup
import re
from request import get_html
#from categories import categories


def get_list_categories(html):
    print(":get_list_categories")
    """ Функция возвращает список категорий. """
    f = open("out.html","wb")
    f.write(html.encode("utf-8"))
    f.close()
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find('div', attrs={'class': re.compile('^category-with-counters-root-*')}).find_all('div', attrs={'class': re.compile('^category-with-counters-item-*')})
    categories =  { element.find('a').get_text() : element.find('a').get('href').split("/")[2] for element in elements }
    print(categories)
    return categories


def get_dict_categories(list_ip):
    print(":get_dict_categories")
    """ Функция возвращает словарь с категориями. """
    html = get_html('https://www.avito.ru/', list_ip)
    dict_categories = get_list_categories(html)

    # Добавляем в словарь категории. Ключём является название категории на русском языке,
    # значение является название категории на английском языке
    #dict_categories = {category[0]: category[1] for category in categories}
    return dict_categories
