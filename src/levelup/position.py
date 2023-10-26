class Position ():

    x = -100
    y = -100

    def __init__(self, x: int, y: int):
        self.x = x # X-coordinates 
        self.y = y # Y-coordinates 

    def __eq__(self, obj):
        if self.x == obj.x and self.y == obj.y:
            return True
        else:
            return False



    
