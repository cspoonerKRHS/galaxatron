import pygame, sys, math, random

pygame.init()

from Potato import Potato
from Player import Player
from Slow_Time import SlowTime

clock = pygame.time.Clock()

width = 800
height = 600
size = width, height

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("images/backgrounds/startmenu.png")
bgRect = bgImage.get_rect()

bgColor = r,g,b = 0,0,0

ballp = Player(["images/player.png",], [3,3], [50,50], [width/2,height/2])

potatoes = [Potato([random.randint(3,3), random.randint(6,6)],  
              [random.randint(75, width-75), random.randint(75, height-75)])]
              
powerUps = []
              
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
    
    bgImage = pygame.image.load("images/backgrounds/basenoplanet.png")
    
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

        if random.randint(0,1000) == 0:   #1 in 60 chance
            powerUps += [SlowTime([random.randint(25, width-25), random.randint(25, height-25)])]
            
                    
        for potato in potatoes:
            potato.update()
        for powerUp in powerUps:
            powerUp.update()
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
        for powerUp in powerUps:
            if ballp.collidePowerUp(powerUp):
                if powerUp.type == "slow time":
                    for potato in potatoes:
                        potato.slowDown()
                
        deadcount= 0
        
        for powerUp in powerUps:
            if not powerUp.living:
                powerUps.remove(powerUp)
        
        for potato in potatoes:
            if not potato.living:
                deadcount += 1
                
        if len(potatoes) == deadcount:
            level += 1
            for potato in potatoes:
                potato.hit()
            potatoes += [Potato([random.randint(3,3), random.randint(6,6)],  
                                [random.randint(75, width-75), random.randint(75, height-75)])]
            
                          
        screen.blit(bgImage, bgRect)
        for powerUp in powerUps:
            screen.blit(powerUp.image, powerUp.rect)
        screen.blit(ballp.image, ballp.rect)
        for potato in potatoes:
            screen.blit(potato.image, potato.rect)
        pygame.display.flip()
        clock.tick(60)