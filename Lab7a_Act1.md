# Checkers game
### *Doesn't have any game logic whatsoever but it's still checkers*

Input must be given in the form i,j to i2,j2  
Since i and j are list indices, i goes right as it increases, but j goes down as it increases.  

## Algorithm
### *Why it works*
- Program is split into classes:
    - piece classes are piece and empty, used mostly to make output easier with the \_\_str\_\_() method
    - board is represented by the board() class, handles all the necessary logic.
- Designing piece classes:
    - Only necessary attributes are colour for the pieces and str output for both pieces and empties
    - Needs move_logic function, will return true if it is a piece, false if it is an empty
- Designing board:
    - needs move function that will process input into usable indices, then check to make sure that
        1. The piece exists
        2. The final location is valid
    - board will store all pieces in order in a 2d list
    - board has a \_\_str\_\_() method that outputs the correct board
- Main file:
    - All main file needs is to import and initialize a board, an input statement to call the move() function, and a loop to repeat input until the user is done, then print the board