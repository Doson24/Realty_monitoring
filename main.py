import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime
import csv

def init_webdriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Режим без интерфейса
    chrome_options.add_argument('--start-fullscreen')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument('--disable-dev-shm-usage')

    # chrome_options.add_argument("--start-maximized")
    #в режиме headless без user-agent не загружает страницу
    chrome_options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"'')
    # self.driver = webdriver.Chrome('C:\\install\\chromedriver.exe', options=chrome_options)
    driver = webdriver.Chrome('C:\\install\\chromedriver.exe', options=chrome_options)
    return driver

def write_file(data):
    """
    Формат записываемой строки: кол-во в Железногосрке, кол-во в Красноярске, Дата
    """
    a_file = open("Count_realty.csv", "a", newline='')
    writer = csv.writer(a_file, dialect='excel')
    writer.writerow(data)

    a_file.close()

def avito(url, driver):
    driver.get(url)
    driver.set_window_size(1920, 1080)
    count = driver.find_element(By.CLASS_NAME, 'page-title-count-wQ7pG').text.replace(' ', '')
    return count

def domclick(url, driver):
    driver.get(url)
    driver.set_window_size(1920, 1080)
    driver.save_screenshot('screen.png')
    count = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/main/div/div/div[3]/div/div[2]/div[1]').text.replace(' ', '')
    '//*[@id="content"]/div/main'
    return count

def main(urls, cities):
    driver = init_webdriver()
    date = datetime.date.today().strftime('%Y-%m-%d')
    count_list = [avito(url, driver) for url in urls]
    count_list.append(date)
    # domclick('https://krasnoyarsk.domclick.ru/pokupka', driver)

    driver.close()

    write_file(count_list)

    # print(city_realty_count)

if __name__ == '__main__':
    urls = ['https://www.avito.ru/krasnoyarskiy_kray_zheleznogorsk/kvartiry/prodam-ASgBAgICAUSSA8YQ',
            'https://www.avito.ru/krasnoyarsk/kvartiry/prodam-ASgBAgICAUSSA8YQ']
    cities = ['Железногосрк', "Красноярск"]

    while True:
        main(urls, cities)
        print('запись завершена')
        print('sleep')
        time.sleep(3600)
