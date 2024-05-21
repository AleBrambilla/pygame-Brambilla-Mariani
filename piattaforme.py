import pygame
from pygame.locals import *
from random import randint

pygame.init()

class Piattaforma(pygame.sprite.Sprite):
    def __init__(self, y):
        image=pygame.image.load('Brambilla-Mariani-img/platform.png').convert_alpha()
        super().__init__()

        self.image=image
        self.image = pygame.transform.rotozoom(self.image, 0, 0.8)
        self.rect=self.image.get_rect(topleft=(randint(0,400), y))
        self.corrente=False
        #print(y)

    def scorri(self):
            self.rect.y+=3
            if self.rect.y>805:
                self.kill()

def corrente(piattaforme, player):          
    for i,piattaforma in enumerate(piattaforme.sprites()):
                if not piattaforma.corrente:    
                    if piattaforma.rect.colliderect(player.sprite.rect):
                        piattaforme.sprites()[i].corrente=True
                        #print(piattaforma.corrente)
                        for j in range(len(piattaforme.sprites()[:i-1:])):
                            piattaforme.sprites()[j].corrente=False  
        
def bool_scorrere(piattaforme, player):
    scorri=True
    corrente(piattaforme, player)
    for piattaforma in piattaforme.sprites(): 
        if piattaforma.rect.top >=700 and piattaforma.corrente:
            scorri=False
        

    return scorri
    