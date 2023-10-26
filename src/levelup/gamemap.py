class gamemap:

    def getPositions(self):
        print("This is getPositions method.")

    def calculateValidatePositions(self):
        GRID_SIZE = 10
    while True:
        try:
            # Get user input for the X and Y coordinates
            x = int(input(f"Enter the X coordinate (0 to {GRID_SIZE-1}): "))
            y = int(input(f"Enter the Y coordinate (0 to {GRID_SIZE-1}): "))

            if direction:'NORTH'
            y +=1
            if 0 <= y < GRID_SIZE:
                return y
            else: y -=1

            # Check if the coordinates are within the grid boundaries
            if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                return x, y
            else:
                print("Coordinates are out of bounds. Please try again.")
        except ValueError:
            print("Invalid input. Please enter integers for coordinates.")
    

    def get_position(self):
        print("This is get_position method.")