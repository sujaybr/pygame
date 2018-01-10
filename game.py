import pygame, sys
from pygame.locals import *
import math
pygame.init()
FPS = 30 
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((700,700), 0, 32)
pygame.display.set_caption('Hello world!')

catImg = pygame.image.load('invtri.png')

# to scale down the img
catImg = pygame.transform.scale(catImg, (150,150))
 # set up the colors
BLACK = ( 0, 0, 0 )
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0 )
BLUE = ( 0, 0, 255 )

LEN = 5 
def computeDistances(ang):
    xcom = LEN * math.cos(ang)
    ycom = LEN * math.sin(ang)

    return (xcom, ycom)
    

# These are the coordinates
ax = ay = 0
bx = by = 10
angle = 0
while True: 
    DISPLAYSURF.fill(RED)

    keys = pygame.key.get_pressed()
    if keys[K_d]:
        angle = (angle - 10) % 360 
    elif keys[K_a]:
        angle = (angle + 10) % 360
    elif keys[K_w]:
        tx, ty = computeDistances(math.radians(360 - angle))
        ax += tx
        ay += ty
    elif keys[K_s]:
        pass 
    elif keys[K_r]:
        pass
    # pygame.draw.rect(DISPLAYSURF, RED, (ax, ay, bx, by))

    print (ax, ay, angle)
    DISPLAYSURF.blit(pygame.transform.rotate(catImg, angle), (ax, ay))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)


