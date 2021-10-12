from pieces import piece, empty

class board():
    def __init__(self):
        self.board = [
            [
                0
            ],
            [
                0
            ],
            [
                0
            ],
            [
                0
            ],
            [
                0
            ],
            [
                0
            ],
            [
                0
            ],
            [
                0
            ],
        ]
    
    def __str__(self):
        string = ""
        for list in self.board:
            for item in list:
                string += str(item) + " "
            string += "\n"
        return string
