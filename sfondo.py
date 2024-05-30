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

player.sprite.rect.center = ((piattaforme.sprites()[-1].rect.centerx, altezze[-1]+70))
prossima = 5
salta = True
player.sprite.gravity = 6

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
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
        player.sprite.rect.centery = altezze[-1]+10

    screen.fill((0,200,250))
    piattaforme.draw(screen)
    player.update(salta)
    player.draw(screen)

    salta = False

    pygame.display.update()
    clock.tick(60)

