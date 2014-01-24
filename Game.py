import pygame, sys, math, random, time

pygame.init()

from Potato import Potato
from Player import Player
from Slow_Time import SlowTime
from Speed_Time import SpeedTime
from Button import Button

clock = pygame.time.Clock()
altFlag = False
fullscreen = 0


width = 800
height = 600
size = width, height

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("Images/backgrounds/startmenu.png")
bgRect = bgImage.get_rect()

bgColor = r,g,b = 0,0,0

startbutton = Button("Images/backgrounds/startbutton.png", [width/2, height/2], [250, 100])

keyboardoption = Button("Images/backgrounds/mousebutton.png", [0, 0], [250, 100])

player = Player(["Images/Player.png",], [5,5], [50,50], [width/2,height/2])

potatoes = [Potato([random.randint(3,3), random.randint(6,6)],  
              [random.randint(75, width-75), random.randint(75, height-75)])]
              
powerUps = []
              
start = False
cutScreen = False
level = 0
while True:
    while not start and not cutScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
                    cutScreen = True
                    level = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startbutton.collidePoint(event.pos):
                
                    start = True
                    cutScreen = True
                    level = 1
        
        screen.blit(bgImage, bgRect)
        screen.blit(startbutton.image, startbutton.rect)
        screen.blit(keyboardoption.image, keyboardoption.rect)
        pygame.display.flip()
        clock.tick(60)
    
    bgImage = pygame.image.load("Images/backgrounds/basenoplanet.png")
    
    while start and cutScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or (event.key == pygame.K_RETURN and not altFlag):
                    cutScreen = False
                if (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                        altFlag = True
                if (event.key == pygame.K_RETURN) and altFlag:
                    if fullscreen == 0:
                        fullscreen = pygame.FULLSCREEN
                    else:
                        fullscreen = 0
                    screen = pygame.display.set_mode((width,height),fullscreen)
                    pygame.display.flip()
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                    altFlag = False
              
        
        player.direction("stop")
        
        lvlImg = pygame.image.load("Images/backgrounds/level"+str(level)+".png")
        lvlRect = lvlImg.get_rect()
        screen.blit(lvlImg,lvlRect)
        pygame.display.flip() 
        clock.tick(60)
              
    while start and not cutScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.direction("right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.direction("left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("down")
                if (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                    altFlag = True
                if (event.key == pygame.K_RETURN) and altFlag:
                    if fullscreen == 0:
                        fullscreen = pygame.FULLSCREEN
                    else:
                        fullscreen = 0
                    screen = pygame.display.set_mode((width,height),fullscreen)
                    pygame.display.flip()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.direction("stop right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.direction("stop left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("stop up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("stop down")
                if (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                    altFlag = False
                

        if random.randint(0,1000) == 0:   #1 in 60 chance
            powerUps += [SlowTime([random.randint(25, width-25), random.randint(25, height-25)])]
        if random.randint(0,1000) == 0:   #1 in 60 chance
            powerUps += [SpeedTime([random.randint(25, width-25), random.randint(25, height-25)])]
            
                    
        for potato in potatoes:
            potato.update()
        for powerUp in powerUps:
            powerUp.update()
        player.update()        
        
        for potato in potatoes:
            potato.collideWall(width, height)
        player.collideWall(width, height)
        
        if len(potatoes) > 1:
            for first in range(len(potatoes)-1):
                for second in range(first+1,len(potatoes)):
                    potatoes[first].collideBall(potatoes[second])
        
        for potato in potatoes:
            player.collideBall(potato)
        
        for powerUp in powerUps:
            if player.collidePowerUp(powerUp):
                if powerUp.type == "slow time":
                    for potato in potatoes:
                        potato.slowDown()
                if powerUp.type == "speed time":
                    for potato in potatoes:
                        potato.speedUp()
                if powerUp.type == "Male Enhancement":
                    for potato in potatoes:
                        potato.doubleSize()
                        
                
        deadcount= 0
        for powerUp in powerUps:
            if not powerUp.living:
                powerUps.remove(powerUp)
        
        for potato in potatoes:
            if not potato.living:
                deadcount += 1
                
        if len(potatoes) == deadcount:
            level += 1
            cutScreen = True
            for potato in potatoes:
                potato.hit()
            potatoes += [Potato([random.randint(3,3), random.randint(6,6)],  
                                [random.randint(75, width-75), random.randint(75, height-75)])]
            
            
                         
        screen.blit(bgImage, bgRect)
        for powerUp in powerUps:
            screen.blit(powerUp.image, powerUp.rect)
        screen.blit(player.image, player.rect)
        for potato in potatoes:
            screen.blit(potato.image, potato.rect)
        pygame.display.flip()
        clock.tick(60)