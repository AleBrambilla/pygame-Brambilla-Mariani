import pygame
from pygame.locals import *
from piattaforme import Piattaforma

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        global salto_alto, salto_basso
        salto_alto = pygame.image.load('Brambilla-Mariani-img/salto in alto.png').convert_alpha()
        salto_alto = pygame.transform.rotozoom(salto_alto, 0, 0.5)
        salto_basso = pygame.image.load('Brambilla-Mariani-img/salto in basso.png').convert_alpha()
        salto_basso = pygame.transform.rotozoom(salto_basso, 0, 0.5)

        self.image = salto_alto
        self.rect = self.image.get_rect(midbottom = (275,700))
        self.gravity = 0

        self.inizio=True

    def salto(self, salta):
        if self.rect.bottom >= 700 or salta:
            self.gravity = -22

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        

    def movimento(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 5
        if keys[K_RIGHT]:
            self.rect.x += 5

        if self.rect.x>550:
            self.rect.x=0

        if self.rect.x<0:
            self.rect.x=550

    def anima(self):
        if self.gravity>0:
            self.image=salto_basso
        else:
            self.image=salto_alto

    def update(self, salta):
        # if self.rect.colliderect(Piattaforma()) or self.inizio:
        if salta and self.gravity>0:
            self.salto(salta)
        # if self.rect.colliderect(Piattaforma()):
        #     self.inizio=False

        self.anima()
        self.apply_gravity()
        self.movimento()

    