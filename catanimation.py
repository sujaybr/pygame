#! /usr/bin/env python
# -*- coding: utf-8 -*-
# File              : dev/python/pygame/catanimation.py
# Author            : Sujay <sujaybr9@gmail.com>
# Date              : 03.01.2018
# Last Modified Date: 07.01.2018
# Last Modified By  : Sujay <sujaybr9@gmail.com>

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30    # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
catImg = pygame.image.load('cat.png')
catx = 0
caty = 0
# ax = ay = 0
# bx = by = 0

direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    # if direction == 'right':
    #     catx += 5
    #     if catx == 280:
    #         direction = 'down'
    # elif direction == 'down':
    #     caty += 5
    #     if caty == 220:
    #         direction = 'left'
    # elif direction == 'left':
    #     catx -= 5
    #     if catx == 10:
    #         direction = 'up'
    # elif direction == 'up':
    #     caty -= 5
    #     if caty == 10:
    #         direction = 'right' 
    catx += 5
    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
