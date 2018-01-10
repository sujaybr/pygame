import pygame, sys
from pygame.locals import *
import math

pygame.init()
FPS = 10 
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((700,700), 0, 32)
pygame.display.set_caption('Hello world!')

catImg = pygame.image.load('cat.png')

 # set up the colors
BLACK = ( 0, 0, 0 )
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0 )
BLUE = ( 0, 0, 255 )

LEN = 10 

def computeDistances(ang):
    xcom = LEN * math.cos(ang)
    ycom = LEN * math.sin(ang)

    return (xcom, ycom)
    
# These are the coordinates
ax = ay = 350
bx = by = 30
angle = 0
while True: 
    DISPLAYSURF.fill(WHITE)

    keys = pygame.key.get_pressed()
    if keys[K_a]:
        angle = (angle - 30) % 360
    elif keys[K_d]:
        angle = (angle + 30) % 360
    elif keys[K_w]:
        tx, ty = computeDistances(math.radians(angle))
        ax += tx
        ay += ty
    elif keys[K_s]:
        pass 
    
    print (ax, ay, angle,3* math.sin(angle),3* math.cos(angle))
    pygame.draw.rect(DISPLAYSURF, RED, (ax, ay, bx, by))

    # DISPLAYSURF.blit(pygame.transform.rotate(catImg, angle), (ax, ay))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)

def draw(ax,ay):
    pygame.draw.rect(DISPLAYSURF, RED, (ax, ay, 30, 30))
    return 0 
