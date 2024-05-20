import pygame
from pygame.locals import *
from random import randint

pygame.init()

class Piattaforma(pygame.sprite.Sprite):
    def __init__(self, y):
        image=pygame.image.load('pygame-Brambilla-Mariani/Brambilla-Mariani-img/platform.png').convert_alpha()
        super().__init__()

        self.image=image
        self.image = pygame.transform.rotozoom(self.image, 0, 0.8)
        self.rect=self.image.get_rect(topleft=(randint(0,400), y))
        print(y)

    

    
    

    

    
