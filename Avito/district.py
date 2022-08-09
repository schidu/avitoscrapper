# coding=utf-8
from bs4 import BeautifulSoup
from request import get_html


def get_data(html):
    print(":get_data")
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find("optgroup", label="район").find_all("option")
    # Ключём является название района на русском, значение является id района.
    data = {element.text: element.get("value") for element in elements}
    #[{"id":208,"name":"Адлерский","altName":"р-н Адлерский"},{"id":209,"name":"Лазаревский","altName":"р-н Лазаревский"},{"id":210,"name":"Хостинский","altName":"р-н Хостинский"},{"id":211,"name":"Центральный","altName":"р-н Центральный"}]
    return data


def get_dict_district(city, list_ip):
    print(":get_dict_district")
    """ Функция возвращает словарь с районами city. """
    #locationId=634450
    url = "https://www.avito.ru/web/1/locations/districts?locationId={}".format(city.locationId)
    html = get_html(url, list_ip)
    district = get_data(html)
    return district
