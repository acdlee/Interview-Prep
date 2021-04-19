import unittest
from gcd import gcd

class TestGcb(unittest.TestCase):
	"""
		Test the algorithm gcd(a, b) from 
		gcd.py.
	"""

	#setup for the test cases
	def setUp(self):
		pass

	#ensure that the gcd(412, 260) is
	#indeed 4. 
	def test_oracle_input(self):
		self.assertEqual(gcd(412, 260), 4)

	#test that gcd(a, b) == gcd(b, a)
	def test_inverted_input(self):
		self.assertEqual(gcd(412, 260), gcd(260, 412))

	#test the functionality when passed
	#a real number
	@unittest.skip("Invalid real number input.")
	def test_invalid_input(self):
		self.assertEqual(gcd(12.1, 1), -1)	#this gcd call returns a float

if __name__ == '__main__':
	unittest.main()