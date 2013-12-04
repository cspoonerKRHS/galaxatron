import pygame, sys, math

class SlowTime():
    def __init__(self, speed = [5,5],  pos = (0,0)):
        self.image = pygame.image.load("images/potato.png")
        #self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2
        self.place(pos)
        self.living = True
        self.frame = 0
        self.didhit = False