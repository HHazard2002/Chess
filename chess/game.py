import pygame
from .constants import *
from checkers.board import Board
from minimax.algorithm import *

class Game:
  def __init__(self, win):
        self._init()
        self.win = win