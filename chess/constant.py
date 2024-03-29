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

ROOK_EVAL = [[ 0,  0,  0,  0,  0,  0,  0,  0], [0.5, 1,  1,  1,  1,  1,  1, 0.5], 
             [-0.5, 0,  0,  0,  0,  0,  0, -0.5], [-0.5, 0,  0,  0,  0,  0,  0, -0.5], 
             [-0.5, 0,  0,  0,  0,  0,  0, -0.5], [-0.5, 0,  0,  0,  0,  0,  0, -0.5], 
             [-0.5, 0,  0,  0,  0,  0,  0, -0.5], [0, 0, 0, 0.5, 0.5, 0, 0, 0]]

KNIGHT_EVAL = [[-5, -4, -3, -3, -3, -3, -4, -5], [-4, -2, 0, 0, 0, 0, -2, -4], 
               [-3, 0, 1, 1.5, 1.5, 1, 0, -3], [-3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3], 
               [-3, 0, 1.5, 2, 2, 1.5, 0, -3], [-3, 0.5, 1, 1.5, 1.5, 1, 0.5, -3], 
               [-4, -2, 0, 0.5, 0.5, 0, -2, -4], [-5, -4, -3, -3, -3, -3, -4, -5]]

QUEEN_EVAL = [[-2, -1, -1, -0.5, -0.5, -1, -1, -2], [-1, 0, 0, 0, 0, 0, 0, -1], 
              [-1, 0, 0.5, 0.5, 0.5, 0.5, 0, -1], [-0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5], 
              [0, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5], [-1, 0.5, 0.5, 0.5, 0.5, 0.5, 0, -1], 
              [-1, 0, 0.5, 0, 0, 0, 0, -1], [-2, -1, -1, -0.5, -0.5, -1, -1, -2]]

BISHOP_EVAL = [[-2, -1, -1, -1, -1, -1, -1, -2], [-1, 0, 0, 0, 0, 0, 0, -1], 
               [-1, 0, 0.5, 1, 1, 0.5, 0, -1], [-1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1], 
               [-1, 0, 1, 1, 1, 1, 0, -1], [-1, 1, 1, 1, 1, 1, 1, -1], 
               [-1, 0.5, 0, 0, 0, 0, 0.5, -1], [-2, -1, -1, -1, -1, -1, -1, -2]]

PAWN_EVAL = [[0, 0, 0, 0, 0, 0, 0, 0], [5, 5, 5, 5, 5, 5, 5, 5], 
             [1, 1, 2, 3, 3, 2, 1, 1], [0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5],
             [0, 0, 0, 2, 2, 0, 0, 0], [0.5, -0.5, -1, 0, 0, -1, -0.5, 0.5], 
             [0.5, 1, 1, -2, -2, 1, 1, 0.5], [0, 0, 0, 0, 0, 0, 0, 0]]

EVAL[KING] = KING_EVAL
EVAL[QUEEN] = QUEEN_EVAL
EVAL[KNIGHT] = KNIGHT_EVAL
EVAL[PAWN] = PAWN_EVAL
EVAL[BISHOP] = BISHOP_EVAL
EVAL[ROOK] = ROOK_EVAL

CROWN = pygame.transform.scale(pygame.image.load('checkers/crown.png'), (44, 25))

BLACK_KING = pygame.transform.scale(pygame.image.load('checkers/image/black_king.png'), (80, 60))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load('checkers/image/black_queen.png'), (80, 60))
BLACK_ROOK = pygame.transform.scale(pygame.image.load('checkers/image/black_rook.png'), (80, 60))
BLACK_BISHOP = pygame.transform.scale(pygame.image.load('checkers/image/black_bishop.png'), (80, 60))
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load('checkers/image/black_knight.png'), (80, 60))
BLACK_PAWN = pygame.transform.scale(pygame.image.load('checkers/image/black_pawn.png'), (70, 60))

WHITE_KING = pygame.transform.scale(pygame.image.load('checkers/image/white_king.png'), (80, 60))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load('checkers/image/white_queen.png'), (80, 60))
