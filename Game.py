import pygame, sys, math

pygame.init()

from Ball import Ball
from Player import Player

clk = pygame.time.Clock()

width = 640
height = 480
size = width, height

screen = pygame.display.set_mode(size)
bgColor = r,g,b = 0,0,0

ball1 = Ball(["ball1.png", "ball2.png"], (5,2), (width/2, height/2), (75,75))
ball2 = Ball(["ball1.png", "ball2.png"], (2,5), (width/3, height/3), (125,125))
ball3 = Ball(["ball1.png", "ball2.png"], (4,7), (450, 125), (100,100))
ball4 = Ball(["ball1.png", "ball2.png"], (3,5), (500, 300), (200,200))

pBall = Player("player.png", (3,3), (550,150), (50,50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                pBall.direction("right")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                pBall.direction("left")
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                pBall.direction("up")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                pBall.direction("down")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                pBall.direction("stop right")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                pBall.direction("stop left")
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                pBall.direction("stop up")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                pBall.direction("stop down")
    
    ball1.update()
    ball2.update()
    ball3.update()
    ball4.update()
    pBall.update()
    
    
    ball1.wallBounce(width, height)
    ball2.wallBounce(width, height)
    ball3.wallBounce(width, height)
    ball4.wallBounce(width, height)
    pBall.wallBounce(width, height)
    
    
    ball1.collideBall(ball2)
    ball1.collideBall(ball3)
    ball1.collideBall(ball4)
    ball2.collideBall(ball3)
    ball2.collideBall(ball4)
    ball3.collideBall(ball4)
    
    pBall.collideBall(ball1)
    pBall.collideBall(ball2)
    pBall.collideBall(ball3)
    pBall.collideBall(ball4)
    
    screen.fill(bgColor)
    screen.blit(ball1.image, ball1.rect)
    screen.blit(ball2.image, ball2.rect)
    screen.blit(ball3.image, ball3.rect)
    screen.blit(ball4.image, ball4.rect)
    screen.blit(pBall.image, pBall.rect)
    pygame.display.flip()
    clk.tick(60)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














