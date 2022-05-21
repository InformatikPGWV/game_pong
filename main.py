# Imports
try:
    import pygame
    import json
    import threading
    import websocket
    import rel
    import time
    import pyfiglet
except:
    import subprocess
    subprocess.call("pip install -r requirements.txt", shell=True)

    import pygame
    import json
    import threading
    import websocket
    import rel
    import time
    import pyfiglet


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
player1 = Player(1)
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
                player1.event(event)
                if(multiplayer == True):
                    player2.event(event)

            ################################# UPDATE/ Animate SPRITE #################################
            player1.update()
            if(multiplayer == True):
                player2.update()
            ################################# UPDATE WINDOW AND DISPLAY #################################
            canvas.fill((255, 255, 255))
            ############################### DRAW PLAYER #################################
            player1.draw(canvas)
            if(multiplayer == True):
                player2.draw(canvas)
            #############################################################################
        clock.tick(60)  # LOCK TO 60 FRAMES PER SECOND
        window.blit(canvas, (0, 0))
        pygame.display.update()
        # print(clock.get_fps())
    print("\n\n\n\nThanks for Playing...")


################################# WebSockets #################################


def connectToWebSocket():
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://wss.astrago.de",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    # rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()


def on_error(ws, error):
    pass


def on_close(ws, close_status_code, close_msg):
    pass


def on_open(ws):
    pass


def on_message(ws, event):
    # print(event)
    recievedWsEvent = json.loads(event)

    # Pong Game
    if recievedWsEvent["game"] == "pong":

        # Actions of 1st Player
        if recievedWsEvent["sender"] == "player1":

            # Up Key
            if recievedWsEvent["data"]["action"] == "upPressed":
                player1.UP_KEY = True
                player1.update()
                player1.draw(canvas)
                window.blit(canvas, (0, 0))
                pygame.display.update()

            elif recievedWsEvent["data"]["action"] == "upReleased":
                player1.UP_KEY = False
                player1.update()
                player1.draw(canvas)
                window.blit(canvas, (0, 0))
                pygame.display.update()

            # Down Key
            if recievedWsEvent["data"]["action"] == "downPressed":
                player1.DOWN_KEY = True
                player1.update()
                player1.draw(canvas)
                window.blit(canvas, (0, 0))
                pygame.display.update()

            elif recievedWsEvent["data"]["action"] == "downReleased":
                player1.DOWN_KEY = False
                player1.update()
                player1.draw(canvas)
                window.blit(canvas, (0, 0))
                pygame.display.update()

        # Actions of 2nd Player
        if recievedWsEvent["sender"] == "player2":

            # Up Key
            if recievedWsEvent["data"]["action"] == "upPressed":
                player2.UP_KEY = True
                player2.update()
                player2.draw(canvas)
                window.blit(canvas, (0, 0))
                pygame.display.update()

            elif recievedWsEvent["data"]["action"] == "upReleased":
                player2.UP_KEY = False
                player2.update()
                player2.draw(canvas)
                window.blit(canvas, (0, 0))
                pygame.display.update()

            # Down Key
            if recievedWsEvent["data"]["action"] == "downPressed":
                player2.DOWN_KEY = True
                player2.update()
                player2.draw(canvas)
                window.blit(canvas, (0, 0))
                pygame.display.update()

            elif recievedWsEvent["data"]["action"] == "downReleased":
                player2.DOWN_KEY = False
                player2.update()
                player2.draw(canvas)
                window.blit(canvas, (0, 0))
                pygame.display.update()


################################# END #################################

def showWarning():
    print(str(pyfiglet.figlet_format("WARNUNG!", font="banner3")))
    print("Aufgrund eines Bugs darf der Schließen-Klopf des Spielfensters NICHT gedrückt werden.\nSchließen Sie das Spiel bitte NUR über den Schließen-Knopf der Konsole.\nVielen Dank.")
    time.sleep(10)


if __name__ == "__main__":

    showWarning()

    wsConnection = threading.Thread(target=connectToWebSocket)
    wsConnection.start()

    mainGame()


# todo:
# - add a button to go to the main menu
# - add a button to go to the credits
# - add a button to go to the instructions
# - add a button to go to the high scores
# - add a button to go to the options
