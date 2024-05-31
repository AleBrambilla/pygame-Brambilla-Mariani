import pygame
from random import randint, choice
from player import Player
from piattaforme import Classica

pygame.init()
screen = pygame.display.set_mode((550, 800))
clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle()
player.add(Player())

piattaforme = pygame.sprite.Group()
for _ in range(6):
    piattaforme.add(Classica(randint(100, 700)))

altezze = [70, 200, 330, 460, 590, 720]
for i in range(6):
    piattaforme.sprites()[i].rect.centery = altezze[i]

listax1 = [350, 256, 440, 240, 72, 276]
listax2 = [344, 484, 284, 132, 264, 84]
listax3 = [200, 100, 320, 120, 240, 474]

listax = choice([listax1, listax2, listax3])
for i in range(6):
    piattaforme.sprites()[i].rect.centerx = listax[i]

player.sprite.rect.center = ((piattaforme.sprites()[-1].rect.centerx, altezze[-1]+70))
salta = True
player.sprite.gravity = 6
conta = 0
fase = 'animazione'
prossima = 5
sfondo = pygame.image.load('Brambilla-Mariani-img/sfondo.png').convert()
sfondo = pygame.transform.rotozoom(sfondo, 0, 1.1)

def anima_home():
    global fase, prossima, salta, listax, sfondo

    if fase == 'preparazione':
        
        for i in range(6):
            if piattaforme.sprites()[i].rect.centerx < listax[i]:
                piattaforme.sprites()[i].rect.centerx += 6

        for i in range(6):
            if piattaforme.sprites()[i].rect.centerx > listax[i]:
                piattaforme.sprites()[i].rect.centerx -= 6

        conta = 0
        for i in range(6):
            if piattaforme.sprites()[i].rect.centerx == listax[i]:
                conta += 1

        if conta == 6:
            fase = 'animazione'
            player.sprite.gravity = -24

    elif fase == 'animazione':
        for piattaforma in pygame.sprite.spritecollide(player.sprite, piattaforme, False):
            if player.sprite.rect.bottom > piattaforma.rect.top and player.sprite.rect.bottom < piattaforma.rect.bottom - 5 and player.sprite.gravity>5:
                salta = True
                for i,p in enumerate(piattaforme.sprites()):
                    piattaforme.sprites()[i].corrente=False

                piattaforma.corrente = True

        for i,p in enumerate(piattaforme.sprites()):
            if p.corrente == True:
                prossima = i-1

        if prossima < 6 and piattaforme.sprites()[prossima].rect.centerx > player.sprite.rect.centerx:
            player.sprite.rect.centerx += 6
            player.sprite.img = player.sprite.img_destra

        if prossima < 6 and piattaforme.sprites()[prossima].rect.centerx < player.sprite.rect.centerx:
            player.sprite.rect.centerx -= 6
            player.sprite.img = player.sprite.img_sinistra

        if player.sprite.rect.bottom < 0 and piattaforme.sprites()[0].corrente:
            listax = choice([listax1, listax2, listax3])
            player.sprite.rect.center = (listax[-1], 850)
            fase = 'preparazione'

        player.update(salta)
        salta = False
    
    screen.blit(sfondo, (0,0))
    piattaforme.draw(screen)    
    player.draw(screen)


