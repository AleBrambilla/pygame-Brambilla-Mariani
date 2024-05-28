import pygame
from pygame.locals import *
from piattaforme import Piattaforma

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        global img_destra, img_sinistra
        alto_destra = pygame.image.load('Brambilla-Mariani-img/salto in alto.png').convert_alpha()
        alto_destra = pygame.transform.rotozoom(alto_destra, 0, 0.5)
        basso_destra = pygame.image.load('Brambilla-Mariani-img/salto in basso.png').convert_alpha()
        basso_destra = pygame.transform.rotozoom(basso_destra, 0, 0.5)
        img_destra = [alto_destra, basso_destra]
        alto_sinistra = pygame.transform.flip(alto_destra, True, False)
        basso_sinistra = pygame.transform.flip(basso_destra, True, False)
        img_sinistra = [alto_sinistra, basso_sinistra]
        self.img = img_destra

        self.image = alto_destra
        self.rect = self.image.get_rect(midbottom = (275,700))
        self.gravity = 0

        self.inizio=True

    def salto(self):
        self.gravity=-22

    def apply_gravity(self):
        if self.gravity<22:
            self.gravity += 1
        self.rect.y += self.gravity

    def movimento(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 5
            self.img = img_sinistra
        if keys[K_RIGHT]:
            self.rect.x += 5
            self.img = img_destra

        if self.rect.centerx  > 550:
            self.rect.x = -20

        if self.rect.centerx < 0:
            self.rect.right=570

    def anima(self):
        if self.gravity>0:
            self.image=self.img[1]
        else:
            self.image=self.img[0]

    def update(self, inizio, salta):
        if salta and self.gravity>5:
            self.salto()
        self.anima()
        self.apply_gravity()
        self.movimento()
        


    