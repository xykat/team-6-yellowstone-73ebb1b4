class GameMap:

    def getPositions(self):
        print("This is getPositions method.")

    def calculateValidatePositions(self):
    
        while True:
            try:
            # Get user input for the X and Y coordinates
                x = int(input(f"Enter the X coordinate (0 to {GRID_SIZE-1}): "))
                y = int(input(f"Enter the Y coordinate (0 to {GRID_SIZE-1}): "))

                if direction:'NORTH'
                y +=1
                if 0 <= y < 10:
                    y=y
                else: y -=1

                if direction:'SOUTH'
                y -=1
                if 0 <= y < 10:
                    y=y
                else: y +=1
                
                if direction:'EAST'
                x -=1
                if 0 <= x < 10:
                    x=x
                else: x +=1

                if direction:'WEST'
                x ==1
                if 0 <= x < 10:
                    x=x
                else: x -=1

            
            except ValueError:
                    print("Invalid input. Please enter integers for coordinates.")