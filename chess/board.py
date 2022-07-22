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