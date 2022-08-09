# coding=utf-8
import undetected_chromedriver as uc
from requests import get
from requests.exceptions import ProxyError, ReadTimeout, SSLError, ConnectionError
from seleniumwire import webdriver
#from selenium import webdriver
from selenium_stealth import stealth
import os
from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.chrome.options import Options
import time
CHROMEDRIVER_EXE_PATH = 'chromedriver.exe'


def get_html(url, list_ip):
    print(":get_html")
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    for ip in list_ip:
        try:
            html = response(url, ip, headers)
            if html is not None: return html
        except (ProxyError, ConnectionError, ReadTimeout, SSLError):
            list_ip.pop(list_ip.index(ip))
            continue


def response(url, ip, headers):
    print(":response")
    #r = get(url, proxies={"https": ip}, headers=headers, timeout=7)
    swoptions = {
    'proxy': {
        'http': 'http://'+ip,
        'https': 'https://'+ip,
        'no_proxy': 'localhost,127.0.0.1'
        }
    }
    if "PROGRAMFILES(X86)" not in os.environ:
        os.environ["PROGRAMFILES(X86)"] = ""
    #options = uc.ChromeOptions()
    #prefs = {"profile.managed_default_content_settings.images": 2}
    #options.add_experimental_option("prefs", prefs)
    #driver = webdriver.Chrome(executable_path=CHROMEDRIVER_EXE_PATH,options=options)
    #uc.install(executable_path=CHROMEDRIVER_EXE_PATH,)
    #opts.add_argument(f'--proxy-server=socks5://127.0.0.1:9050')
    driver = uc.Chrome()#options=options)
    #driver.get('https://distilnetworks.com')
    #driver = webdriver.Chrome(executable_path=CHROMEDRIVER_EXE_PATH,seleniumwire_options=swoptions,options=options)

    # stealth(
    # driver,
    # user_agent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
    # languages = ["en-US", "en"],
    # vendor = "Google Inc.",
    # platform = "Win32",
    # webgl_vendor = "Intel Inc.",
    # renderer = "Intel Iris OpenGL Engine",
    # fix_hairline = False,
    # run_on_insecure_origins = False,
    # )
    #
    #driver = webdriver.Chrome(executable_path=CHROMEDRIVER_EXE_PATH,seleniumwire_options=swoptions,options=options)
    #r =
    #url="https://wwww.ya.ru"
    driver.get(url)
    time.sleep(30)
    if len(driver.page_source) > 80000:
        return driver.page_source


def for_metro(url, list_ip, headers):
    print(":for_metro")
    for ip in list_ip:
        try:
            r = get(url, proxies={"https": ip}, headers=headers, timeout=5)
            return r.text
        except (ProxyError, ConnectionError, ReadTimeout, SSLError):
            list_ip.pop(list_ip.index(ip))
            continue
