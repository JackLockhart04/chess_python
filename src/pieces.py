class Piece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.symbol

class Pawn(Piece):
    symbol = 'P'