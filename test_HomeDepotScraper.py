from unittest import TestCase
from HomeDepotScraper import *


class TestHomeDepotScraper(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_scraper = HomeDepotScraper()

    @classmethod
    def tearDownClass(cls):
        cls.test_scraper.quit_driver()

    def test_get_by_internet_number_1(self):
        attribute1 = 'price'
        attribute2 = 'unit'
        mod_num = '301015010'
        model_number = [mod_num]
        result = '2.69 /sq. ft.'
        resultArray = self.test_scraper.get_by_internet_number(model_number)
        self.assertEqual(result, resultArray[mod_num][attribute1] + ' ' + resultArray[mod_num][attribute2])

    def test_get_by_internet_number_2(self):
        attribute1 = 'price'
        attribute2 = 'unit'
        mod_num1 = '100676582'
        mod_num2 = '309567384'
        mod_num3 = '308301772'
        model_numbers = [mod_num1, mod_num2, mod_num3]
        result1 = '99.00'
        result2 = '34.97'
        result3 = '879.55'
        resultArray = self.test_scraper.get_by_internet_number(model_numbers)
        self.assertEqual(result1, (resultArray[mod_num1][attribute1] + ' ' + resultArray[mod_num1][attribute2]).strip())
        self.assertEqual(result2, (resultArray[mod_num2][attribute1] + ' ' + resultArray[mod_num2][attribute2]).strip())
        self.assertEqual(result3, (resultArray[mod_num3][attribute1] + ' ' + resultArray[mod_num3][attribute2]).strip())

    def test_get_by_model_number_3(self):
        attribute = 'price'
        mod_num = 'HMDR1000WE'
        model_number = [mod_num]
        result = '443.46'
        self.assertEqual(result, self.test_scraper.get_by_model_number(model_number)[mod_num][attribute])
