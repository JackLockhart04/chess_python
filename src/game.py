from board import Board
from pieces import Pawn

class Game:
    def __init__(self):
        self.board = Board()
        self.setup_pieces()

    def setup_pieces(self):
        # Example: Place pawns on the board
        for i in range(8):
            self.board.board[1][i] = Pawn('white')
            self.board.board[6][i] = Pawn('black')

    def start(self):
        self.board.display()

if __name__ == "__main__":
    game = Game()
    game.start()