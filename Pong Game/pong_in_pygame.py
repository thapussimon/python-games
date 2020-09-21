import pygame

# Initialization
pygame.init()

# Windows setting
wn = pygame.display.set_mode((800, 600))
# Title
pygame.display.set_caption("Pong Game by Thapus Simon")

# Icon

icon = pygame.image.load("ping-pong.png")
pygame.display.set_icon(icon)

# Paddle A

player_A_Img = pygame.image.load("player1.png")
player_A_X = 0
player_A_Y = 280
player_A_change = 0



#Paddle B
player_B_Img=pygame.image.load("player2.png")
player_B_X=730
player_B_Y=280
player_B_change=0



#Drawing The paddle A on the screen
def playerA(x, y):
    wn.blit(player_A_Img, (x, y))

#Drawing The Player Bon the screen
def playerB(x,y):
    wn.blit(player_B_Img,(x,y))

run = True
while run:
    # Filling The SCreen With Black Color
    wn.fill((0, 0, 0))

    # Checking for events
    for events in pygame.event.get():

        # Checking If The window is closed
        if events.type == pygame.QUIT:
            run = False

        # Paddle A Movement
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                player_A_change = -0.5
            if events.key == pygame.K_RIGHT:
                player_A_change = 0.5
        if events.type == pygame.KEYUP:
            player_A_change = 0

    if player_A_Y < 18:
        player_A_Y = 18
    elif player_A_Y > 518:
        player_A_Y = 518

    player_A_Y += player_A_change
    playerA(player_A_X, player_A_Y)
    playerB(player_B_X,player_B_Y)
    pygame.display.update()
