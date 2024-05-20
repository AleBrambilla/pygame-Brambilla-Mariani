import pygame
from pygame.locals import *
from random import randint

pygame.init()

class Piattaforma(pygame.sprite.Sprite):
    def __init__(self) -> None:
        image=pygame.image.load('Brambilla-Mariani-img/platform.png').convert_alpha()
        super().__init__()

        self.image=image
        self.rect=self.image.get_rect(left=randint(0,400), bottom=-200)

    
    

    

    
