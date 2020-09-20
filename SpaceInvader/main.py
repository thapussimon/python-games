import pygame

# Initialize The pygame
pygame.init()

# Create The screen With 600px Height and 800px Width (W*H) form
screen = pygame.display.set_mode((800, 600))

# Title and Icon

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("ufo.png")

pygame.display.set_icon(icon)

# Player Image

playerImg = pygame.image.load("player.png")

playerX = 370
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))  # Draw The player On The screen


# Game Loop, If not Created The Screen would exit
running = True
while running:
    # This Takes RGB Values
    screen.fill((0, 0, 0)) # Fills The SCreen to The RGB Value

    #Checking The events, We nee to check for the window closing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  ##CLosing The Window, This check if the user press X, The window gets closed




    player()
    pygame.display.update()
