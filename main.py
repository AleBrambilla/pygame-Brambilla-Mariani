import pygame, sys
import pygame.display
from pygame.locals import *

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        salto_alto = pygame.image.load('pygame-Brambilla-Mariani/salto in alto.png').convert_alpha()
        salto_alto = pygame.transform.rotozoom(salto_alto, 0, 0.5)
        salto_basso = pygame.image.load('pygame-Brambilla-Mariani/salto in basso.png').convert_alpha()
        salto_basso = pygame.transform.rotozoom(salto_basso, 0, 0.5)
        salti = [salto_alto, salto_basso]
        ind_salti = 1

        self.image = salti[ind_salti]
        self.rect = self.image.get_rect(midbottom = (275,700))


WINDOW_SIZE = (550, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo=pygame.image.load('pygame-Brambilla-Mariani/sfondo.png').convert()
ground = pygame.image.load('pygame-Brambilla-Mariani/ground.png').convert()

player = pygame.sprite.GroupSingle()
player.add(Player())

pygame.display.set_caption('Home')

clock = pygame.time.Clock()
fps = 60

keys=pygame.key.get_pressed()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sfondo, (0,0))
    screen.blit(ground, (0, 700))
    player.draw(screen) 
    
    pygame.display.update()
    clock.tick(60)
