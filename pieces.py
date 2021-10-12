class piece:
    def __init__(self, position, colour):
        self.position = position
        self.colour = colour
    
    def move_logic(move):
        return True
    
    def __str__(self):
        if self.colour:
            return "O"
        else:
            return "@"

class empty:
    def __init__(self, position, colour):
        self.position = position
    
    def move_logic(move):
        return False
    
    def __str__(self):
        return "."
