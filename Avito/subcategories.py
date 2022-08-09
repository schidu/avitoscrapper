# coding=utf-8
from bs4 import BeautifulSoup
from request import get_html


def get_data(html, category):
    print("get_data")
    links = []
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find("ul", class_="rubricator-submenu-18HMk").find_all("li")
    for element in elements:
        href_category = element.find("a").get('href').split('/')[2].split('?')[0]
        if href_category == category:
                href = element.find("a").get('href').split('/')[3].split('?')[0]
                links.append(href)
    links.remove(links[0])
    return links


def get_subcategories(category, list_ip):
    print("get_subcategories")
    """ Функция возвращает список подкатегорий category. """
    url = "https://avito.ru/rossiya/{}".format(category)
    html = get_html(url, list_ip)
    subcategories = get_data(html, category)
    return subcategories
