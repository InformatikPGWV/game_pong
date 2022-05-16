import pygame


class Button():
    def __init__(self, x, y, image, scale):
        width =  image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        
    def draw(self,display):
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check if mouse is over button
        if self.rect.collidepoint(pos):
            #change the transparency of the button
            self.image.set_alpha(100)
        else:
            self.image.set_alpha(255)
        
        #draw button
        display.blit(self.image, (self.rect.x, self.rect.y))
    
    def isClicked(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            #check if mouse is clicked
            if pygame.mouse.get_pressed()[0] and self.clicked == False: # 0 LMB 1 RMB 2 RMB
                self.clicked = True # Blockiert das bei Klicken, halten erkannt wird
                action = True
            if pygame.mouse.get_pressed()[0] == False: # Setzt den Click zurück, wenn Taste losgelassen
                action = False
                self.clicked = False
        return action