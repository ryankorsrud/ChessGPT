import pygame, sys
from settings import *
from board import Board

class Game:
    #initializes the game
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Chess')
        self.running = True
        self.board = Board()
        self.players_turn = 'white' # white always starts

        self.run()

    '''
    Runs the game
    Args(None)
    Returns(None)
    '''
    def run(self):
        while self.running:
            self.update()
            self.display()
    
    '''
    Updates the game.
    Args(None)
    Returns(None)
    '''
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_row = event.pos[1]//SQ_WIDTH
                clicked_col = event.pos[0]//SQ_HEIGHT
                if self.board.squares[clicked_row][clicked_col].piece: #checks if the square they clicked has a piece
                    piece = self.board.squares[clicked_row][clicked_col].piece
                    
                    if piece.colour == self.players_turn: # checks if that piece belongs to the player who clicked it
                        moves = self.board.get_moves(piece, clicked_row, clicked_col)
                        print(moves)
                    
            # exits the game
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
    '''
    Displays the game on the screen.
    Args(None)
    Returns(None)
    '''
    def display(self):
        self.board.draw(self.screen)
        pygame.display.flip()    