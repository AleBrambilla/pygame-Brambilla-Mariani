import pygame
from pygame.locals import *
from piattaforme import bool_scorrere

class Punteggio:
    def __init__(self):
        self.font=pygame.font.Font(None, 50)
        self.ammontare=0
        self.text=self.font.render(f'score: {self.ammontare}', True, (255,0,0))

    def update(self, piattaforme, player):
        if bool_scorrere(piattaforme, player):
            self.ammontare+=1

    def draw(self, screen):
        self.text=self.font.render(f'score: {self.ammontare}', True, (255,0,0))
        screen.blit(self.text, (30, 30))

    def draw_finale(self, screen, t):
        font1=pygame.font.Font(None, 150)
        gameover=font1.render('GAME OVER', True, (255,255,255))
        gameover_rect=gameover.get_rect(center=(275, 100))

        font2=pygame.font.Font(None,50)
        punteggio_finale=font2.render(f'{self.text}', True, (255,255,255))
        punteggio_finale_rect=punteggio_finale.get_rect(center=(275,550))

        if t:
            screen.blit(gameover, gameover_rect)
            screen.blit(punteggio_finale, punteggio_finale_rect)

