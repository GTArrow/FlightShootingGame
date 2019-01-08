print('Start Testing\n***************************')
import unittest as ut
print("import unittest successfully!")
from Bullet import *
print('import Bullet successfully!')

class TestBoss(ut.TestCase):
	def setUp(self):
		self.Bullet=Bullet(0, 0, 50, 0, 2, 2, 2)

	def testMove(self):
		self.Bullet.move()
		self.assertEqual(self.Bullet.x, 0)
		self.assertEqual(self.Bullet.y, 2)

	def testReset(self):
		self.Bullet.reset(2, 3)
		self.assertEqual(self.Bullet.x, 2)
		self.assertEqual(self.Bullet.y, 3)

if __name__=='__main__':
	ut.main()