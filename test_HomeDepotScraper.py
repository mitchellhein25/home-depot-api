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
        attribute3 = 'brand'
        attribute4 = 'name'
        attribute5 = 'bullet_points'
        mod_num1 = '100676582'
        mod_num2 = '309567384'
        mod_num3 = '308301772'
        model_numbers = [mod_num1, mod_num2, mod_num3]
        result1 = '99.00'
        brand1 = 'Glacier Bay'
        name1 = '2-piece 1.1 GPF/1.6 GPF High Efficiency Dual Flush Complete Elongated Toilet in White, Seat Included'
        bullet_points1 = 'Delivers powerful 1.1 or 1.6 GPF for efficient flush performance. QuickConnect Easy Installation System. Includes toilet seat, wax ring and floor mounting bolt set.'
        result2 = '34.97'
        brand2 = 'Kwikset'
        name2 = 'Satin Nickel Single Cylinder Deadbolt featuring SmartKey Security with Microban Antimicrobial Technology'
        bullet_points2 = 'Single cylinder operates by key outside & thumb turn inside. Fits door thickness of 1-3/8 in. to 1-3/4 in. SmartKey Security re-keying allows you to re-key lock yourself.'
        result3 = '879.55'
        brand3 = 'Krosswood Doors'
        name3 = '36 in. x 80 in. Craftsman 2-Panel 6-Lite Clear Low-E Knotty Alder Unfinished Wood Front Door Slab'
        bullet_points3 = 'Slab size 36 in. x 80 in. Must be finished on all six sides. Must have adequate overhang, see warranty for details.'
        resultArray = self.test_scraper.get_by_internet_number(model_numbers)
        self.assertEqual(result1, (resultArray[mod_num1][attribute1] + ' ' + resultArray[mod_num1][attribute2]).strip())
        self.assertEqual(brand1, resultArray[mod_num1][attribute3])
        self.assertEqual(name1, resultArray[mod_num1][attribute4])
        self.assertEqual(bullet_points1, resultArray[mod_num1][attribute5])
        self.assertEqual(result2, (resultArray[mod_num2][attribute1] + ' ' + resultArray[mod_num2][attribute2]).strip())
        self.assertEqual(brand2, resultArray[mod_num2][attribute3])
        self.assertEqual(name2, resultArray[mod_num2][attribute4])
        self.assertEqual(bullet_points2, resultArray[mod_num2][attribute5])
        self.assertEqual(result3, (resultArray[mod_num3][attribute1] + ' ' + resultArray[mod_num3][attribute2]).strip())
        self.assertEqual(brand3, resultArray[mod_num3][attribute3])
        self.assertEqual(name3, resultArray[mod_num3][attribute4])
        self.assertEqual(bullet_points3, resultArray[mod_num3][attribute5])

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