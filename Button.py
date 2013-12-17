import pygame, sys, math

class Button():
    def __init__(self, image, pos = (0,0), size = (100,100)):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.place(pos)
        
    def collidePoint(self, pt):
        if self.rect.right > pt[0] and self.rect.left < pt[0]:
            if self.rect.bottom > pt[1] and self.rect.top < pt[1]:
                return True
        return False
        
    def place(self, pt):
        self.rect.center = pt