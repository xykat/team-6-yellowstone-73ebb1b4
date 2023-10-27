from levelup.position import Position
from levelup.direction import Direction
from levelup.gamemap import GameMap
class Character:
    name = ""
    current_position : Poistion = Poistion(-100, -100)
    map : Map = Map ()
    
    def __init__(self, name):
        self.name = character_name
    
    def move(self, direction:Poistion) -> None:
        self.current_position = self.current_position =self.map.calculate_new_position(
            self.current_position, direction)
    
    def enter_map(self, map : Map): 
        self.map = map 
        self.current_position = self.map.starting_position
