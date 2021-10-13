from board import board

_board = board()

while True:
    print(_board)
    _board.move(str(input("Please enter the move you would like to make, in the form of i,j to i2,j2: ")))
    if str(input("Would you like to quit? (y/n): ")) == "y":
        break