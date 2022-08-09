# coding=utf-8
from district import get_dict_district
from city import cities
from links import links_to_product_pages
from goods import get_goods
from category import get_dict_categories
from threads import start_threads
from subcategories import get_subcategories
from metro import get_metro
from proxies import get_proxy


def main():
    list_ip = get_proxy()

    city = cities["Ижевск"]  # Вместо "Ижевск", введите нужный Вам город

    dict_categories = get_dict_categories(list_ip)
    print(dict_categories)

    category = dict_categories["Личные вещи"]  # Вместо "Велосипеды", ввидите нужную Вам категорию

    direction = get_dict_district(city, list_ip)  # Если в city метро, то direction = get_metro(city, proxy_list)
    print(direction)

    #district_or_metro = 'district'  # 'district' или 'metro'

    subcategories = get_subcategories(category, list_ip)
    print(subcategories)

    links = links_to_product_pages(city, category, subcategories, direction['Октябрьский'], list_ip, district_or_metro)
    print(links)

    list_goods = get_goods(links, list_ip)
    print(list_goods)

    number_of_threads = 1  # Количество потоков

    numbers = start_threads(list_goods, number_of_threads)


if __name__ == '__main__':
    main()
