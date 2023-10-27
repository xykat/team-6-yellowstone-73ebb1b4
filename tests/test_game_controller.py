from unittest import TestCase
from levelup.controller import GameController

# THIS IS AN EXAMPLE UNIT TEST. 
# All the unit tests for the Game Controller should go here
# Unit tests for other classes should be in their own .py files (like test_character.py)
class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None
    #Test 1
    def test_create_character_updates_status(self):
        testObj = GameController()
        arbitrary_name = "ARBITRARY"
        testobj.create_character(arbitrary_name)
        self.assertEqual(arbitrary_name, testobj.status.character_name)
        self.assertIsNotNone(testobj.character)
   #Test 2
    def test_start_game_creates_map_and_enters_char(self):
        testObj = GameController()
        arbitrary_name = "ARBITRARY"
        fake_char = FakeCharacter(arbitrary_name)
        testObj.character = fake_char 

        testObj.start_game() #start the game 

        self.assertIsNotNone(testObj.map)
        self.assertTrue(fake_char.is_enter_map_called)
        self.assertTrue(testObj.status.running)
        self.assertEqual(0, testObj.status.move_count)

    #Test 3
    def test_move_calls_char_move(self):
        testobj = GameController()
        arbitrary_name = "ARBITRARY"
        fake_char = FakeCharacter(arbitrary_name)
        testobj.character = fake_char
        arbitrary_direction = Direction.NORTH

        testobj.move(arbitrary_direction)

        self.assertTrue(fake_char.is_move_called)
        self.assertEqual(fake_char.last_move_direction, arbitrary_direction)
