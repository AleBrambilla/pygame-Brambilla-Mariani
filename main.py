import pygame
from pygame.locals import *
from sys import exit
from random import randint, choice

from player import Player
from piattaforme import Piattaforma, bool_scorrere
from punteggio import Punteggio

pygame.init()

tasto_start=pygame.Surface((200, 100))
tasto_start.fill((255,255,255))
start_rect=tasto_start.get_rect(center=(275, 550))
        
font=pygame.font.Font(None, 50)
inizio_scritta=font.render('INIZIO', True, (0,0,0))
inizio_scritta_rect=inizio_scritta.get_rect(center=(275, 550))

font=pygame.font.Font(None, 150)
titolo=font.render('TITOLO', True, (100,255,0))
titolo_rect=titolo.get_rect(midtop=(275, 50))

def gameover():

    global Game_Over, inizio

    screen.fill((0,200,250))

    if Game_Over:   # non è bello come game_over diventa true

        screen.blit(tasto_start, start_rect)
        screen.blit(inizio_scritta, inizio_scritta_rect)
        screen.blit(titolo, titolo_rect)

    if start_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        Game_Over=False

    if player.sprite.rect.y>800:
        Game_Over=True
        inizio=True
    
def collisions():
    global inizio
    
    for piattaforma in pygame.sprite.spritecollide(player.sprite, piattaforme, False):
        if player.sprite.rect.bottom > piattaforma.rect.top and player.sprite.rect.bottom < piattaforma.rect.bottom - 5:
            inizio=False
            for i,p in enumerate(piattaforme.sprites()):
                piattaforme.sprites()[i].corrente=False
            piattaforma.corrente = True
            return True
        
    if player.sprite.rect.bottom>=ground_rect.top:
        inizio = True
        return True
    
    return False

WINDOW_SIZE = (550, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo = pygame.image.load('Brambilla-Mariani-img/sfondo.png').convert()
sfondo = pygame.transform.rotozoom(sfondo, 0, 1.1)

ground = pygame.image.load('Brambilla-Mariani-img/ground.png').convert()
ground_rect=ground.get_rect(topleft=(0, 700))

player = pygame.sprite.GroupSingle()
player.add(Player())

piattaforme = pygame.sprite.Group()
piattaforme.add(Piattaforma(randint(500, 600)))

punteggio=Punteggio()

pygame.display.set_caption('Home')

clock = pygame.time.Clock()


Game_Over=True
inizio=True


while True:

#    cominciare(inizio)
    gameover()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if Game_Over:

            if event.type==MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and start_rect.collidepoint(pygame.mouse.get_pos()):
                Game_Over=False
                ground_rect.y = 700
                piattaforme.empty()
                piattaforme.add(Piattaforma(randint(500, 600)))
                player.sprite.rect.midbottom = (275,700)
                punteggio=Punteggio()
                inizio=True
            if event.type== KEYUP and Game_Over and event.key==K_SPACE:
                inizio=True

    if not Game_Over:

        pygame.display.set_caption('Game')
        screen.blit(sfondo, (0,0))
        screen.blit(ground, ground_rect)
        
        if piattaforme.sprites()[-1].rect.y > 0:
            piattaforme.add(Piattaforma(piattaforme.sprites()[-1].rect.y + randint(-200, -150)))
            
        salta=collisions()
        piattaforme.draw(screen)
        player.update(inizio, salta)
        salta = False
        player.draw(screen)

        if bool_scorrere(piattaforme, player)  and not inizio:
            ground_rect.y+=3
            player.sprite.rect.y+=3
            for piattaforma in piattaforme:
                piattaforma.scorri()
    
        punteggio.update(piattaforme, player, inizio)
        punteggio.draw(screen)

    elif Game_Over and not inizio:
        punteggio.draw_finale(screen)

    pygame.display.update()
    clock.tick(60)
    

