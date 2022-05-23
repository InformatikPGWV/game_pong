import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.velocityY = random.randint(-3,3)
        # self.velocityY = -5
        # self.velocityX = 0
        self.velocityX = random.randint(-8,8)
        self.centerBottom = (3, 8)
        self.sideOffset = 40
        self.image = pygame.image.load('assets/images/ball.png')
        self.rect = self.image.get_rect()
        self.rect.x = (1280/2) - (self.rect.width/2)
        self.rect.y = (720/2) - (self.rect.height/2)

    def draw(self, display):
        display.blit(self.image, self.rect)

    def update(self, player1,player2):
        if self.rect.colliderect(player1.rect):
            print("Collision with player1")
            self.velocityX = -self.velocityX * 1.075
            self.velocityY = self.velocityY * 1.075
        if self.rect.colliderect(player2.rect):
            print("Collision with player2")
            self.velocityX = -self.velocityX * 1.075
            self.velocityY = self.velocityY * 1.075
        



        if self.rect.y <= 0:
            print("Collision with top")
            self.velocityY = -self.velocityY
        if self.rect.y >= 705:
            print("Collision with bottom")
            self.velocityY = -self.velocityY
        
        if self.rect.x <= 0:
            print("Collision with left")
            self.rect.x = (1280/2) - (self.rect.width/2)
            self.rect.y = (720/2) - (self.rect.height/2)
        elif self.rect.x >= 1255:
            print("Collision with right")
            self.rect.x = (1280/2) - (self.rect.width/2)
            self.rect.y = (720/2) - (self.rect.height/2)
        
    
        self.rect.y += self.velocityY
        self.rect.x += self.velocityX