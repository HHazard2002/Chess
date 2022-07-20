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
    
    def draw(self, win):
        if self.color == BLACK:
            if self.type == ROOK:
                win.blit(BLACK_ROOK, (self.x - 47, self.y - 25))
            if self.type == BISHOP:
                win.blit(BLACK_BISHOP, (self.x - 40, self.y - 30))
            if self.type == KNIGHT:
                win.blit(BLACK_KNIGHT, (self.x - 40, self.y - 30))
            if self.type == KING:
                win.blit(BLACK_KING, (self.x - 40, self.y - 30))
            if self.type == QUEEN:
                win.blit(BLACK_QUEEN, (self.x - 40, self.y - 30))
            if self.type == PAWN:
                win.blit(BLACK_PAWN, (self.x - 35, self.y - 25))
        else:
            if self.type == ROOK:
                win.blit(WHITE_ROOK, (self.x - 35, self.y - 30))
            if self.type == BISHOP:
                win.blit(WHITE_BISHOP, (self.x - 40, self.y - 30))
            if self.type == KNIGHT:
                win.blit(WHITE_KNIGHT, (self.x - 40, self.y - 30))
            if self.type == KING:
                win.blit(WHITE_KING, (self.x - 40, self.y - 30))
            if self.type == QUEEN:
                win.blit(WHITE_QUEEN, (self.x - 40, self.y - 30))
            if self.type == PAWN:
                win.blit(WHITE_PAWN, (self.x - 35, self.y - 25))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)