import pygame
from pygame.locals import *
from sys import exit
from random import randint, choice

from player import Player
from piattaforme import Cadente, Classica, Mobile_x, Mobile_y, Temporanea, bool_scorrere, platform_list
from punteggio import Punteggio

pygame.init()
   
def collisions():
    global inizio
    
    for piattaforma in pygame.sprite.spritecollide(player.sprite, piattaforme, False):
        if player.sprite.rect.bottom > piattaforma.rect.top and player.sprite.rect.bottom < piattaforma.rect.bottom - 5:
            inizio=False
            for i,p in enumerate(piattaforme.sprites()):
                piattaforme.sprites()[i].corrente=False
                if type(piattaforma) == Cadente and player.sprite.gravity>5:
                    piattaforma.cadi = True
                    player.sprite.salto()

            piattaforma.corrente = True
            return True
        
    if player.sprite.rect.bottom>=ground_rect.top:
        inizio = True
        return True
    
    return False

def inizializza():
    global punteggio, inizio
    ground_rect.y = 700
    piattaforme.empty()
    piattaforme.add(Classica(randint(500, 600)))
    player.sprite.rect.midbottom = (275,700)
    punteggio=Punteggio()
    inizio=True

def immagini():

    global tasto_start, start_rect, font, inizio_scritta, inizio_scritta_rect, titolo1, titolo_rect1, titolo2, titolo_rect2, tasto_start2, start_rect2, inizio_scritta2, inizio_scritta_rect2, restart, restart_rect, image_piattaforma, ground, ground_rect, sfondo, lava, lava_rect
    tasto_start=pygame.Surface((200, 100))
    tasto_start.fill((255,255,255))
    start_rect=tasto_start.get_rect(center=(275, 420))
            
    font=pygame.font.Font(None, 50)
    inizio_scritta=font.render('CLASSIC', True, (0,0,0))
    inizio_scritta_rect=inizio_scritta.get_rect(center=(275, 420))

    font=pygame.font.SysFont('Cooper Black', 30)
    titolo1=font.render("Ale&Davi's", False, (26,128,5))
    titolo_rect1=titolo1.get_rect(midtop=(275, 50))

    font=pygame.font.SysFont('Cooper Black', 90)
    titolo2=font.render("PLATFORM", False, (26,128,5))
    titolo_rect2=titolo2.get_rect(midtop=(275, 130))

    tasto_start2=pygame.Surface((200, 100))
    tasto_start2.fill((255,255,255))
    start_rect2=tasto_start2.get_rect(center=(275, 600))
            
    font=pygame.font.Font(None, 50)
    inizio_scritta2=font.render('RUN MODE', True, (0,0,0))
    inizio_scritta_rect2=inizio_scritta2.get_rect(center=(275, 600))

    restart=font.render('RESTART', True, (0,0,0))
    restart_rect=inizio_scritta_rect

    sfondo = pygame.image.load('Brambilla-Mariani-img/sfondo.png').convert()
    sfondo = pygame.transform.rotozoom(sfondo, 0, 1.1)

    image_piattaforma=pygame.image.load('Brambilla-Mariani-img/platform.png').convert_alpha()
    image_piattaforma=pygame.transform.rotozoom(image_piattaforma, 30, 0.7)

    ground = pygame.image.load('Brambilla-Mariani-img/ground.png').convert()
    ground_rect=ground.get_rect(topleft=(0, 700))

    lava=pygame.image.load('Brambilla-Mariani-img/lava.png').convert_alpha()
    lava=pygame.transform.rotozoom(lava, 0, 1.5)
    lava_rect=lava.get_rect(center=(275, 730))

def RunMode_init():
    global punteggio, t_inizio, inizio
    lava_rect.centery = 730

    t_inizio=pygame.time.get_ticks()

    prima=Classica(350)
    prima.rect.centerx=275
    piattaforme.empty()
    piattaforme.add(prima)

    player.sprite.rect.midbottom = (275,300)
    punteggio=Punteggio()
    inizio=True


WINDOW_SIZE = (550, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)

immagini()

player = pygame.sprite.GroupSingle()
player.add(Player())

piattaforme = pygame.sprite.Group()
piattaforme.add(Classica(randint(500, 600)))

punteggio=Punteggio()

pygame.display.set_caption('Home')

clock = pygame.time.Clock()

stato = 'home'

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    if stato == 'home':
        screen.fill((0,200,250))
        screen.blit(tasto_start, start_rect)
        screen.blit(inizio_scritta, inizio_scritta_rect)
        screen.blit(titolo1, titolo_rect1)
        screen.blit(titolo2, titolo_rect2)
        screen.blit(tasto_start2, start_rect2)
        screen.blit(inizio_scritta2, inizio_scritta_rect2)
        screen.blit(pygame.transform.rotozoom(player.sprite.image, 0, 1.3), (25, 550))
        screen.blit(image_piattaforma, (400, 350))

        if start_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            stato = 'classico'
            inizializza()
        if start_rect.collidepoint(pygame.mouse.get_pos()) and event.type== KEYUP and event.key==K_KP_ENTER:
            stato = 'classico'
            inizializza()

        if start_rect2.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            stato = 'run mode'
            RunMode_init()

        #print(stato)
        if start_rect2.collidepoint(pygame.mouse.get_pos()) and event.type== KEYUP and event.key==K_KP_ENTER:
            stato = 'run mode'
            RunMode_init()

    if stato == 'classico':
        
        pygame.display.set_caption('Classic Mode')
        screen.blit(sfondo, (0,0))
        screen.blit(ground, ground_rect)
        
        if piattaforme.sprites()[-1].rect.y > 0:
            pos=piattaforme.sprites()[-1].rect.y + randint(-200, -150)
            l=platform_list(pos, punteggio.ammontare)
            piattaforme.add(choice(l))
            
        salta=collisions()
        piattaforme.draw(screen)
        player.update(inizio, salta)
        salta = False
        player.draw(screen)

        if bool_scorrere(piattaforme) and not inizio:
            ground_rect.y+=5
            player.sprite.rect.y+=5
            for piattaforma in piattaforme:
                piattaforma.scorri()

        for piattaforma in piattaforme:   
            piattaforma.update()
    
        punteggio.update(piattaforme, player, inizio)
        punteggio.draw(screen)

        if player.sprite.rect.y>800:
            stato_precedente='classico'
            stato = 'morte'
            inizio=True

    elif stato == 'morte':
        punteggio.draw_finale(screen)

        screen.blit(tasto_start, start_rect)
        screen.blit(restart, restart_rect)
        if event.type== KEYUP and event.key==K_SPACE:
            stato = 'home'
        if start_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            stato = stato_precedente
            if stato=='classico':
                inizializza()
            else:
                RunMode_init()

    elif stato == 'run mode':

        pygame.display.set_caption('Run Mode')
        screen.blit(sfondo, (0,0))
        screen.blit(lava, lava_rect)

        VEL_AVANZ=1+(pygame.time.get_ticks()-t_inizio)//15000

        if piattaforme.sprites()[-1].rect.y > 0:
            pos=piattaforme.sprites()[-1].rect.y + randint(-200, -150)
            l=platform_list(pos, punteggio.ammontare)
            piattaforme.add(choice(l))
        piattaforme.draw(screen)
        
        salta=collisions()
        player.update(inizio, salta)
        player.draw(screen)

        for piattaforma in piattaforme:   
            piattaforma.update()
            piattaforma.rect.y+=VEL_AVANZ
            if type(piattaforma) == Mobile_y or type(piattaforma) == Cadente:
                piattaforma.centro+=VEL_AVANZ

    
        punteggio.RunMode(VEL_AVANZ)
        punteggio.draw(screen)

        if lava_rect.colliderect(player.sprite.rect):
            stato_precedente='run mode'
            stato = 'morte'
            inizio=True

    pygame.display.update()
    clock.tick(60)
    

