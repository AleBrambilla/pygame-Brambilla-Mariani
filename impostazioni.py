import pygame

def init_impostazioni(screen, variabili):
    
    screen.fill((0,200,250))

    font=pygame.font.Font(None, 60)
    Temp=font.render('Temporanea', False, (0,0,0))
    Mob_y=font.render('Saliscendi', False, (0,0,0))
    Mob_x=font.render('Mobile', False, (0,0,0))
    Cad=font.render('Cadente', False, (0,0,0))

    screen.blit(Temp, (100, 200))
    screen.blit(Cad, (100, 350))
    screen.blit(Mob_x, (100, 500))
    screen.blit(Mob_y, (100,650))

    font=pygame.font.Font(None, 100)
    screen.blit(font.render('IMPOSTAZIONI', False, (0,0,255)), (30, 80))

    l=[pygame.Surface((50, 50)) for _ in range(4)]
    rect=[l[i].get_rect(topleft=(460, 200+150*i)) for i in range(4)]

    for i in range(len(l)):
        l[i].fill((255,0,0))

    for i in range(4):
        if variabili[i]:
            l[i].fill((0,190,0))
            rect[i].x=400 
        screen.blit(l[i], rect[i])

    return rect

def change(bool):
    if bool:
        bool=False
    else:
        bool=True
    return bool