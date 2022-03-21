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
        attribute3 = 'brand'
        attribute4 = 'name'
        attribute5 = 'bullet_points'
        mod_num = '301015010'
        model_number = [mod_num]
        result = '2.69 /sq. ft.'
        brand = 'Pergo'
        name = 'Outlast+ 5.23 in. W Applewood Waterproof Laminate Wood Flooring (13.74 sq. ft./case)'
        bullet_points = '''Golden laminate wood flooring with a soft scraped finish. Waterproof laminate flooring perfect for kitchens and bathrooms. Durable laminate planks offer dent, scratch, and stain protection.'''
        resultArray = self.test_scraper.get_by_internet_number(model_number)
        self.assertEqual(result, resultArray[mod_num][attribute1] + ' ' + resultArray[mod_num][attribute2])
        self.assertEqual(brand, resultArray[mod_num][attribute3])
        self.assertEqual(name, resultArray[mod_num][attribute4])
        self.assertEqual(bullet_points, resultArray[mod_num][attribute5])

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

    def test_get_by_internet_number_3(self):
        attribute1 = 'price'
        attribute2 = 'unit'
        mod_num1 = 'HMDR1000WE'
        mod_num2 = '302264764'
        mod_num3 = '315125493'
        model_numbers = [mod_num1, mod_num2, mod_num3]
        result1 = '349.00'
        result2 = '268.00'
        result3 = '24.98'
        resultArray = self.test_scraper.get_by_internet_number(model_numbers)
        self.assertEqual(result1, (resultArray[mod_num1][attribute1] + ' ' + resultArray[mod_num1][attribute2]).strip())
        self.assertEqual(result2, (resultArray[mod_num2][attribute1] + ' ' + resultArray[mod_num2][attribute2]).strip())
        self.assertEqual(result3, (resultArray[mod_num3][attribute1] + ' ' + resultArray[mod_num3][attribute2]).strip())