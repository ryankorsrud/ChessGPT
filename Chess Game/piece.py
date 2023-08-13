import pygame
from settings import *

class Piece:
    # initializes the piece
    def __init__(self, colour, row, col, img_name, val):
        # since the pieces are 80px and the squares are 100px, we must offset their position by 10 to be centered in their square
        self.POS_OFFSET = 10
        self.colour = colour
        self.row = row
        self.col = col
        self.val = val
        
        img_dir = 'assets/' + img_name + '.png'
        # pieces that are initially on the 1st and 2nd rank are white
        self.image = pygame.image.load(img_dir).convert_alpha()
    
    '''
    Draws the piece.
    Args(pygame screen)
    Returns(None)  
    '''
    def draw(self, screen):
        screen.blit(self.image, (self.col*SQ_WIDTH + self.POS_OFFSET, self.row*SQ_HEIGHT + self.POS_OFFSET))

class Pawn(Piece):
    def __init__(self, colour, row, col, img_name):
        super().__init__(colour, row, col, img_name, val=1)

class Bishop(Piece):
    def __init__(self, colour, row, col, img_name):
        super().__init__(colour, row, col, img_name, val=3)

class Knight(Piece):
    def __init__(self, colour, row, col, img_name):
        super().__init__(colour, row, col, img_name, val=3)

class Rook(Piece):
    def __init__(self, colour, row, col, img_name):
        super().__init__(colour, row, col, img_name, val=5)

class Queen(Piece):
    def __init__(self, colour, row, col, img_name):
        super().__init__(colour, row, col, img_name, val=10)

class King(Piece):
    def __init__(self, colour, row, col, img_name):
        super().__init__(colour, row, col, img_name, val=10000)