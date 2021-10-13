# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               Reagan Wall
#               Logan Winship
#               Tyler Mayou & Zack Abbott
# Section:      472/572
# Assignment:   Lab 7A Activity 1
# Date:         October 13, 2021

#class definition
# used for an actual piece
class piece:
    def __init__(self, position, colour):
        self.position = position
        self.colour = colour
    
    def move_logic(self):
        return True

# used to output spaces as a "O" or a "@"
# overrides the inherent str() method
    def __str__(self):
        if self.colour:
            return "O"
        else:
            return "@"

# used for an empty spot
class empty:
    def __init__(self, position):
        self.position = position
    
    def move_logic(self):
        return False

# used to output blank spaces as a "."
# overrides the inherent str() method
    def __str__(self):
        return "."
