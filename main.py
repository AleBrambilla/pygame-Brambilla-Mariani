import pygame
from sys import exit

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        salto_alto = pygame.image.load('Brambilla-Mariani-img/salto in alto.png').convert_alpha()
        salto_alto = pygame.transform.rotozoom(salto_alto, 0, 0.5)
        salto_basso = pygame.image.load('Brambilla-Mariani-img/salto in basso.png').convert_alpha()
        salto_basso = pygame.transform.rotozoom(salto_basso, 0, 0.5)
        salti = [salto_alto, salto_basso]
        ind_salti = 1

        self.image = salti[ind_salti]
        self.rect = self.image.get_rect(midbottom = (275,700))
        self.gravity = 0

    def salto(self):
        if self.rect.bottom >= 700:
            self.gravity = -22

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 700:
            self.rect.bottom = 700

    def movimento(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 6
        if keys[pygame.K_RIGHT]:
            self.rect.x += 6
        
    def update(self):
        self.salto()
        self.apply_gravity()
        self.movimento()

WINDOW_SIZE = (550, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
sfondo = pygame.image.load('Brambilla-Mariani-img/sfondo.png').convert()
ground = pygame.image.load('Brambilla-Mariani-img/ground.png').convert()

player = pygame.sprite.GroupSingle()
player.add(Player())

pygame.display.set_caption('Home')

clock = pygame.time.Clock()
fps = 60

keys=pygame.key.get_pressed()

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
