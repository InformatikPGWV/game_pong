import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.randomizeStartVelocity()
        self.centerBottom = (3, 8)
        self.sideOffset = 40
        self.image = pygame.image.load('assets/images/ball.png')
        self.rect = self.image.get_rect()
        self.rect.x = (1280/2) - (self.rect.width/2)
        self.rect.y = (720/2) - (self.rect.height/2)
        self.maxVelocityX = 30 # max velocity in x Richtung || sollte 30 nicht überschreiten
        self.maxVelocityY = 10 # max velocity in y Richtung || sollte 15 nicht überschreiten
        
        self.minVelocityX = 3 # min velocity in x Richtung
        self.minVelocityY = 3 # min velocity in y Richtung
        
        self.sounds = {"hit" : "assets/sounds/hit.wav",
                       "goal": "assets/sounds/goal.wav"}

    def draw(self, display):
        display.blit(self.image, self.rect)

    def centerBall(self):
        self.rect.x = (1280/2) - (self.rect.width/2)
        self.rect.y = (720/2) - (self.rect.height/2)
        self.randomizeStartVelocity()
    
    def validateMinSpeed(self):
        # Setze ein Minimum für die Geschwindigkeit
        if self.velocityX < self.minVelocityX:
            self.velocityX = self.minVelocityX
        if self.velocityY < self.minVelocityY:
            self.velocityY = self.minVelocityY
    
    def randomizeStartVelocity(self):
        self.velocityY = random.randint(2,6)
        self.velocityX = random.randint(2,6)
        # Invertiere die Richtung zufällig
        if random.randint(0,1) == 0:
            self.velocityX = -self.velocityX
        if random.randint(0,1) == 0:
            self.velocityY = -self.velocityY
    
    
    def update(self, player1,player2):
        returnMessage = ""
        if self.rect.colliderect(player1.rect):
            print("Collision with player1")
            pygame.mixer.Sound.play(pygame.mixer.Sound(self.sounds["hit"]))
            if self.velocityX > -self.maxVelocityX:
                self.velocityX = -self.velocityX * 1.075
            self.velocityY = self.velocityY * 1.075
            self.rect.y = self.rect.y
            self.rect.x = self.rect.x + 15
            print(self.velocityX)
            
            
        if self.rect.colliderect(player2.rect):
            print("Collision with player2")
            pygame.mixer.Sound.play(pygame.mixer.Sound(self.sounds["hit"]))
            if self.velocityX > -self.maxVelocityX:
                self.velocityX = -self.velocityX * 1.075
            self.velocityY = self.velocityY * 1.075
            self.rect.y = self.rect.y
            self.rect.x = self.rect.x - 15
            print(self.velocityX)

        if self.rect.y <= 0:
            print("Collision with top")
            self.velocityY = -self.velocityY
        if self.rect.y >= 705:
            print("Collision with bottom")
            self.velocityY = -self.velocityY
        
        if self.rect.x <= 0:
            print("Collision with left")
            self.centerBall()
            self.validateMinSpeed()
            pygame.mixer.Sound.play(pygame.mixer.Sound(self.sounds["goal"]))
            returnMessage = "goalPlayer2"
        elif self.rect.x >= 1255:
            print("Collision with right")
            self.centerBall()
            self.validateMinSpeed()
            pygame.mixer.Sound.play(pygame.mixer.Sound(self.sounds["goal"]))
            returnMessage = "goalPlayer1"

        self.rect.y += self.velocityY
        self.rect.x += self.velocityX
        return returnMessage