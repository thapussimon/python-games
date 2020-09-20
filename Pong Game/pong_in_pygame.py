import pygame

pygame.init()

wn = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong Game by Thapus Simon")

run = True
while run:

    wn.fill((0,0,0))

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False


