from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumScraper:

    def __init__(self):
        DRIVER_PATH = 'C:\chromedriver\chromedriver.exe'

        # ChromeOptions = webdriver.ChromeOptions()
        # ChromeOptions.add_argument('--disable-browser-side-navigation')

        options = Options()
        options.headless = True
        options.add_argument('--blink-settings=imagesEnabled=false')
        options.add_argument("--window-size=1920,1200")
        # chrome_options = ChromeOptions

        self.driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
