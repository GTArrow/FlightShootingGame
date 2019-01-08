print('Start Testing\n***************************')
import unittest as ut
print("import unittest successfully!")
from Gift import *
print('import Gift successfully!')

class TestBoss(ut.TestCase):
	def setUp(self):
		self.gift=Gift(0, 0)

	def testMove(self):
		self.gift.move(1500)
		self.assertEqual(self.gift.x, 0)
		self.assertTrue(2<=self.gift.y<=4)
		self.gift.y=245
		self.gift.move(1500)
		self.assertTrue(0<=self.gift.x<=168)
		self.assertEqual(self.gift.y, 0)

	def testReset(self):
		self.gift.reset()
		self.assertEqual(self.gift.x, -7)
		self.assertEqual(self.gift.y, -7)

if __name__=='__main__':
	ut.main()