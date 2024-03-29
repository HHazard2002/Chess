import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.game import Game
from minimax.algorithm import *
import time

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():

    if 1 == 0:

        run = True
        clock = pygame.time.Clock()
        game = Game(WIN)

        while run:
            clock.tick(FPS)

            if game.winner() != None:
                print(game.winner())
                run = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)
                
            game.update()
            
        pygame.quit()

        if 0 == 0:
            run = True
            clock = pygame.time.Clock()
            game = Game(WIN)

            while run:
                clock.tick(FPS)

                if game.turn == BLACK:
                    start = time.time()

                    value, new_board = pruning(game.get_board(), 3, BLACK, game)
                    print(value)

                    game.ai_move(new_board)
                    end = time.time()
                    print(end - start)

                if game.winner() != None:
                    print(game.winner())
                    run = False
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                        game.select(row, col)
                
                game.update()