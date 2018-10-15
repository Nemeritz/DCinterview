import unittest
import CLoader


class AddTest(unittest.TestCase):
	def test_addition(self):
		module = CLoader.load('example')
		self.assertEqual(module.add(1, 2), 1 + 2)

