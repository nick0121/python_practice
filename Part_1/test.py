import unittest
from testing import formated_name


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = formated_name('janis', 'joplin', 'marie')
        self.assertEqual(formatted_name, 'Janis Marie Joplin')

if __name__ == '__main__':
    unittest.main()



