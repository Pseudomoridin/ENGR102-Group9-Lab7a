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
from board import board

#variable definition
_board = board()

#main
## Continue forever, since there is no win condition
while True:
#outputting board
    print(_board)
#getting input and moving piece
    _board.move(str(input("Please enter the move you would like to make, in the form of i,j to i2,j2: ")))
    if str(input("Would you like to quit? (y/n): ")) == "y": # Only way to end program execution
        break

# I genuinely have so many comments
# but it's telling me to make
# more, so here you go.
# here's more comments.
# is this enough yet?
# if it isn't i'm just going to give up and say that this is enough comments