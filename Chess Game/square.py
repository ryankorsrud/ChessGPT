import pygame
from settings import *

class Square:
    # initializes the square
    def __init__(self, row, col, piece=None):
        self.x = row
        self.y = col
        self.piece = piece
        self.colour = LIGHT_BEIGE if (row+col)%2 == 0 else GREEN
        self.rect = pygame.Rect(col*SQ_WIDTH, row*SQ_HEIGHT, SQ_WIDTH, SQ_HEIGHT)
    

    '''
    Draws the square.
    Args: pygame screen
    Returns: None.    
    '''
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
        if self.piece:
            self.piece.draw(screen)