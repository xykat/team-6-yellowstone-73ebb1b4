import logging
from dataclasses import dataclass
from enum import Enum
from levelup.character import Character


DEFAULT_CHARACTER_NAME = "Character"

@dataclass

class GameStatus:
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: tuple = (3,3)
    move_count: int = 0

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:

    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        pass

    # Pre-implemented to demonstrate ATDD
    # TODO: Update this if it does not match your design (hint - it doesnt)
    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.status.character_name = character_name
        else:
            self.status.character_name = DEFAULT_CHARACTER_NAME

    def move(self, direction: Direction) -> None:
        # TODO: Implement move - should call something on another class
        # TODO: Should probably also update the game results
        self.character.move(direction)
        self.status.current_position = (self.character.current_position.x, self.character.current_position.y)
        self.status.move_count= self.status.move_count + 1

    def set_character_position(self, xycoordinates: tuple) -> None:
        # TODO: IMPLEMENT THIS TO SET CHARACTERS CURRENT POSITION -- exists to be testable
        pass

    def set_current_move_count(self, move_count: int) -> None:
        # TODO: IMPLEMENT THIS TO SET CURRENT MOVE COUNT -- exists to be testable

        pass
        # +=
    def get_total_positions(self) -> int:
        # TODO: IMPLEMENT THIS TO GET THE TOTAL POSITIONS FROM THE MAP - - exists to be
        # testable
        return -10

    
#     def __init__(self):
#         self.name = None  # Initialize the name attribute
    
#     def get_user_input(self, prompt):
#         user_input = input(prompt)
#         return user_input

# # Create an instance of the class
# input_handler = Character()

# # Show to the user and collect the data
# user_text = input_handler.get_user_input("Enter the name of your character: ")
# print("You entered: ", user_text)