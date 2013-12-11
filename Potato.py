import pygame, sys, math

class Potato():
    def __init__(self, speed = [5,5],  pos = (0,0)):
        self.baseImage = pygame.image.load("images/potato.png")
        self.image = self.baseImage
        #self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.normalSize = self.rect.size
        self.doubleSize = (self.normalSize[0]*2, self.normalSize[1]*2)
        self.normalSpeedx = speed[0]
        self.normalSpeedy = speed[1]
        self.speedx = self.normalSpeedx
        self.speedy = self.normalSpeedy
        self.slowSpeedx = int(self.normalSpeedx/2)
        self.slowSpeedy = int(self.normalSpeedy/2)
        self.upSpeedx = int(self.normalSpeedx*2)
        self.upSpeedy = int(self.normalSpeedy*2)
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2
        self.place(pos)
        self.living = True
        self.frame = 0
        self.didhit = False
        self.hitcounter = 3
        self.slowTimeMax = 60*10
        self.slowTimer = self.slowTimeMax
        self.speedTimeMax = 60*10
        self.speedTimer = self.speedTimeMax
        
    
    def hit(self):
        if self.living:
            self.image = pygame.image.load("images/ghost_potato.png")
            #self.image = pygame.transform.scale(self.image, size)
            self.rect = self.image.get_rect(center = self.rect.center)
            self.living = False
        else:
            self.image = pygame.image.load("images/potato.png")
            #self.image = pygame.transform.scale(self.image, size)
            self.rect = self.image.get_rect(center = self.rect.center)
            self.living = True
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self):
        self.move()
        if self.slowTimer < self.slowTimeMax:
            if self.slowTimer > 0:
                self.slowTimer -= 1
            else:
                self.slowTimer = self.slowTimeMax
                self.speedx = self.normalSpeedx
                self.speedy = self.normalSpeedy
        if self.speedTimer < self.speedTimeMax:
            if self.speedTimer > 0:
                self.speedTimer -= 1
            else:
                self.speedTimer = self.speedTimeMax
                self.speedx = self.normalSpeedx
                self.speedy = self.normalSpeedy
        if self.didhit:
            if self.hitcounter > 0:
                self.hitcounter -= 1
            else:
                self.hitcounter = 3
                self.didhit = False
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        # print self.speed
        
    def collideWall(self, width, height):
        if not self.didhit:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.move()
                self.move()
                self.didhit = True
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.move()
                self.move()
                self.didhit = True
            
    def collideBall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    if self.rect.center[0] < other.rect.center[0]: #self left of other
                        if not self.didhit:
                            if self.speedx > 0: #moving right
                                self.speedx = -self.speedx
                                self.didhit = True
                        if not other.didhit:
                            if other.speedx < 0: #moving left
                                other.speedx = -other.speedx
                                other.didhit = True
                    if self.rect.center[0] > other.rect.center[0]: #self right of other
                        if self.speedx < 0: #moving left
                            self.speedx = -self.speedx
                        if other.speedx > 0: #moving right
                            other.speedx = -other.speedx
                    if self.rect.center[1] < other.rect.center[1]: #self above other
                        if self.speedy > 0: #moving down
                            self.speedy = -self.speedy
                        if other.speedy < 0: #moving up
                            other.speedy = -other.speedy
                    if self.rect.center[1] > other.rect.center[1]:#self below other
                        if self.speedy < 0: #moving up
                            self.speedy = -self.speedy
                        if other.speedy > 0: #moving down
                            other.speedy = -other.speedy
    
    def slowDown(self):
        self.slowTimer = self.slowTimeMax-1
        self.speedx = self.slowSpeedx
        self.speedy = self.slowSpeedy
        
    def speedUp(self):
        self.speedTimer = self.speedTimeMax-1
        self.speedx = self.upSpeedx
        self.speedy = self.upSpeedy
            
    def doubleSize(self):
        self.image = pygame.transform.scale(self.baseImage, self.doubleSize)
        self.rect = self.image.get_rect()
    
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))