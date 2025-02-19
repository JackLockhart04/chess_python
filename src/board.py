class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Initialize an 8x8 board with None
        return [[None for _ in range(8)] for _ in range(8)]

    def display(self):
        for row in self.board:
            print(" ".join(["." if piece is None else str(piece) for piece in row]))