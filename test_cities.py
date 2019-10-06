import unittest
from city_function import get_formatted_city


class CittTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')


    def test_city_country_pop(self):
        formatted_city = get_formatted_city('santiago', 'chile', 20000)
        self.assertEqual(formatted_city, 'Santiago, Chile And The Population Is 20000')

if __name__ == '__main__':
    unittest.main()

