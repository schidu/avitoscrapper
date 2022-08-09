# coding=utf-8
import requests
from bs4 import BeautifulSoup

list_ip = []


def get_html(url):
    print("get_html")
    r = requests.get(url)
    return r.text


def get_list_ip(html):
    print(":get_list_ip")
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find("tbody").find_all("tr")
    for element in elements:
        ip = element.find_all("td")[0].text
        port = element.find_all("td")[1].text
        country = element.find_all("td")[2].text
        if country=='RU':
            proxy = "{}:{}".format(ip, port)
            list_ip.append(proxy)
    return list_ip


def get_proxy():
    print(":get_proxy")
    """ Функция возвращает список https прокси. """
    url = "https://www.sslproxies.org/"
    html = get_html(url)
    list_ip = get_list_ip(html)
    print(list_ip)
    return list_ip




