import tkinter as tk
from PIL import Image, ImageTk
from modules.Board import Board
from modules.Pieces import Piece as Pieces
from modules.Constants import *
from modules.Movement import move_history

pieceIdToName = {
    1: "King",
    2: "Pawn",
    3: "Knight",
    4: "Bishop",
    5: "Rook",
    6: "Queen"
}

def update_move_history(event):
    moveHistory.delete("1.0", tk.END)
    moveHistory.insert(tk.END, "Move History:\n")
    for move in move_history:
        moveHistory.insert(tk.END, f"{move.whoMoved} : {pieceIdToName[move.notation[0]]} {move.notation[1]}\n")

window = tk.Tk()

window.title("Chess")
window.iconbitmap("icon.ico")
window.configure(bg="#F6DFF6")
window.geometry(f"1200x800")

board = Board(window,WIDTH,HEIGHT)

board.LoadPiecesFromFen(board.canvas, "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr w KQkq - 0 1") #Loads starting board.

moveHistory = tk.Text(window, width=50, height=20, bg="#F6DFF6", fg="#303030", font=("Comic Sans MS", 20))
moveHistory.pack(side="right", fill="y")
moveHistory.insert(tk.END, "Move History:\n")

window.bind("<Button>", update_move_history)

window.mainloop()
