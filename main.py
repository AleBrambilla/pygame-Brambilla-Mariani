import pygame
from pygame.locals import *
from sys import exit
from random import randint, choice

from player import Player
from piattaforme import Piattaforma, bool_scorrere
from punteggio import Punteggio

pygame.init()

def gameover():

    global Game_Over, mouse, tasti_mouse

    mouse=pygame.mouse.get_pos()
    tasti_mouse=pygame.mouse.get_pressed()

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

    

    if Game_Over:

        screen.blit(tasto_start, start_rect)
        screen.blit(inizio, inizio_rect)
        screen.blit(titolo, titolo_rect)

        if start_rect.collidepoint(mouse) and tasti_mouse[0]:
            Game_Over=False

    if player.sprite.rect.y>800:
        Game_Over=True
    
def collisions():
    global inizio
    
    if pygame.sprite.spritecollide(player.sprite, piattaforme, False) or inizio: 
        ris= True
    else:
        ris=False

    if pygame.sprite.spritecollide(player.sprite, piattaforme, False):
        inizio=False
        
    if not inizio:
        ground_rect.y+=3

    return ris

WINDOW_SIZE = (550, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo = pygame.image.load('Brambilla-Mariani-img/sfondo.png').convert()
ground = pygame.image.load('Brambilla-Mariani-img/ground.png').convert()
ground_rect=ground.get_rect(topleft=(0, 700))

player = pygame.sprite.GroupSingle()
player.add(Player())

piattaforme = pygame.sprite.Group()
piattaforme.add(Piattaforma(randint(500, 600)))

punteggio=Punteggio()

pygame.display.set_caption('Home')

clock = pygame.time.Clock()
fps = 50


global Game_Over, inizio

Game_Over=True
inizio=True

while True:

    mouse=pygame.mouse.get_pos()
    tasti_mouse=pygame.mouse.get_pressed()
    #print(mouse, tasti_mouse)

    gameover()

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if not Game_Over:

        pygame.display.set_caption('Game')
        screen.blit(sfondo, (0,0))
        screen.blit(ground, ground_rect)

        salta=collisions() 
        
        
        if piattaforme.sprites()[-1].rect.y > 0:
            piattaforme.add(Piattaforma(piattaforme.sprites()[-1].rect.y + randint(-200, -150)))

        piattaforme.draw(screen)
        player.update(salta)
        player.draw(screen)


        if bool_scorrere(piattaforme, player):
            for piattaforma in piattaforme:
                piattaforma.scorri()
    
        punteggio.update(piattaforme, player)
        punteggio.draw(screen)

    


    pygame.display.update()
    clock.tick(60)


