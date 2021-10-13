from pieces import piece, empty

class board():
    def __init__(self):
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

    def __str__(self):
        string = ""
        for list in self.board:
            for item in list:
                string += str(item) + " "
            string += "\n"
        return string
