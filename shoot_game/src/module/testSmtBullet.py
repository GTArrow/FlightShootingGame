print('Start Testing\n***************************')
import unittest as ut
print("import unittest successfully!")
from Smart_Bullet import *
print('import Smart Bullet successfully!')
from Player import *
print('import Player successfully!')

class TestBoss(ut.TestCase):
	def setUp(self):
		self.smtBullet=Smart_Bullet(0, 0, 50, 5, 2, 2)
		self.player=Player(10, 10, 300)

	def testMove(self):
		self.smtBullet.move()
		self.assertEqual(self.smtBullet.x, 175)
		self.assertEqual(self.smtBullet.y, 0)

	def testReset(self):
		self.smtBullet.reset(2, 3)
		self.assertEqual(self.smtBullet.x, 2)
		self.assertEqual(self.smtBullet.y, 3)
		self.assertEqual(self.smtBullet.state, 1)

	def testAim(self):
		self.smtBullet.reset(0, 0)
		self.smtBullet.aim(self.player)
		self.assertTrue(3.0<self.smtBullet.speed_x<3.5)
		self.assertTrue(3.0<self.smtBullet.speed_y<3.5)

if __name__=='__main__':
	ut.main()