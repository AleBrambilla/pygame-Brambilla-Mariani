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
            
class Classica(Piattaforma):
    def __init__(self, y):
        super().__init__(y)
    def update() -> None:
        super().scorri()

class Mobile_x(Piattaforma):
    def __init__(self, y):
        super().__init__(y)
        self.delta=randint(50,200)
        self.centro=self.rect.centerx
        self.direzione=-1
    
    def update(self):
        super().scorri()
        self.rect.x+=self.direzione*3
        if self.rect.x < self.centro - self.delta: self.direzione = 1
        if self.rect.x > self.centro + self.delta: self.direzione = -1

class Mobile_y(Piattaforma):
    def __init__(self, y):
        super().__init__(y)
        self.delta=randint(25,100)
        self.centro=self.rect.centery
        self.direzione=-1
    
    def update(self):
        super().scorri()
        self.rect.y+=self.direzione*3
        if self.rect.y < self.centro - self.delta: self.direzione = 1
        if self.rect.y > self.centro + self.delta: self.direzione = -1





def corrente(piattaforme, player):          
    for i,piattaforma in enumerate(piattaforme.sprites()):
                
                if not piattaforma.corrente:  
                    if piattaforma.rect.colliderect(player.sprite.rect):

                        piattaforme.sprites()[i].corrente=True

                        for j in range(len(piattaforme.sprites()[:i-1:])):
                            piattaforme.sprites()[j].corrente=False

                        break

    return i  
        
def bool_scorrere(piattaforme, player, score):

    i=corrente(piattaforme, player)

    scorri=True
    for piattaforma in piattaforme.sprites(): 
        if piattaforma.rect.top >=700 and piattaforma.corrente:
            scorri=False
        if score<120 and piattaforme.sprites()[i].rect.bottom>800:
            scorri=False
        

    return scorri
    