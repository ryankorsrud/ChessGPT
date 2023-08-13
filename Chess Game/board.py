import pygame
from settings import *
from square import Square
from piece import *

class Board:
    # initializes the board
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
    Args(None)
    Returns(List[List[Square]
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
    Args(None)
    Returns(None)
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
    Args(None)
    Returns(None)
    '''
    def draw(self, screen):
        for row in self.squares:
            for square in row:
                square.draw(screen)
    
    '''
    Gets the valid moves of a piece.
    Args(Piece: piece, int: row, int: column)
    Returns(List[List[int]])
    '''
    def get_moves(self, piece, row, col):
        '''
        Checks that a row and column is inside the board
        Args(int: row, int: column)
        Returns(bool)
        '''
        def in_range(r, c):
            return (0 <= r <= 7) and (0 <= c <= 7)
        
        '''
        Gets a list of the valid king moves
        Args(None)
        Returns(List[List[int]])
        '''
        def king_moves():
            #gets all of the possible moves
            possible_moves = []
            for i in range(-1, 1):
                for j in range(-1, 1):
                    if i != 0 or j != 0:
                        possible_moves.append([i,j])
            
            # parses the possible moves for only valid moves
            valid_moves = []
            for move in possible_moves:
                r, c = move[0]+row, move[1]+col
                if in_range(r, c):
                    if self.squares[r][c].piece != None:
                        if self.squares[r][c].piece.colour != piece.colour:
                            valid_moves.append([r,c])
                    else:
                        valid_moves.append([r,c])
            return valid_moves

        '''
        Gets a list of the valid knight moves
        Args(None)
        Returns(List[List[int]])
        '''
        def knight_moves():
            possible_moves = [[-1, 2], [-1, -2], [1, 2], [1, -2], [-2, 1], [-2,-1], [2, 1], [2, -1]]
            
            # parses the possible moves for onlyt valid moves
            valid_moves = []
            for move in possible_moves:
                r, c = move[0]+row, move[1]+col
                if in_range(r, c):
                    if self.squares[r][c].piece != None:
                        if self.squares[r][c].piece.colour != piece.colour:
                            valid_moves.append([r,c])
                    else:
                        valid_moves.append([r,c])
            return valid_moves

        '''
        Gets a list of the valid straight line moves for some directions
        Args(List[List[int]]: directions)
        Returns(List[List[int]])
        '''
        def line_moves(directions):
            valid_moves = []
            for dir in directions:
                r, c = row + dir[0], col + dir[1]
                while in_range(r, c):
                    if self.squares[r][c].piece != None:
                        if self.squares[r][c].piece.colour != piece.colour:
                            valid_moves.append([r,c])
                        break   # exit the while loop since a piece blocks any remaining squares in the direction
                    else:
                        valid_moves.append([r,c])
                    r, c = r+dir[0], c+dir[1]
            return valid_moves
        
        diagonal_directions = [[-1, -1], [-1, 1], [1, 1], [1,-1]]         
        horizontal_and_vertical_directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        if isinstance(piece, King):
            return king_moves()
        if isinstance(piece, Knight):
            return knight_moves()
        elif isinstance(piece, Bishop):
            return line_moves(diagonal_directions)
        elif isinstance(piece, Rook):
            return line_moves(horizontal_and_vertical_directions)
        elif isinstance(piece, Queen):
            return line_moves(diagonal_directions+horizontal_and_vertical_directions)