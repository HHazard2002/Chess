from .constants import *
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color, type, value):
        self.row = row
        self.col = col
        self.color = color
        self.type = type
        self.king = False
        self.value = value
        self.x = 0
        self.y = 0
        self.calc_pos()