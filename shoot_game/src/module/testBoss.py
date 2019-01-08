print('Start Testing\n***************************')
import unittest as ut
print("import unittest successfully!")
from Boss import *
print('import Boss successfully!')

class TestBoss(ut.TestCase):
	def setUp(self):
		self.boss=Boss(1000, 60, 60)

	def testShow_up(self):
		self.boss.show_up()
		self.assertEqual(self.boss.state, 1)
		self.assertEqual(self.boss.x, 85)
		self.assertEqual(self.boss.y, 30)

	def testMove(self):
		self.boss.show_up()
		self.boss.move()
		self.assertEqual(self.boss.x, 86)

	def testReset(self):
		self.boss.reset(1000)
		self.assertEqual(self.boss.state, 0)
		self.assertEqual(self.boss.life, 1000)

if __name__=='__main__':
	ut.main()