from unittest import TestCase
from levelup.controller import gamemap

# THIS IS AN EXAMPLE UNIT TEST. 
# All the unit tests for the Game Map should go here
# Unit tests for other classes should be in their own .py files (like test_character.py)
class TestGameMap(TestCase):
    def test_init(self):
        testObj = gamemap()
        assert testObj.status != None