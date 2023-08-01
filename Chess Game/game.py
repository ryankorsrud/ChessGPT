import pygame, sys
from settings import *
from board import Board

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Chess')
        self.running = True
        self.board = Board()


        self.run()

    
    def run(self):
        while self.running:
            self.update()
            self.display()
    
    
    def update(self):
        # quits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def display(self):
        self.board.draw(self.screen)
        pygame.display.flip()    
