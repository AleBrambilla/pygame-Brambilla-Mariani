import pygame
from pygame.locals import *
from piattaforme import bool_scorrere

class Punteggio:
    def __init__(self):
        self.font=pygame.font.Font(None, 50)
        self.ammontare=0
        self.text=self.font.render(f'score: {int(self.ammontare)}', True, (255,0,0))

    def update(self, piattaforme, player, inizio):
        if bool_scorrere(piattaforme) and not inizio:
            self.ammontare+=1

    def RunMode(self, VEL_AVANZ):
        self.ammontare+=VEL_AVANZ/3

    def draw(self, screen):
        self.text=self.font.render(f'score: {int(self.ammontare)}', True, (255,0,0))
        screen.blit(self.text, (30, 30))

    def draw_finale(self, screen):
        font1=pygame.font.Font(None, 100)
        gameover=font1.render('GAME OVER', True, (255,255,255))
        gameover_rect=gameover.get_rect(center=(275, 100))

        font2=pygame.font.Font(None,50)
        punteggio_finale=font2.render(f'{int(self.ammontare)}', True, (255,255,255))
        punteggio_finale_rect=punteggio_finale.get_rect(center=(275,550))

        font3=pygame.font.Font(None, 25)
        istruzioni=font3.render('Space Key --> Restart', True, (255,255,255))
        istruzioni_rect=istruzioni.get_rect(center=(275, 650))

        screen.fill((0,0,0))
        screen.blit(gameover, gameover_rect)
        screen.blit(punteggio_finale, punteggio_finale_rect)
        screen.blit(istruzioni, istruzioni_rect)

