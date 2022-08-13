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