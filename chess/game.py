import pygame
from .constants import *
from checkers.board import Board
from minimax.algorithm import *

class Game:
  def __init__(self, win):
        self._init()
        self.win = win

  def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

  def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}

  def winner2(self):
        value, new_board = minimax(self.get_board(), 0, self.turn, self)
        print(value)
        if value < -800:
            return BLACK
        elif value > 800:
            return WHITE
        return None

  def winner(self):
        color = self.turn
        if self.board.is_checkmate(color):
            if color == BLACK:
                return WHITE
            elif color == WHITE:
                return BLACK
        else:
            return None
  
  def reset(self):
        self._init()

  def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
              self.selected = None
              self.select(row, col)
            elif self.winner() != None:
              print(self.winner())
              run = False
      
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_legal_moves(piece)
            return True
          
        return False

  def _move(self, row, col):

        eaten_piece = self.board.get_piece(row, col)
        piece = self.selected
        board = self.board
        if piece and eaten_piece != 0 and (row, col) in self.valid_moves:
            self.eaten_pieces = eaten_piece
            board.remove(eaten_piece)
            board.move(piece, row, col)
            self.change_turn()
            if piece.type == PAWN and ((row == 7 and piece.color == BLACK) or (row == 0 and piece.color == WHITE)):
                piece.type = QUEEN 
                piece.value = 9
        elif piece and piece.type == KING:
            if piece.color == BLACK and board.roker_black:
                if col == 2:
                    board.move(board.get_piece(0,0), 0, 3)
                elif col == 6:
                    board.move(board.get_piece(0,7), 0, 5)
            elif piece.color == WHITE and board.roker_white:
                if col == 2:
                    board.move(board.get_piece(7,0), 7, 3)
                elif col == 6:
                    board.move(board.get_piece(7,7), 7, 5)
        if piece and eaten_piece == 0 and (row, col) in self.valid_moves:
            board.move(piece, row, col) 
            self.change_turn()  
        else:
            return False 
        if piece.type == PAWN and ((row == 7 and piece.color == BLACK) or (row == 0 and piece.color == WHITE)):
            piece.type = QUEEN
            piece.value = 9
        if piece.type == KING or piece.type == ROOK:
            if piece.color == BLACK:
                board.roker_black = False
            elif piece.color == WHITE:
                board.roker_white = False
        elif piece.type == PAWN and ((piece.color == BLACK and row == 3) or (piece.color == WHITE and row == 4)) :
            board.en_passant = piece
        else:
            board.en_passant = None
        if board.eaten_en_passant:
            board.remove(board.eaten_en_passant)
            board.eaten_en_passant = None

        return True

  def draw_valid_moves(self, moves):
    for move in moves:
        row, col = move
        pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

  def new_piece(self, move):
    return False

  def change_turn(self):
    self.valid_moves = {}
    if self.turn == BLACK:
        self.turn = WHITE
    else:
        self.turn = BLACK

  def get_board(self):
    return self.board