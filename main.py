# Imports
try:
    import pygame
except:
    import subprocess
    subprocess.call("pip install -r requirements.txt", shell=True)

    import pygame


from packages.player import Player
from packages.utils import Button


# multiplayer = input("Multiplayer? (y/n) ")
multiplayer = "y"
if(multiplayer == "y"):
    multiplayer = True
elif(multiplayer == "n"):
    multiplayer = False
else:
    multiplayer = False
    print("Invalid input. Defaulting to single player.")

################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 1280, 720
canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W, DISPLAY_H)))
clock = pygame.time.Clock()
################################# LOAD PLAYER ###################################
player = Player(1)
if(multiplayer == True):
    player2 = Player(2)
################################# LOAD BUTTONS ###################################
start_img = pygame.image.load("assets/images/buttons/start.png")
exit_img = pygame.image.load("assets/images/buttons/exit.png")


exit_button = Button(DISPLAY_W/2-(240/2)+(279/2)+10,
                     DISPLAY_H/2-(126/4), exit_img, 0.5)
start_button = Button(DISPLAY_W/2-(279/2)-25,
                      DISPLAY_H/2-(126/4), start_img, 0.5)
# ################################# GAME LOOP ##########################
showMainMenu = False


def mainGame():
    global showMainMenu
    running = True
    while running:

        if showMainMenu:
            start_button.draw(canvas)
            exit_button.draw(canvas)
            if start_button.isClicked():
                print("Start")
                showMainMenu = False
            if exit_button.isClicked():
                print("EXIT")
                running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        else:
            ################################# CHECK PLAYER INPUT #################################
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                player.event(event)
                if(multiplayer == True):
                    player2.event(event)

            ################################# UPDATE/ Animate SPRITE #################################
            player.update()
            if(multiplayer == True):
                player2.update()
            ################################# UPDATE WINDOW AND DISPLAY #################################
            canvas.fill((255, 255, 255))
            ############################### DRAW PLAYER #################################
            player.draw(canvas)
            if(multiplayer == True):
                player2.draw(canvas)
            #############################################################################
        clock.tick(60)  # LOCK TO 60 FRAMES PER SECOND
        window.blit(canvas, (0, 0))
        pygame.display.update()
        print(clock.get_fps())
    print("\n\n\n\nThanks for Playing...")


################################# END #################################
mainGame()

# todo:
# - add a button to go to the main menu
# - add a button to go to the credits
# - add a button to go to the instructions
# - add a button to go to the high scores
# - add a button to go to the options
