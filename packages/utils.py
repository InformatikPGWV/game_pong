import pygame

class Button():
    def __init__(self, x, y, image, scale):
        # initialisiere Button
        width =  image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width * scale), int(height * scale))) # Skaliere das Bild / den Button
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        
    def draw(self,display):
        pos = pygame.mouse.get_pos() # Frage Maus Position ab
        
        if self.rect.collidepoint(pos): # Prüfe ob Maus über Button ist
            self.image.set_alpha(100) # Setze Alpha Wert zu halb transparent
        else:
            self.image.set_alpha(255) # Setze Alpha Wert zurrück
        
        display.blit(self.image, (self.rect.x, self.rect.y)) # Zeige Button an
    
    def isClicked(self):
        #get mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False: # 0 LMB 1 RMB 2 RMB ---- Prüfe ob Maustaste gedrückt ist
                self.clicked = True # Blockiert das bei Klicken, halten erkannt wird, und gibt dann True zurück
            if pygame.mouse.get_pressed()[0] == False: # Setzt den Click zurück, wenn Taste losgelassen
                self.clicked = False # Setzt den Click zurück
        return self.clicked # Gebe Status zurück