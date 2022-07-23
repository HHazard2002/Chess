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
