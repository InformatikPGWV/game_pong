import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)
        self.UP_KEY, self.DOWN_KEY = False, False
        self.score = 0
        self.velocityY = 0
        self.speedY = 5
        self.centerBottom = (3, 8)
        self.id = id
        self.sideOffset = 40
        if(self.id == 1):
            self.image = pygame.image.load('assets/images/player/player1.png')
            self.rect = self.image.get_rect()
            self.rect.x = self.sideOffset - (self.rect.width/2)
            self.rect.y = 400
        elif(self.id == 2):
            self.image = pygame.image.load('assets/images/player/player2.png')
            self.rect = self.image.get_rect()
            self.rect.x = 1280 - self.sideOffset - (self.rect.width/2)
            self.rect.y = 400

        # print("Loaded Player"+str(self.id))

    def event(self, event):
        if(self.id == 1):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.UP_KEY = True
                elif event.key == pygame.K_s:
                    self.DOWN_KEY = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.UP_KEY = False
                elif event.key == pygame.K_s:
                    self.DOWN_KEY = False
        elif(self.id == 2):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                elif event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.UP_KEY = False
                elif event.key == pygame.K_DOWN:
                    self.DOWN_KEY = False

    def draw(self, display):
        display.blit(self.image, self.rect)

    def update(self):
        self.velocityY = 0
        if self.UP_KEY:
            self.velocityY = -self.speedY
            self.rect.y += self.velocityY
        elif self.DOWN_KEY:
            self.velocityY = self.speedY
            self.rect.y += self.velocityY
        
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= 645:
            self.rect.y = 645
            
    def getScore(self):
        return self.score