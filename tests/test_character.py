from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)
    

    def test_enter_map_sets_map_and_updates_position(self):
        testobj = Character (self.ARBITRARY_NAME)
        stubbed_map = FakeMap()
        testobj.enter_map(stubbed_map)
        self.assertEqual(stubbed_map, testobj.map)
        self.assertEqual(testobj.current_position, stubbed_map.starting_position)

    def test_move_updates_position(self):
        testobj = Character(self.ARBITRARY_NAME)
        stubbed_map = FakeMap()
        testobj.map = stubbed_map

        testobj.move(Direction.EAST)
        self.assertEqual(stubbed_map.STUBBED_X, testobj.current_position.x)
        self.assertEqual(stubbed_map.STUBBED_Y, testobj.current_position.y)