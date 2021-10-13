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

#imports
from pieces import piece, empty

#class definition
class board():
    def __init__(self):
        #the board itself
        self.board = [
            [
                piece([0,0],True), empty([]),
                piece([0,3],True), empty([]),
                piece([0,5],True), empty([]),
                piece([0,7],True), empty([]),
            ],
            [
                empty([]),
                piece([0,0],True), empty([]),
                piece([0,3],True), empty([]),
                piece([0,5],True), empty([]),
                piece([0,7],True),
            ],
            [
                piece([0,0],True), empty([]),
                piece([0,3],True), empty([]),
                piece([0,5],True), empty([]),
                piece([0,7],True), empty([]),
            ],
            [
                empty([]), empty([]),
                empty([]), empty([]),
                empty([]), empty([]),
                empty([]), empty([]),
            ],
            [
                empty([]), empty([]),
                empty([]), empty([]),
                empty([]), empty([]),
                empty([]), empty([]),
            ],
            [
                empty([]),
                piece([0,0],False), empty([]),
                piece([0,3],False), empty([]),
                piece([0,5],False), empty([]),
                piece([0,7],False),
            ],
            [
                piece([0,0],False), empty([]),
                piece([0,3],False), empty([]),
                piece([0,5],False), empty([]),
                piece([0,7],False), empty([]),
            ],
            [
                empty([]),
                piece([0,0],False), empty([]),
                piece([0,3],False), empty([]),
                piece([0,5],False), empty([]),
                piece([0,7],False),
            ],
        ]

# This is all the logic and preprocessing for every move
# Changes single string into 4 integers so the computer can use them
    def move(self, string):
        loc1 = string[0:3]
        loc2 = string[7:]
        if (int(loc2[0]) % 2) != (int(loc2[2]) % 2):
            print(int(loc2[0]) % 2,int(loc2[2]) % 2)
            print("Move is invalid- you cannot move to that space.")
            return
        print(loc1, loc2)
        if self.board[int(loc1[0])][int(loc1[2])].move_logic():
            self.board[int(loc2[0])][int(loc2[2])] = self.board[int(loc1[0])][int(loc1[2])]
            self.board[int(loc1[0])][int(loc1[2])] = empty([])
        else:
            print("There is not a piece at that location.")
        return

# used to output the board itself
# overrides the predefined str() method
    def __str__(self):
        string = ""
        for list in self.board:
            for item in list:
                string += str(item) + " "
            string += "\n"
        return string
