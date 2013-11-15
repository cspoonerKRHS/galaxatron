import pygame, sys, math, random

pygame.init()

from Potato import Potato
from Player import Player

clock = pygame.time.Clock()

width = 640
height = 480
size = width, height

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("rsc/bg/startbg.png")
bgRect = bgImage.get_rect()

bgColor = r,g,b = 0,0,0

ballp = Player(["images/player",], [3,3], [50,50], [width/2,height/2])

bsize = random.randint(25, 150)
balls = [Potato("images/potato", 
              [random.randint(-5,5), random.randint(-5,5)], 
              [bsize, bsize], 
              [random.randint(75, width-75), random.randint(75, height-75)])]
              
start = False
while True:
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
        
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)
    
    bgImage = pygame.image.load("rsc/bg/mainbg.png")
    
    level = 1
    
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    ballp.direction("right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    ballp.direction("left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    ballp.direction("up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    ballp.direction("down")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    ballp.direction("stop right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    ballp.direction("stop left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    ballp.direction("stop up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    ballp.direction("stop down")

        for ball in balls:
            ball.update()
        ballp.update()        
        
        for ball in balls:
            ball.collideWall(width, height)
        ballp.collideWall(width, height)
        
        if len(balls) > 1:
            for first in range(len(balls)-1):
                for second in range(first+1,len(balls)):
                    balls[first].collideBall(balls[second])
        
        for ball in balls:
            ballp.collideBall(ball)
            
        for ball in balls:
            if not ball.living:
                balls.remove(ball)
                
        
        if len(balls) == 0:
            level += 1
            for i in range(level):
                print i
                bsize = random.randint(25, 150)
                balls += [Ball("rsc/enemy/ball.png", 
                              [random.randint(-5,5), random.randint(-5,5)], 
                              [bsize, bsize], 
                              [random.randint(75, width-75), random.randint(75, height-75)])]
                          
        screen.blit(bgImage, bgRect)
        screen.blit(ballp.image, ballp.rect)
        for ball in balls:
            screen.blit(ball.image, ball.rect)
        pygame.display.flip()
        clock.tick(60)
                








