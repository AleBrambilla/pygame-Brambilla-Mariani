import pygame, sys
import pygame.display
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (550, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo=pygame.image.load('sfondo.png').convert()
omino_base=pygame.image.load('personaggio base.png').convert_alpha()

pygame.display.set_caption('Home')

clock = pygame.time.Clock()
fps = 60

keys=pygame.key.get_pressed()


def aggiorna():
    pygame.display.update()
    clock.tick(fps)



    
        


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sfondo, (0,0))
    screen.blit(omino_base, (0,0))


    aggiorna()