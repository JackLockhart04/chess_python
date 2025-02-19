import tkinter as tk
from board import Board
from pieces import Pawn

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess")
        self.board = Board()
        self.setup_pieces()
        self.create_widgets()

    def setup_pieces(self):
        for i in range(8):
            self.board.board[1][i] = Pawn('white')
            self.board.board[6][i] = Pawn('black')

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.draw_board()

    def draw_board(self):
        colors = ["white", "gray"]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x1 = col * 50
                y1 = row * 50
                x2 = x1 + 50
                y2 = y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                piece = self.board.board[row][col]
                if piece:
                    self.canvas.create_text(x1 + 25, y1 + 25, text=str(piece), font=("Arial", 24))

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()