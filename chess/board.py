import pygame
from minimax.algorithm import simulate_move
from .constant import *
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.number_eaten_pieces = 0
        self.eaten_pieces = []
        self.en_passant = None
        self.eaten_en_passant = None
        self.roker_white = True
        self.roker_black = True
        self.create_board()

    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, GREEN, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def evaluate(self):
        evaluation = 0
        black_pieces = self.get_all_pieces(BLACK)
        white_pieces = self.get_all_pieces(WHITE)
        
        for piece in black_pieces:
            evaluation += piece.value + EVAL[piece.type][7 - piece.row][7 - piece.col]
        for piece in white_pieces:
            evaluation -= piece.value + EVAL[piece.type][piece.row][piece.col]    
            
        return evaluation

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color and piece.row <= 7:
                    pieces.append(piece)
        return pieces

    def get_piece(self, row, col):
        return self.board[row][col]
    
    def get_king(self, color):
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.type == KING and piece.color == color:
                    return (piece.row, piece.col)
    
    def simulate_move(self, piece, move, board):
        board.move(piece, move[0], move[1])

        return board

    def is_check(self, move, piece):

        king_position = (-1, -1)
        possible_moves = {}
        is_check = False
        removed = False
        piece_row = piece.row
        piece_col = piece.col
        index_row = move[0]
        index_col = move[1]
        color = piece.color
        moves = {}
        moves[(index_row, index_col)] = piece
        if color == BLACK:
            not_color = WHITE
        else:
            not_color = BLACK
       
        if self.board[index_row][index_col] != 0:
            removed_piece = self.get_piece(index_row, index_col)
            removed = True
            self.remove(removed_piece)

        self.move(piece, index_row, index_col)

        king_position = self.get_king(color)
        
        if king_position != (-1, -1):
            for opposite_piece in self.get_all_pieces(not_color):
                possible_moves.update(self.get_valid_moves(opposite_piece))
                if king_position in possible_moves.keys():
                    is_check = True
                    break

        self.move(piece, piece_row, piece_col)
        if removed:
            self.move(removed_piece, index_row, index_col)
            self.number_eaten_pieces -= 1
            self.eaten_pieces.pop()

        return is_check

    def get_legal_moves(self, piece):

        all_legal_moves = {}
        illegal_moves = []
        all_legal_moves = self.get_valid_moves(piece)
        for move in all_legal_moves:
            if self.is_check(move, all_legal_moves[move]):
                illegal_moves.append(move)

        for move in illegal_moves:
            all_legal_moves.pop(move)

        return all_legal_moves

    def is_checkmate(self, color):
        moves = {}
        pieces = self.get_all_pieces(color)
        for piece in pieces:
            moves.update(self.get_legal_moves(piece))
            if len(moves) != 0:
                return False
        return True

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def create_board(self):
        for row in range(ROWS + 1):
            self.board.append([])
            for col in range (COLS):
                if row == 0:
                    if (col == 0 or col == 7):
                        self.board[row].append(Piece(row, col, BLACK, ROOK, 50))
                    if (col == 1 or col == 6):
                        self.board[row].append(Piece(row, col, BLACK, KNIGHT, 30))
                    if (col == 2 or col == 5):
                        self.board[row].append(Piece(row, col, BLACK, BISHOP, 30))
                    if (col == 3):
                        self.board[row].append(Piece(row, col, BLACK, QUEEN, 90))
                    if (col == 4):
                        self.board[row].append(Piece(row, col, BLACK, KING, 900))
                elif row == 1:
                  self.board[row].append(Piece(row, col, BLACK, PAWN, 10))
                elif row == 6:
                    self.board[row].append(Piece(row, col, WHITE, PAWN, 10))
                elif row == 7:
                    if (col == 0 or col == 7):
                        self.board[row].append(Piece(row, col, WHITE, ROOK, 50))
                    if (col == 1 or col == 6):
                        self.board[row].append(Piece(row, col, WHITE, KNIGHT, 30))
                    if (col == 2 or col == 5):
                        self.board[row].append(Piece(row, col, WHITE, BISHOP, 30))
                    if (col == 3):
                        self.board[row].append(Piece(row, col, WHITE, QUEEN, 90))
                    if (col == 4):
                        self.board[row].append(Piece(row, col, WHITE, KING, 900))
                else:
                    self.board[row].append(0)
        
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, piece):
        self.board[8].append(0)
        self.move(piece, 8, self.number_eaten_pieces)
        self.number_eaten_pieces += 1
        self.eaten_pieces.append(piece)
        
        if 0 == 1:
            for piece in piece:
                self.board[piece.row][piece.col] = 0
                if piece != 0:
                    if piece.color == WHITE:
                        self.red_left -= 1
                    else:
                        self.white_left -= 1
    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1

        col = piece.col
        row = piece.row
        color = piece.color
        type = piece.type
        direction = 0
        if piece.color == BLACK:
            direction = 1
        else:
            direction -1

        if type == PAWN:
            moves.update(self.pawn_moves(col, row, color))
        if type == KING:
            moves.update(self.king_moves(col, row, color))
        if type == BISHOP or type == QUEEN:
            moves.update(self.bishop_up_left(col, row, col, row, color))
            moves.update(self.bishop_up_right(col, row, col, row, color))
            moves.update(self.bishop_down_left(col, row, col, row, color))
            moves.update(self.bishop_down_right(col, row, col, row, color))
        if type == ROOK or type == QUEEN:
            moves.update(self.rook_up(col, row, col, row, color))
            moves.update(self.rook_down(col, row, col, row, color))
            moves.update(self.rook_left(col, row, col, row, color))
            moves.update(self.rook_right(col, row, col, row, color))
        if type == KNIGHT:
            moves.update(self.knight_moves(col, row, color))   
    
        return moves

    def pawn_moves(self, col, row, color):
        if color == WHITE:
            new_row = row - 1
        else:
            new_row = row + 1
        moves = {}
        current = self.board[row][col]
        if 0 <= new_row <= 7:
    
            if self.board[new_row][col] == 0:
                moves[(new_row, col)] = current
                if row == 6 and color == WHITE and self.board[row - 2][col] == 0:
                    moves[(row - 2, col)] = current
                elif row == 1 and color == BLACK and self.board[row + 2][col] == 0:
                    moves[(row + 2, col)] = current  

            if col + 1 <= 7 and self.board[new_row][col + 1] != 0 and self.board[new_row][col + 1].color != color:
                moves[(new_row, col+1)] = current
                 
            if 0 <= col - 1 and self.board[new_row][col - 1] != 0 and self.board[new_row][col - 1].color != color:
                moves[(new_row, col-1)] = current
            
            if self.en_passant and self.en_passant.row == row:
                if 7 >= col + 1 and self.en_passant.col == col + 1:
                    moves[(new_row, col+1)] = current
                    self.eaten_en_passant = self.en_passant
                elif 0 <= col -1 and self.en_passant.col == col - 1:
                    moves[(new_row, col-1)] = current
                    self.eaten_en_passant = self.en_passant

        return moves

    def king_moves(self, col, row, color):
        moves = {}
        current = self.board[row][col]
        if 0 <= row - 1:
            if self.board[row - 1][col] == 0 or self.board[row - 1][col].color != color:
                moves[(row - 1, col)] = current
            if 0 <= col - 1 and (self.board[row - 1][col - 1] == 0 or self.board[row - 1][col - 1].color != color):
                moves[(row - 1, col - 1)] = current
            if 7 >= col + 1 and (self.board[row - 1][col + 1] == 0 or self.board[row - 1][col + 1].color != color):
                moves[(row - 1, col + 1)] = current
        if 7 >= row + 1:
            if self.board[row + 1][col] == 0 or self.board[row + 1][col].color != color:
                moves[(row + 1, col)] = current
            if 0 <= col - 1 and (self.board[row + 1][col - 1] == 0 or self.board[row + 1][col - 1].color != color):
                moves[(row + 1, col - 1)] = current
            if 7 >= col + 1 and (self.board[row + 1][col + 1] == 0 or self.board[row + 1][col + 1].color != color):
                moves[(row + 1, col + 1)] = current
        if 0 <= col - 1:
            if self.board[row][col - 1] == 0 or self.board[row][col - 1].color != color:
                moves[(row, col - 1)] = current
        if 7 >= col + 1:
            if self.board[row][col + 1] == 0 or self.board[row][col + 1].color != color:
                moves[(row, col + 1)] = current
        if color == BLACK and self.roker_black:
            if self.board[0][1] == 0 and self.board[0][2] == 0 and self.board[0][3] == 0:
                moves[(0,2)] = current
            if self.board[0][5] == 0 and self.board[0][6] == 0:
                moves[(0,6)] = current
        elif color == WHITE and self.roker_white:
            if self.board[7][1] == 0 and self.board[7][2] == 0 and self.board[7][3] == 0:
                moves[(7,2)] = current
            if self.board[7][5] == 0 and self.board[7][6] == 0:
                moves[(7,6)] = current
            
        return moves

    def bishop_up_left(self, current_col, current_row, col, row, color):
        moves = {}
        current = self.board[current_row][current_col]
        if 0 <= col - 1 and 0 <= row - 1:
            if self.board[row - 1][col - 1] == 0:
                moves[(row - 1, col - 1)] = current
                moves.update(self.bishop_up_left(current_col, current_row, col - 1, row - 1, color))
            elif self.board[row - 1][col - 1].color != color:
                moves[(row - 1, col - 1)] = current

        return moves

    def bishop_up_right(self, current_col, current_row, col, row, color):
        moves = {}
        current = self.board[current_row][current_col]
        if 7 >= col + 1 and 0 <= row - 1:
            if self.board[row - 1][col + 1] == 0:
                moves[(row - 1, col + 1)] = current
                moves.update(self.bishop_up_right(current_col, current_row, col + 1, row - 1, color))
            elif self.board[row - 1][col + 1].color != color:
                moves[(row - 1, col + 1)] = current

        return moves

    def bishop_down_left(self, current_col, current_row, col, row, color):
        moves = {}
        current = self.board[current_row][current_col]
        if 0 <= col - 1 and 7 >= row + 1:
            if self.board[row + 1][col - 1] == 0:
                moves[(row + 1, col - 1)] = current
                moves.update(self.bishop_down_left(current_col, current_row, col - 1, row + 1, color))
            elif self.board[row + 1][col - 1].color != color:
                moves[(row + 1,col - 1)] = current

        return moves
    
    def bishop_down_right(self, current_col, current_row, col, row, color):
        moves = {}
        current = self.board[current_row][current_col]
        if 7 >= col + 1 and 7 >= row + 1:
            if self.board[row + 1][col + 1] == 0:
                moves[(row + 1, col + 1)] = current
                moves.update(self.bishop_down_right(current_col, current_row, col + 1, row + 1, color))
            elif self.board[row + 1][col + 1].color != color:
                moves[(row + 1, col + 1)] = current

        return moves

    def rook_up(self, current_col, current_row, col, row, color):
        moves = {}
        current = self.board[current_row][current_col]
        if 0 <= col - 1:
            if self.board[row][col - 1] == 0:
                moves[(row, col - 1)] = current
                moves.update(self.rook_up(current_col, current_row, col - 1, row, color))
            elif self.board[row][col - 1].color != color:
                moves[(row, col - 1)] = current
        return moves

    def rook_down(self, current_col, current_row, col, row, color):
        moves = {}
        current = self.board[current_row][current_col]
        if 7 >= col + 1:
            if self.board[row][col + 1] == 0:
                moves[(row, col + 1)] = current
                moves.update(self.rook_down(current_col, current_row, col + 1, row, color))
            elif self.board[row][col + 1].color != color:
                moves[(row, col + 1)] = current
        return moves

    def rook_right(self, current_col, current_row, col, row, color):
        moves = {}
        current = self.board[current_row][current_col]
        if 7 >= row + 1:
            if self.board[row + 1][col] == 0:
                moves[(row + 1, col)] = current
                moves.update(self.rook_right(current_col, current_row, col, row + 1, color))
            elif self.board[row + 1][col].color != color:
                moves[(row + 1, col)] = current
        return moves

    def rook_left(self, current_col, current_row, col, row, color):
        moves = {}
        current = self.board[current_row][current_col]
        if 0 <= row - 1:
            if self.board[row - 1][col] == 0:
                moves[(row - 1, col)] = current
                moves.update(self.rook_left(current_col, current_row, col, row - 1, color))
            elif self.board[row - 1][col].color != color:
                moves[(row - 1, col)] = current
        return moves