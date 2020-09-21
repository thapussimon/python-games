
# 1.26.24 Time

import pygame

from random import randint

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

# Player 1 X coordinate & Y coordinate
playerX = 370
playerY = 480

playerX_change = 0

# Enemy Player


enemyImg = pygame.image.load("enemy.png")
enemyX = randint(0, 780)
enemyY = randint(0, 150)
enemyX_change = 1
enemyY_change = 30

# Background Image

bgImg = pygame.image.load("background.jpg")

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 8

# Ready state You can't see the bullet on the screen
# Fire the bullet is moving
bulletState = "ready"


def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    #If the value of x & y is give directly it would be shot from the LHS, We need it to be shot from the exact middle
    screen.blit(bulletImg, (x+16 , y+10 )) #x+16, & y+10 is found out by playing with the nos, it is used to make the bullet come from the center


def player(x, y):
    screen.blit(playerImg, (x, y))  # Draw The player1 On The screen


def enemy(x, y):
    screen.blit(enemyImg, (x, y))  # Draw The Enemy On The screen


# Game Loop, If not Created The Screen would exit
running = True
while running:
    # This Takes RGB Values
    screen.fill((0, 0, 0))  # Fills The SCreen to The RGB Value
    screen.blit(bgImg, (0, 0))

    # Checking The events, We nee to check for the window closing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  ##CLosing The Window, This check if the user press X, The window gets closed

        # Player Movements Control Part
        # If Keystroke is pressed check for left or right
        if event.type == pygame.KEYDOWN:
            print("A Keystroke is Pressed")
            if event.key == pygame.K_LEFT:
                print("Left Arrow Pressed")
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                print("Right Arrow Pressed")
                playerX_change = 5
            if event.key==pygame.K_SPACE:
                print("Space is pressed")
                fire_bullet(playerX,bulletY)

        # Player Keystroke Control Part
        # Keystroke Release Checking
        if event.type == pygame.KEYUP:
            playerX_change = 0
            print("KEY released")
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key stroke has been Released")


    playerX += playerX_change  # Left and Right Movement of The player is fixed

    # Player Boundary CHecking To restrict The Movement

    if playerX < 0:
        playerX = 0
    elif playerX > 736:  # Since the png we have selected is 64 * 64,we have to subtract it from the 800 width which gives 736
        playerX = 736

    # Calling Player to draw The player on the screen
    player(playerX, playerY)
    # calling Enemy to draw The enemy on the screen
    enemy(enemyX, enemyY)

    # Enemy Setup= Boundary, Movement
    enemyX += enemyX_change

    if enemyX < 0:
        enemyX_change = 1.5
        enemyY += enemyY_change

    elif enemyX > 736:
        enemyX_change = -1.5
        enemyY += enemyY_change

    #Bullet Movement, FOr Persistence
    if bulletState=="fire":
        fire_bullet(playerX,bulletY)
        bulletY-=bulletY_change

    pygame.display.update()
