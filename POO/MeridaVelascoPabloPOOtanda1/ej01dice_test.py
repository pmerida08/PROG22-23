from ej01dice import Dice
from unittest import TestCase
import unittest

class MyTestCase(unittest.TestCase):

    def set_up(self):
        self.caras = Dice()

    def test_side(self):
        self.assertEqual(self.caras.face, 6)

    def test_roll(self):
        self.assertLessEqual(self.caras.try_it(), 6)
        self.assertGreaterEqual(self.caras.try_it(), 1)

    def test_dados(self):
        self.assertLessEqual(self.caras.try_it(), 6)
        self.assertGreaterEqual(self.caras.try_it(), 1)

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()