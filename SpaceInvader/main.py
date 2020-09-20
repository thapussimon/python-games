import pygame

# Initialize The pygame
pygame.init()

# Create The screen With 800px Height and 600px Width
screen = pygame.display.set_mode((800, 600))



#Title and Icon

pygame.display.set_caption("Space Invaders")

icon=pygame.image.load("ufo.png")

pygame.display.set_icon(icon)

#Game Loop, If not Created The Screen would exit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False ##CLosing The Window, This check if the user press X, The window gets closed


    #This Takes RGB Values
    screen.fill((0,0,0))
    pygame.display.update()
