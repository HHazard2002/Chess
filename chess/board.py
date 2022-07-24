import pygame
from minimax.algorithm import simulate_move
from .constants import *
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
