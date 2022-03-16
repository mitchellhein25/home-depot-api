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

    def get_by_model_number(self, model_numbers):
        results = {}
        for model_num in model_numbers:
            # Enter search item
            search_box = self.driver.find_element_by_class_name("SearchBox__input")
            search_box.clear()
            # model_search = ""
            # for model_num in model_numbers:
            #     if " " in model_num:
            #         continue
            #     model_search += model_num + "|"
            # model_search = model_search.strip("|")
            search_box.send_keys(model_num)
            # Click Search Button
            search_button = self.driver.find_element_by_class_name("SearchBox__button")
            search_button.click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-format__main-price"))
            )
            # Get all model numbers on page
            model_number_elements = self.driver.find_elements_by_class_name("product-identifier__model")
            for model_num in model_numbers:
                for num in model_number_elements:
                    # print(num.text.replace("Model# ", ""))
                    if num.text.replace("Model# ", "") == model_num:
                        price = self.get_price(num)
                        results[model_num] = {"price": price}
                        break
            # for model_num in model_numbers:
            #     if model_num not in results.keys():
            #         results.update(self.get_price_by_model_number([model_num]))
        return results

    def get_price(self, num):
        try:
            dollars = num.find_element_by_xpath("./../../following-sibling::div/div/div/div/div/div/span[2]")
            cents = num.find_element_by_xpath("./../../following-sibling::div/div/div/div/div/div/span[3]")
        except:
            dollars = num.find_element_by_xpath("./../../following-sibling::div/div/div/div/div/div/div/span[2]")
            cents = num.find_element_by_xpath("./../../following-sibling::div/div/div/div/div/div/div/span[3]")
        return dollars.text + "." + cents.text

    def quit_driver(self):
        self.driver.quit()

# scraper_test = HomeDepotScraper()
# print(scraper_test.get_by_model_number(['LF000885', 'N2316', '740J 15 SMT CP K4']))
# # print(scraper_test.get_price_by_model_number('N2316'))
# # print(scraper_test.get_price_by_model_number('740J 15 SMT CP K4'))
# scraper_test.quit_driver()