import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
GREEN = (50,205,50)

KING = "KING"
QUEEN = "QUEEN"
PAWN = "PAWN"
BISHOP = "BISHOP"
ROOK = "ROOK"
KNIGHT = "KNIGHT"

EVAL = {}

KING_EVAL = [[-3, -4, -4, -5, -5, -4, -4, -3], [-3, -4, -4, -5, -5, -4, -4, -3], [-3, -4, -4, -5, -5, -4, -4, -3], [-3, -4, -4, -5, -5, -4, -4, -3],[-2, -3, -3, -4, -4, -3, -3, -2], [-1, -2, -2, -2, -2, -2, -2, -1], [ 2,  2,  0,  0,  0,  0,  2,  2], [ 2,  3,  1,  0,  0,  0,  3,  2]]

