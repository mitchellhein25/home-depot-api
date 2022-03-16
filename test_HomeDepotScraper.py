from unittest import TestCase
from HomeDepotScraper import *


class TestHomeDepotScraper(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_scraper = HomeDepotScraper()

    @classmethod
    def tearDownClass(cls):
        cls.test_scraper.quit_driver()

    def test_get_by_model_number_1(self):
        model_number = ['LF000885']
        result = '2.69'
        self.assertEqual(result, self.test_scraper.get_by_model_number(model_number)['LF000885']['price'])

    def test_get_by_model_number_2(self):
        model_number = ['LF000885', 'N2316', '740J 15 SMT CP K4']
        result = '2.69'
        self.assertEqual(result, self.test_scraper.get_by_model_number(model_number)['LF000885']['price'])
