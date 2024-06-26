from typing import Any
import pygame
from pygame.locals import *
from random import randint

pygame.init()

class Piattaforma(pygame.sprite.Sprite):
    def __init__(self, y):
        global image
        image=pygame.image.load('Brambilla-Mariani-img/platform.png').convert_alpha()
        super().__init__()

        self.image=image
        self.image = pygame.transform.rotozoom(self.image, 0, 0.8)
        self.rect=self.image.get_rect(topleft=(randint(0,400), y))
        self.corrente=False
        #print(y)

    def scorri(self):
        self.rect.y+=5
        if type(self) == Mobile_y or type(self) == Cadente:
            self.centro+=5
            
class Classica(Piattaforma):
    def __init__(self, y):
        super().__init__(y)
    def update(self):
        pass

class Mobile_x(Piattaforma):
    def __init__(self, y):
        super().__init__(y)
        self.delta=randint(50,200)
        self.centro=self.rect.centerx
        self.direzione=-1
    
    def update(self):
        self.rect.x+=self.direzione*3
        if self.rect.centerx < self.centro - self.delta: self.direzione = 1
        if self.rect.centerx > self.centro + self.delta: self.direzione = -1

class Mobile_y(Piattaforma):
    def __init__(self, y):
        super().__init__(y)
        self.delta=randint(50,100)
        self.centro=self.rect.centery
        self.direzione=-1
    
    def update(self):
        self.rect.y+=self.direzione*3
        if self.rect.centery < self.centro - self.delta: self.direzione = 1
        if self.rect.centery > self.centro + self.delta: self.direzione = -1
 
class Cadente(Piattaforma):
    def __init__(self, y):
        super().__init__(y)
        self.gravity = 0
        self.cadi=False

        self.delta= 2
        self.centro=self.rect.centery
        self.direzione=-1
        
    def update(self):
        self.rect.y+=self.direzione*4
        if self.rect.centery < self.centro - self.delta: self.direzione = 1
        if self.rect.centery > self.centro + self.delta: self.direzione = -1
        self.apply_gravity()

    def apply_gravity(self):
        if self.cadi:
            self.gravity += 1
            self.rect.y += self.gravity

class Temporanea(Piattaforma):
    def __init__(self, y):
        super().__init__(y)
        self.frames=0
        self.x=self.rect.x
        self.image=pygame.transform.rotozoom(self.image, 180, 1)

    def update(self):
        self.frames+=1
        if self.frames>100:
            self.rect.x=1000
        else:
            self.rect.x=self.x

        if self.frames>200:
            self.frames=0

def bool_scorrere(piattaforme):

    scorri=True
    for piattaforma in piattaforme.sprites(): 
        if piattaforma.rect.top >=600 and piattaforma.corrente:
            scorri=False

    return scorri

def platform_list(pos, score , bool):
   l=[Classica(pos) for _ in range(3)]
   if score>200 and bool[1]:
       l.append(Cadente(pos))
   if score>300 and bool[3]:
       l.append(Mobile_y(pos))
   if score>500 and bool[2]:
       l.append(Mobile_x(pos))
   if score>700 and bool[0]:
       l.append(Temporanea(pos))
   if score>1000:
       l.pop(0)                          

   return l
