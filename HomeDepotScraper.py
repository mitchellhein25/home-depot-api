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
            wait = WebDriverWait(self.driver, 15)
            try:
                wait.until(
                    EC.text_to_be_present_in_element((By.XPATH, "//*[@class='price-format__main-price']/span[1]"), ""))
            except:
                wait.until(
                    EC.text_to_be_present_in_element((By.XPATH, "//*[@class='price-detailed__unit-price']/span"), ""))

            nums = self.driver.find_elements_by_class_name("price-detailed__unit-price")
            if len(nums) > 0:
                for value in nums:
                    price = value.find_element_by_xpath("./span")
                    if price.text != '':
                        results[model_num] = {"price": price.text.strip('$')}
                        break

            else:
                nums = self.driver.find_elements_by_class_name("price-format__main-price")
                if len(nums) > 0:
                    for value in nums:
                        if value.text != '':
                            price = self.get_price(value)
                            results[model_num] = {"price": price}
                            break

            units = nums[0].find_elements_by_xpath("./following-sibling::span")
            if len(units) > 0:
                for value in units:
                    if value != '':
                        results[model_num].update({"unit": value.text})
            else:
                results[model_num].update({"unit": ""})

        return results

    def get_price(self, num):
        # dollars = num.find_element_by_xpath("./../../following-sibling::div/div/div/div/div/div/span[2]")
        # cents = num.find_element_by_xpath("./../../following-sibling::div/div/div/div/div/div/span[3]")
        dollars = num.find_element_by_xpath("./span[2]")
        cents = num.find_element_by_xpath("./span[3]")
        return (dollars.text + "." + cents.text).strip('.')

    def quit_driver(self):
        self.driver.quit()

# scraper_test = HomeDepotScraper()
# print(scraper_test.get_by_internet_number(['301015010']))
# # print(scraper_test.get_price_by_model_number('N2316'))
# # print(scraper_test.get_price_by_model_number('740J 15 SMT CP K4'))
# scraper_test.quit_driver()