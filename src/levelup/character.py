class Character:
    default_name = None

    def __init__(self, name, default_name):
        self.naem = name
        Chracter.default_name = default_name
        self.position = None 
    
    def get_name(self):
        return self.name
    
    def get_total_positions(self):
        return self.position
    
    def enter_map(self, game_map):
        return game_map
    
    def move(self, direction):
        return direction

        
    