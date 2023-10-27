from unittest import TestCase
from levelup.position import Position


class TestPositionInitWithXY(TestCase):
    def test_init(self):
        x = 2
        y = 4
        testobj = Position(x, y)
        self.assertEqual(x, testobj.x)
        self.assertEqual(y, testobj.y)
