from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from SeleniumScraper import SeleniumScraper

class HomeDepotScraper:

    def __init__(self):
        self.url = "https://www.homedepot.com/"
        self.driver = SeleniumScraper().driver
        # Get the url
        self.driver.get(self.url)
        # Wait for page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "headerSearch"))
        )

    def get_by_internet_number(self, model_numbers):
        results = {}
        for model_num in model_numbers:
            # Enter search item
            search_box = self.driver.find_element_by_class_name("SearchBox__input")
            search_box.clear()
            search_box.send_keys(model_num)
            # Click Search Button
            search_button = self.driver.find_element_by_class_name("SearchBox__button")
            search_button.click()
            try:
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//span[@class='price-detailed__unit-price']/span"))
                )
            except:
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//span[@class='price-format__main-price']/span[2]"))
                )
                num = self.driver.find_element_by_class_name("price-format__main-price")
                price = self.get_price(num)
                results[model_num] = {"price": price}
                continue
            num = self.driver.find_element_by_class_name("price-detailed__unit-price")
            price = num.find_element_by_xpath("./span")
            results[model_num] = {"price": price.text.strip('$')}
            unit = num.find_element_by_xpath("./following-sibling::span")
            results[model_num].update({"unit": unit.text})

        return results

    def get_price(self, num):
        # dollars = num.find_element_by_xpath("./../../following-sibling::div/div/div/div/div/div/span[2]")
        # cents = num.find_element_by_xpath("./../../following-sibling::div/div/div/div/div/div/span[3]")
        dollars = num.find_element_by_xpath("./span[2]")
        cents = num.find_element_by_xpath("./span[3]")
        return dollars.text + "." + cents.text

    def quit_driver(self):
        self.driver.quit()

# scraper_test = HomeDepotScraper()
# print(scraper_test.get_by_internet_number(['301015010']))
# # print(scraper_test.get_price_by_model_number('N2316'))
# # print(scraper_test.get_price_by_model_number('740J 15 SMT CP K4'))
# scraper_test.quit_driver()