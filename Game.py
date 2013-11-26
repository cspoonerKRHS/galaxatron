import pygame, sys, math, random

pygame.init()

from Potato import Potato
from Player import Player

clock = pygame.time.Clock()

width = 640
height = 480
size = width, height

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("images/background.png")
bgRect = bgImage.get_rect()

bgColor = r,g,b = 0,0,0

ballp = Player(["images/player.png",], [3,3], [50,50], [width/2,height/2])

potatoes = [Potato([random.randint(-2,2), random.randint(-5,5)],  
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
    
    bgImage = pygame.image.load("images/background.png")
    
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

        for potato in potatoes:
            potato.update()
        ballp.update()        
        
        for potato in potatoes:
            potato.collideWall(width, height)
        ballp.collideWall(width, height)
        
        if len(potatoes) > 1:
            for first in range(len(potatoes)-1):
                for second in range(first+1,len(potatoes)):
                    potatoes[first].collideBall(potatoes[second])
        
        for potato in potatoes:
            ballp.collideBall(potato)
                
        deadcount= 0
        for potato in potatoes:
            if not potato.living:
                deadcount += 1
                
        if len(potatoes) == deadcount:
            level += 1
            for potato in potatoes:
                potato.hit()
            potatoes += [Potato([random.randint(-2,2), random.randint(-5,5)],  
                                [random.randint(75, width-75), random.randint(75, height-75)])]
            
                          
        screen.blit(bgImage, bgRect)
        screen.blit(ballp.image, ballp.rect)
        for ball in potatoes:
            screen.blit(ball.image, ball.rect)
        pygame.display.flip()
        clock.tick(60)