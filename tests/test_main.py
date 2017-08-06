import unittest

from tests.utilities.main import Main


class MainTest(unittest.TestCase):
	def test_creation(self):
		main = Main()
		self.assertIsNotNone(main.get_server())
		self.assertIsNotNone(main.get_codecast_gateway())