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
        self.result = {}

    def get_by_internet_number(self, model_numbers):
        for model_num in model_numbers:
            self.send_new_search(model_num)
            self.wait_for_page_load()
            nums = self.get_price(model_num)
            self.get_unit(nums, model_num)
            self.get_brand(model_num)
            self.get_name(model_num)
            self.get_bullet_points(model_num)
        return self.result

    def send_new_search(self, model_num):
        # Enter search item
        search_box = self.driver.find_element_by_class_name("SearchBox__input")
        search_box.clear()
        search_box.send_keys(model_num)
        # Click Search Button
        search_button = self.driver.find_element_by_class_name("SearchBox__button")
        search_button.click()

    def wait_for_page_load(self):
        wait = WebDriverWait(self.driver, 15)
        try:
            wait.until(
                EC.text_to_be_present_in_element((By.XPATH, "//*[@class='price-format__main-price']/span[1]"), ""))
        except:
            wait.until(
                EC.text_to_be_present_in_element((By.XPATH, "//*[@class='price-detailed__unit-price']/span"), ""))

    def get_price(self, model_num):
        '''Gets the price object, and returns the elements selected when getting those (nums)'''
        nums = self.driver.find_elements_by_class_name("price-detailed__unit-price")
        if len(nums) > 0:
            for value in nums:
                price = value.find_element_by_xpath("./span")
                if price.text != '':
                    self.result[model_num] = {"price": price.text.strip('$')}
                    break

        else:
            nums = self.driver.find_elements_by_class_name("price-format__main-price")
            if len(nums) > 0:
                for value in nums:
                    if value.text != '':
                        dollars = value.find_element_by_xpath("./span[2]")
                        cents = value.find_element_by_xpath("./span[3]")
                        self.result[model_num] = {"price": (dollars.text + "." + cents.text).strip('.')}
                        break
        return nums

    def get_unit(self, nums, model_num):
        units = nums[0].find_elements_by_xpath("./following-sibling::span")
        if len(units) > 0:
            for value in units:
                if value != '':
                    self.result[model_num].update({"unit": value.text})
        else:
            self.result[model_num].update({"unit": ""})

    def get_brand(self, model_num):
        brand = self.driver.find_elements_by_class_name("product-details__brand--link")
        if len(brand) > 0:
            for value in brand:
                if value != '':
                    self.result[model_num].update({"brand": value.text})
        else:
            self.result[model_num].update({"brand": ""})

    def get_name(self, model_num):
        name = self.driver.find_elements_by_class_name("product-details__title")
        if len(name) > 0:
            for value in name:
                if value != '':
                    self.result[model_num].update({"name": value.text})
        else:
            self.result[model_num].update({"name": ""})

    def get_bullet_points(self, model_num):
        bullets = self.driver.find_elements_by_class_name("salient-points")
        if len(bullets) > 0:
            for value in bullets:
                if value != '':
                    remove_more_details = value.text.replace("View More Details", "")
                    remove_more_details = remove_more_details.replace("\n", ". ")
                    self.result[model_num].update({"bullet_points": remove_more_details.strip()})
        else:
            self.result[model_num].update({"bullet_points": ""})

    def quit_driver(self):
        self.driver.quit()

# scraper_test = HomeDepotScraper()
# print(scraper_test.get_by_internet_number(['301015010']))
# # print(scraper_test.get_price_by_model_number('N2316'))
# # print(scraper_test.get_price_by_model_number('740J 15 SMT CP K4'))
# scraper_test.quit_driver()