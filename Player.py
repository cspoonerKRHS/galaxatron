import pygame, sys, math

class PlayerBall():
    def __init__(self, image, speed = (2,2), pos = (0,0), size = (100,100)):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.maxSpeedx = speed[0]
        self.maxSpeedy = speed[1]
        self.speed = [0,0]
        self.radius = self.rect.width/2
        self.place(pos)
        self.didBounce = False
        
    def update(self):
        self.didBounce = False
        self.move()
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def direction(self, dir):
        if dir == "right":
            self.speed[0] = self.maxSpeedx
        if dir == "left":
            self.speed[0] = -self.maxSpeedx   
        if dir == "stop right":
            self.speed[0] = 0  
        if dir == "stop left":
            self.speed[0] = 0   
        if dir == "up":
            self.speed[1] = -self.maxSpeedy
        if dir == "down":
            self.speed[1] = self.maxSpeedy
        if dir == "stop up":
            self.speed[1] = 0  
        if dir == "stop down":
            self.speed[1] = 0   
        
    def wallBounce(self, width, height):
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = 0
            self.didBounce = True
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = 0
            self.didBounce = True

        
     
    def collideBall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.distanceToPoint(other.rect.center) < (self.radius + other.radius):
                    if not other.didBounce:
                        other.speed[0] = -other.speed[0]
                        other.speed[1] = -other.speed[1]
                        other.didBounce = True
        
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    
    def place(self, pt):
        self.rect.center = pt
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    