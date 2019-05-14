import pygame
import sys
import random
import math

from pygame.locals import *
pygame.init()



WIDTH = 500
HEIGHT = WIDTH
BACKGROUND = (0,0,0)
dotR = 1
WHITE = (255,255,255)

r = int(WIDTH/2)
inCirc = 0.0
total = 0.0
ratio = 0.0
recordPI = -1.0;
recordDiff = 100;

pygame.display.set_caption("PI guestimator!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill(BACKGROUND)

pygame.draw.circle(screen, (255,0,0), (r, r), r, 1)
pygame.display.update()
iter = 1
noChange = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    rX = float(random.randint(0,r))
    rY = float(random.randint(0,r))
    rInt = random.randint(0,1)

    if rInt == 0:
        rX *= -1

    rInt = random.randint(0,1)
    if rInt == 0:
        rY *= -1

    if(float(rX*rX + rY*rY) < float(r*r)):
        inCirc+=1.0
    total+=1.0
    noChange += 1
    if noChange > 10000:
        noChange = 0
        total = 0
        inCirc = 0
        screen.fill(BACKGROUND)
        pygame.draw.circle(screen, (255,0,0), (r, r), r, 1)
        pygame.display.update()
        iter+=1



    if (total-inCirc) != 0:
        ratio = float(inCirc)/float(total-inCirc)
        if(abs(ratio-math.pi) < recordDiff):
            noChange = 0
            recordPI = ratio
            recordDiff = float(abs(ratio - math.pi))
            print(ratio)
            print("log err: " + str(math.log10(recordDiff)))
            print("iteration: " + str(iter))
    if(rX < 0):
        rX += 2*r
    if(rY < 0):
        rY += 2*r

    pygame.draw.rect(screen, WHITE, (rX, rY, 1, 1))
    pygame.display.update()
