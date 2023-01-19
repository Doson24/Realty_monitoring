from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# pip install webdriver-manager

def init_webdriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Режим без интерфейса
    # chrome_options.add_argument('--start-fullscreen')
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument("download.default_directory=C:/install") # Возможно не работает
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "C:\\Users\\user\\Desktop\\Projects\\Restate.ru\\data",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })
    #в режиме headless без user-agent не загружает страницу
    chrome_options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"'')
    # self.driver = webdriver.Chrome('C:\\install\\chromedriver.exe', options=chrome_options)
    # driver = webdriver.Chrome('./driver/chromedriver.exe', options=chrome_options)

    # Добавить режим без изображений

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver