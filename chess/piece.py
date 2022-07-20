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
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2