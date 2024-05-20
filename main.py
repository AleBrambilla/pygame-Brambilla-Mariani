import pygame
from pygame.locals import *
from sys import exit

from player import Player
from piattaforme import Piattaforma

pygame.init()

def gameover():

    global Game_Over

    screen.fill((0,200,250))


    tasto_start=pygame.Surface((200, 100))
    tasto_start.fill((255,255,255))
    start_rect=tasto_start.get_rect(center=(275, 550))
    
    font=pygame.font.Font(None, 50)
    inizio=font.render('INIZIO', True, (0,0,0))
    inizio_rect=inizio.get_rect(center=(275, 550))

    font=pygame.font.Font(None, 150)
    titolo=font.render('TITOLO', True, (100,255,0))
    titolo_rect=titolo.get_rect(midtop=(275, 50))

    mouse=pygame.mouse.get_pos()
    tasti_mouse=pygame.mouse.get_pressed()

    if Game_Over:

        screen.blit(tasto_start, start_rect)
        screen.blit(inizio, inizio_rect)
        screen.blit(titolo, titolo_rect)

        if start_rect.collidepoint(mouse) and tasti_mouse[0]:
            Game_Over=False

    if player.sprite.rect.y>800:
        Game_Over=True
    
    


WINDOW_SIZE = (550, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo = pygame.image.load('Brambilla-Mariani-img/sfondo.png').convert()
ground = pygame.image.load('Brambilla-Mariani-img/ground.png').convert()
ground_rect=ground.get_rect(topleft=(0, 700))

player = pygame.sprite.GroupSingle()
player.add(Player())

pygame.display.set_caption('Home')

clock = pygame.time.Clock()
fps = 60


global Game_Over
Game_Over=True

while True:

    gameover()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if not Game_Over:

        pygame.display.set_caption('Game')
        screen.blit(sfondo, (0,0))
        screen.blit(ground, ground_rect)
        player.update()
        player.draw(screen) 
    
    pygame.display.update()
    clock.tick(60)


