import pygame
from pygame.locals import *

size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)

pygame.init()
running = True
# set window size
screen = pygame.display.set_mode(size)
#set window title
pygame.display.set_caption("Car Game")
#set color
screen.fill((60, 220, 0))

#draw graphics - road
pygame.draw.rect(
    screen,
    (50,50,50),
    (width/2- road_w/2, 0, road_w, width)
)
  # draw centre line
pygame.draw.rect(
    screen,
    (255, 240, 60),
    (width/2 - roadmark_w/2, 0, roadmark_w, height))

# apply changes
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False     

pygame.quit()