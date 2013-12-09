import pygame, sys, math

class SpeedTime():
    def __init__(self, pos = (0,0)):
        self.type = "speed time"
        self.image = pygame.image.load("Images/Speed_Time.png")
        self.rect = self.image.get_rect()
        self.radius = self.rect.width/2
        self.place(pos)
        self.living = True
        self.timer = 60*7
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            self.living = False