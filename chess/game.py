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
