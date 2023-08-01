import pygame
from settings import *
from square import Square
from piece import *

class Board:
    def __init__(self):
        self.config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.squares = self.generate_squares()
        self.generate_pieces()

    '''
    Creates a 2d list of Square objects.
    Args: None
    Returns: 2d list
    '''
    def generate_squares(self):
        output = []
        for row in range(0, TILES, 1):
            output.append([])
            for col in range(0, TILES, 1):
                output[row].append(Square(row, col))       
        return output
        
    '''
    Generates pieces from the boards config
    Args: None
    Returns: None
    '''
    def generate_pieces(self):
        for row in range(0, TILES, 1):
            for col in range(0, TILES, 1):
                if self.config[row][col] != EMPTY:
                    colour = 'white' if 'w' in self.config[row][col] else 'black'
                    if 'R' in self.config[row][col]:
                        self.squares[row][col].piece = Rook(colour, row, col, self.config[row][col])
                    elif 'N' in self.config[row][col]:
                        self.squares[row][col].piece = Knight(colour, row, col, self.config[row][col])
                    elif 'B' in self.config[row][col]:
                        self.squares[row][col].piece = Bishop(colour, row, col, self.config[row][col])
                    elif 'Q' in self.config[row][col]:
                        self.squares[row][col].piece = Queen(colour, row, col, self.config[row][col])
                    elif 'K' in self.config[row][col]:
                        self.squares[row][col].piece = King(colour, row, col, self.config[row][col])
                    elif 'p' in self.config[row][col]:
                        self.squares[row][col].piece = Pawn(colour, row, col, self.config[row][col])

    '''
    Draws the board
    Args: None
    Returns: None
    '''
    def draw(self, screen):
        for row in self.squares:
            for square in row:
                square.draw(screen)