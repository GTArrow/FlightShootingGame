print('Start Testing\n***************************')
import unittest as ut
print("import unittest successfully!")
from Enemy import *
print('import Enemy successfully!')

class TestBoss(ut.TestCase):
	def setUp(self):
		self.enemy=Enemy(0, 0, 5)

	def testMove(self):
		self.enemy.move()
		self.assertEqual(self.enemy.x, 0)
		self.assertEqual(self.enemy.y, 5)

	def testReset(self):
		self.enemy.reset()
		self.assertTrue(0<=self.enemy.x<=115)
		self.assertEqual(self.enemy.y, -9)

	def testNotCollidable(self):
		self.enemy.not_collidable()
		self.assertEqual(self.enemy.width, -1000)
		self.assertEqual(self.enemy.height, -1000)

if __name__=='__main__':
	ut.main()