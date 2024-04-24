import pygame as x, sys
import pygame.display
from pygame.locals import *

WINDOW_SIZE = (1000, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Home')

clock = pygame.time.Clock()
fps = 60

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()