import pygame
from pygame.locals import *
from piattaforme import corrente

class Punteggio:
    def __init__(self):
        self.font=pygame.font.Font(None, 50)
        self.ammontare=0
        self.text=self.font.render(f'score: {self.ammontare}', True, (255,0,0))

    def update(self,  piattaforme, player):
        self.ammontare+=corrente(piattaforme, player)

    def draw(self, screen):
        self.text=self.font.render(f'score: {self.ammontare}', True, (255,0,0))
        screen.blit(self.text, (30, 30))
