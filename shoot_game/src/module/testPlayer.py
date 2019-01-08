import unittest as ut
print("import unittest successfully!")
from Player import *
print('import Player successfully!')

class TestPlayer(ut.TestCase):
	def setUp(self):
		self.player=Player(0, 0, 300)

	def testReset(self):
		self.player.reset(450)
		self.assertEqual(self.player.life, 450)

if __name__=='__main__':
	ut.main()