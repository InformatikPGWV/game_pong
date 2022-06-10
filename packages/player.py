import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)
        # Standard Einstellungen/Variablen für den Spieler
        self.UP_KEY, self.DOWN_KEY = False, False
        self.score = 0 # Punkte
        self.velocityY = 0 # Aktuelle Geschwindigkeit (Y-Achse)
        self.speedY = 5 # Geschwindigkeit des Spielers (Y-Achse)
        self.id = id
        self.sideOffset = 40 # Abstand vom Rand
        
        # Wenn Spieler 1
        if(self.id == 1):
            self.image = pygame.image.load('assets/images/player/player1.png') # Bild des Spielers 1
            self.rect = self.image.get_rect()
            self.rect.x = self.sideOffset - (self.rect.width/2) # Startposition am Rand Links(X-Achse)
        # Wenn Spieler 2
        elif(self.id == 2):
            self.image = pygame.image.load('assets/images/player/player2.png') # Bild des Spielers 2
            self.rect = self.image.get_rect()
            self.rect.x = 1280 - self.sideOffset - (self.rect.width/2) # Startposition am Rand Rechts(X-Achse)
        self.rect.y = 400 # Startposition (Y-Achse)

    def centerPlayers(self):
        self.rect.y = 400

    def event(self, event):
        if(self.id == 1): # Spieler 1 benutzt W, S
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: # Wenn Taste W gedrückt wird, dann UP_KEY auf True setzen
                    self.UP_KEY = True
                elif event.key == pygame.K_s: # Wenn Taste S gedrückt wird, dann DOWN_KEY auf True setzen
                    self.DOWN_KEY = True
            elif event.type == pygame.KEYUP: # Wenn Taste W losgelassen wird, dann UP_KEY auf False setzen
                if event.key == pygame.K_w:
                    self.UP_KEY = False
                elif event.key == pygame.K_s: # Wenn Taste S losgelassen wird, dann DOWN_KEY auf False setzen
                    self.DOWN_KEY = False
        elif(self.id == 2): # Spieler 2 benutzt Pfeiltaste Hoch, Runter
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: # Wenn Pfeiltaste Hoch gedrückt wird, dann UP_KEY auf True setzen
                    self.UP_KEY = True
                elif event.key == pygame.K_DOWN: # Wenn Pfeiltaste Runter gedrückt wird, dann DOWN_KEY auf True setzen
                    self.DOWN_KEY = True
            elif event.type == pygame.KEYUP: # Wenn Pfeiltaste Hoch losgelassen wird, dann UP_KEY auf False setzen
                if event.key == pygame.K_UP:
                    self.UP_KEY = False
                elif event.key == pygame.K_DOWN: # Wenn Pfeiltaste Runter losgelassen wird, dann DOWN_KEY auf False setzen
                    self.DOWN_KEY = False

    def draw(self, display):
        display.blit(self.image, self.rect) # Spieler anzeigen

    def update(self):
        self.velocityY = 0
        if self.UP_KEY: # Wenn UP_KEY auf True ist, dann setze Geschwindigkeit auf -speedY (weil Hoch) && verschiebe Spieler
            self.velocityY = -self.speedY
            self.rect.y += self.velocityY
        elif self.DOWN_KEY: # Wenn DOWN_KEY auf True ist, dann setze Geschwindigkeit auf +speedY (weil Runter) && verschiebe Spieler
            self.velocityY = self.speedY
            self.rect.y += self.velocityY
        
        if self.rect.y <= 0: # Wenn Spieler am Rand oben ist, dann setze Position auf 0
            self.rect.y = 0
        elif self.rect.y >= 645: # Wenn Spieler am Rand unten ist, dann setze Position auf 645 (720 - 75 (Höhe des Spielers) = 645)
            self.rect.y = 645