from modules.ValidateMoves import ValidateMoves
from modules.ValidateKills import ValidateKills
from modules.ValidateKing import ValidateKing
from modules.Constants import *
from modules.Game import Game

class Move:
    def __init__(self, whoMoved, piece, start_pos, end_pos, notation):
        self.whoMoved = whoMoved
        self.piece = piece
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.notation = notation
        self.whoMoved = Game.currentPlayer

move_history = []

def movePiece(self, event):
        # Get the current position of the mouse
        self.x = event.x-(SQSIZE/2)
        self.y = event.y-(SQSIZE/2)
        self.x = 0 if self.x < 0 else self.x
        self.y = 0 if self.y < 0 else self.y
        self.x = MAXPIECEX if self.x > MAXPIECEX else self.x
        self.y = MAXPIECEY if self.y > MAXPIECEY else self.y
        # Move the image to the new position
        self.board.coords(self.button_id, self.x, self.y)
        self.board.lift(self.button_id)

def startMovement(self, event):
    from modules.Board import Board
    from modules.Pieces import Piece
    self.x, self.y = event.x, event.y
    if Game.currentPlayer == self.colour:
        moves = ValidateMoves.getPossibleMoves(self.pos,self.piece, self.colour,self.moved,Board.boardArr)
        kills = ValidateKills.getPossibleKills(self.pos,self.piece, self.colour,self.moved,Board.boardArr)
        BoardArr = Board.boardArr
        ValidateKing.findCheckedMoves(BoardArr, moves, kills, self)
        self.validMoves = moves
        self.validKills = kills
        if moves != []:
            for pos in moves:
                self.imageIDs.append(Board.showMove(pos,self.board))
        if kills != []:
            for pos in kills:
                self.imageIDs.append(Board.showKill(pos,self.board))


from modules.ValidateMoves import ValidateMoves
from modules.ValidateKills import ValidateKills
from modules.ValidateKing import ValidateKing
from modules.Constants import *
from modules.Game import Game

class Move:
    def __init__(self, whoMoved, piece, start_pos, end_pos, notation):
        self.whoMoved = whoMoved
        self.piece = piece
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.notation = notation

move_history = []

def movePiece(self, event):
        # Get the current position of the mouse
        self.x = event.x-(SQSIZE/2)
        self.y = event.y-(SQSIZE/2)
        self.x = 0 if self.x < 0 else self.x
        self.y = 0 if self.y < 0 else self.y
        self.x = MAXPIECEX if self.x > MAXPIECEX else self.x
        self.y = MAXPIECEY if self.y > MAXPIECEY else self.y
        # Move the image to the new position
        self.board.coords(self.button_id, self.x, self.y)
        self.board.lift(self.button_id)

def startMovement(self, event):
    from modules.Board import Board
    from modules.Pieces import Piece
    self.x, self.y = event.x, event.y
    if Game.currentPlayer == self.colour:
        moves = ValidateMoves.getPossibleMoves(self.pos,self.piece, self.colour,self.moved,Board.boardArr)
        kills = ValidateKills.getPossibleKills(self.pos,self.piece, self.colour,self.moved,Board.boardArr)
        BoardArr = Board.boardArr
        ValidateKing.findCheckedMoves(BoardArr, moves, kills, self)
        self.validMoves = moves
        self.validKills = kills
        if moves != []:
            for pos in moves:
                self.imageIDs.append(Board.showMove(pos,self.board))
        if kills != []:
            for pos in kills:
                self.imageIDs.append(Board.showKill(pos,self.board))

def stopMovement(self, event):
    from modules.Pieces import Piece
    from modules.Board import Board
    from modules.Kill import Kill
    def move(x, y, moved):
        board.coords(self.button_id, x*SQSIZE, y*SQSIZE)
        for id in self.imageIDs:
            board.delete(id)
        if moved:
            self.firstMove = False
            self.moved = True
            for id in Piece.rectIDs:
                board.delete(id)
            Piece.rectIDs.append(Board.highlightSquare(self.pos, board)) # Images and rectangles can go in the same place as their id systems both work for deleting
            Piece.rectIDs.append(Board.highlightSquare([y, x], board))
            board.lift(self.button_id)
            Board.boardArr[y][x] = Board.boardArr[self.pos[0]][self.pos[1]]
            Board.boardArr[self.pos[0]][self.pos[1]] = Piece(board, 0, self.pos, "None")
            saveOldPos = self.pos
            self.pos = [y, x]
            for i in Board.boardArr:
                for j in i:
                    if j.piece == Piece.Pawn:
                        j.enPassantValid = False
            if self.piece == Piece.Pawn:
                self.enPassantValid = ValidateMoves.checkEnPassantValid(self.colour, self.pos, Board.boardArr, self.moved)
            currentPlayerBeforeChange = Game.currentPlayer
            Game.currentPlayer = "Black" if Game.currentPlayer == "White" else "White" # If the current player was White, change it to black, else change it to white
            KingsChecked = ValidateKing.findChecks(Board.boardArr)
            if KingsChecked[0]:
                if KingsChecked[1] == "White":
                    Game.WhiteKingChecked = True
                else:
                    Game.BlackKingChecked = True
                if ValidateKing.findCheckmate(Board.boardArr, KingsChecked[1]):
                    Game.Winner = "White" if KingsChecked[1] == "Black" else "Black"
                    print(f"{Game.Winner} wins by checkmate!")
            move_history.append(Move(currentPlayerBeforeChange, self.piece, saveOldPos, [x,y], getAlgebraicNotation(self.piece, saveOldPos, [y,x]))) # add move to history with algebraic notation

    x = event.x//SQSIZE
    y = event.y//SQSIZE
    XOutsideLimits = self.x == 0 or self.x == MAXPIECEX
    YOutsideLimits = self.y == 0 or self.y == MAXPIECEY
    if XOutsideLimits:
        x = self.x//SQSIZE
    if YOutsideLimits:
        y = self.y//SQSIZE
    board = self.board
    board.lift(self.button_id)
    if Game.currentPlayer != self.colour:
        move(self.pos[1], self.pos[0], False)
    elif [y, x] in self.validKills:
        Kill(board, [y, x], self.colour)
        move(x, y, True)
        self.firstMove = False
        self.moved = True
    elif Board.boardArr[y][x].piece != 0:
        move(self.pos[1], self.pos[0], False)
    elif [y, x] not in self.validMoves:
        move(self.pos[1], self.pos[0], False)
    else:
        move(x, y, True)
        self.firstMove = False
        self.moved = True

def getAlgebraicNotation(piece, start_pos, end_pos):
    file_names = ["a", "b", "c", "d", "e", "f", "g", "h"]
    start_file = file_names[start_pos[1]]
    start_rank = str(8 - start_pos[0])
    end_file = file_names[end_pos[1]]
    end_rank = str(8 - end_pos[0])
    return [piece, f"{start_file}{start_rank}-{end_file}{end_rank}"]
