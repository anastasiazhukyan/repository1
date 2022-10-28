import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255,255,255))
circle(screen, (255, 255, 0), (200, 175), 100)

rect(screen, (0, 0, 0), (170, 190, 80, 20))
circle(screen, (255, 0, 0), (150, 150), 20)
circle(screen, (0, 0, 0), (150, 150), 10)
circle(screen, (255, 0, 0), (250, 150), 20)
circle(screen, (0, 0, 0), (250, 150), 10)
polygon(screen, (0, 0, 0), [(120,100), (110,120),
                               (170,140), (180,130)])

polygon(screen, (0, 0, 0), [(210,150), (220,130),
                               (260,100), (270,120)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()