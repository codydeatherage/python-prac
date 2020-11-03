import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
	def setUp(self):
		"""Create an employee instance for testing"""
		self.my_employee = Employee('yDoasd', 'oonganewe', 10000)

	def test_give_default_raise(self):
		self.my_employee.give_raise()
		self.assertEqual(self.my_employee.salary, 15000)

	def test_give_custom_raise(self):
		self.my_employee.give_raise(1000)
		self.assertEqual(self.my_employee.salary, 11000)

if __name__ == '__main__':
	unittest.main()