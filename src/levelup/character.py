from levelup.position import Position
from levelup.direction import Direction
<<<<<<< HEAD
from levelup.gamemap import GameMap
=======
from levelup.map import Map
>>>>>>> 381e970 (changedPosition2)
class Character:
    name = ""
    current_position : Position = Position(-100, -100)
    map : Map = Map ()
    
    def __init__(self, name):
        self.name = character_name
    
    def move(self, direction:Position) -> None:
        self.current_position = self.current_position =self.map.calculate_new_position(
            self.current_position, direction)
    
    def enter_map(self, map : Map): 
        self.map = map 
        self.current_position = self.map.starting_position
