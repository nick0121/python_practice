import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.new_employee = Employee('nick', 'hartford', 60000)


    def test_default_raise(self):
        new_salary = self.new_employee.give_raise()
        self.assertEqual(new_salary, 65000)

    def test_custom_raise(self):
        new_salary = self.new_employee.give_raise(10000)
        self.assertEqual(new_salary, 70000)


if __name__ == '__main__':
    unittest.main()

