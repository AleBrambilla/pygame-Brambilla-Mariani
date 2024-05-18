import pygame
from pygame.locals import *
from sys import exit

from player import Player

pygame.init()


WINDOW_SIZE = (550, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo = pygame.image.load('Brambilla-Mariani-img/sfondo.png').convert()
ground = pygame.image.load('Brambilla-Mariani-img/ground.png').convert()

player = pygame.sprite.GroupSingle()
player.add(Player())

pygame.display.set_caption('Game')

clock = pygame.time.Clock()
fps = 60

mouse=pygame.mouse.get_pos()
tasti_mouse=pygame.mouse.get_pressed()

while True:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sfondo, (0,0))
    screen.blit(ground, (0, 700))
    player.update()
    player.draw(screen) 
    
    pygame.display.update()
    clock.tick(60)


