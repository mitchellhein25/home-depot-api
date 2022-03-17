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

    def test_get_by_model_number_2(self):
        attribute = 'price'
        mod_num1 = 'LF000885'
        mod_num2 = 'N2316'
        mod_num3 = '740J 15 SMT CP K4'
        model_number = [mod_num1, mod_num2, mod_num3]
        result1 = '2.69'
        result2 = '99.00'
        result3 = '28.97'
        resultArray = self.test_scraper.get_by_model_number(model_number)
        self.assertEqual(result1, resultArray[mod_num1][attribute])
        self.assertEqual(result2, resultArray[mod_num2][attribute])
        self.assertEqual(result3, resultArray[mod_num3][attribute])

    def test_get_by_model_number_3(self):
        attribute = 'price'
        mod_num = 'HMDR1000WE'
        model_number = [mod_num]
        result = '443.46'
        self.assertEqual(result, self.test_scraper.get_by_model_number(model_number)[mod_num][attribute])
