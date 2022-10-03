import pygame
import sys
pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

posY_block1 = 150
posY_block2 = 150
posX_circle = 450
posY_circle = 250

circle_right = True
circle_top = True

speed = 3

screenWidth = 900
screenHeight = 500

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Пинг-понг')
pygame.display.set_icon(pygame.image.load('../ball.png'))

score1 = 0
score2 = 0

clock = pygame.time.Clock()

while True:
    clock.tick(130)

    screen.fill(BLACK)

    f = pygame.font.SysFont('Verdana', 15)
    f_finish = pygame.font.SysFont('Verdana', 50)
    sc_score1 = f.render(f'Счет 1 игрока: {score1}', True, WHITE)
    sc_score2 = f.render(f'Счет 2 игрока: {score2}', True, WHITE)
    game_over = f_finish.render('GAME OVER', True, WHITE)
    pos_score2 = sc_score2.get_rect(topright=(860, 40))
    pos_game_over = game_over.get_rect(center=(screenWidth//2, screenHeight//2))
    screen.blit(sc_score1, (40, 40))
    screen.blit(sc_score2, pos_score2)

    if score1 == 5 or score2 == 5:
        screen.blit(game_over, pos_game_over)

    block1 = pygame.draw.rect(screen, GREEN, (0, posY_block1, 20, 100))
    block2 = pygame.draw.rect(screen, GREEN, (880, posY_block2, 20, 100))

    pygame.draw.circle(screen, YELLOW, (posX_circle, posY_circle), 20)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        if posY_block2 > 0:
            posY_block2 -= speed
    elif pressed[pygame.K_DOWN]:
        if posY_block2 + 100 < screenHeight:
            posY_block2 += speed

    if pressed[pygame.K_w]:
        if posY_block1 > 0:
            posY_block1 -= speed
    elif pressed[pygame.K_s]:
        if posY_block1 + 100 < screenHeight:
            posY_block1 += speed

    if posY_circle - 20 <= 0:
        circle_top = False
    elif posY_circle + 20 >= screenHeight:
        circle_top = True

    if circle_right:
        posX_circle += speed
    else:
        posX_circle -= speed

    if circle_top:
        posY_circle -= speed
    else:
        posY_circle += speed

    if posY_block1 <= posY_circle <= posY_block1 + 100 and 20 >= posX_circle - 20 >= 0:
        circle_right = True
    elif posX_circle == 0:
        score1 += 1
        if score1 < 5:
            posX_circle = 450
            posY_circle = 250

    if posY_block2 <= posY_circle <= posY_block2 + 100 and screenWidth - 20 <= posX_circle + 20 <= screenWidth:
        circle_right = False
    elif posX_circle == screenWidth:
        score2 += 1
        if score2 < 5:
            posX_circle = 450
            posY_circle = 250

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()