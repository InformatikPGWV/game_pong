# Imports
try:
    import pygame
    import json
    import threading
    import websocket
    import rel
    import time
    import pyfiglet
    import random
    import sys
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
    import random
    import sys

from packages.player import Player
from packages.ball import Ball
from packages.utils import Button
from packages.jsonHandler import jsonHandler


################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 1280, 720
canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W, DISPLAY_H)))
clock = pygame.time.Clock()

settings = jsonHandler("settings.json")
################################# LOAD PLAYER ###################################
player1 = Player(1)
player2 = Player(2)
ball = Ball()

################################# LOAD BUTTONS ###################################
start_img = pygame.image.load("assets/images/buttons/start.png")
exit_img = pygame.image.load("assets/images/buttons/exit.png")

tick = pygame.image.load("assets/images/tick.png")

mainMenu_startButton = Button(DISPLAY_W/2-(279/2)-25, DISPLAY_H/2-(126/4), start_img, 0.5)
mainMenu_exitButton = Button(DISPLAY_W/2-(240/2)+(279/2)+10,DISPLAY_H/2-(126/4), exit_img, 0.5)

game_exitButton = Button(640,455, exit_img, 0.5)

timeMode = "upcounting"

# ################################# GAME LOOP ##########################
showMainMenu = True
startup = True

green = (0, 255, 0)
blue = (0, 0, 128)

font16 = pygame.font.Font('assets/Roboto-Black.ttf', 16)
font32 = pygame.font.Font('assets/Roboto-Black.ttf', 32)


running = True

def current_milli_time():
    return round(time.time() * 1000)

def current_second_time():
    return round(time.time())

def font(size):
    return pygame.font.Font('assets/Roboto-Black.ttf', size)

font16.render("Connecting to server...", True, (255, 255, 255))

def loadSettings():
    global settings
    settings.getData()
    infiniteGame = settings.data["infiniteGame"]
    LimitedGameTimeMinutes = settings.data["LimitedGameTimeMinutes"]
    LimitedGameTimeSeconds = settings.data["LimitedGameTimeSeconds"]

def quit():
    global running
    running = False
    ws.close()
    exit()

def upcount():
    global gameStartTime
    global secondsTimePlayed
    global minutesTimePlayed
    time = current_second_time() - gameStartTime
    minuteTimePlayed = int(time / 60)
    secondsTimePlayed = int(time % 60)
    if secondsTimePlayed < 10:
        secondsTimePlayed = "0" + str(secondsTimePlayed)
    if minuteTimePlayed < 10:
        minutesTimePlayed = "0" + str(minuteTimePlayed)

def downCount():
    global gameStartTime

def mainGame():
    global gameStartTime
    global secondsTimePlayed
    global minutesTimePlayed
    global showMainMenu
    global ws
    
    while running:
        canvas.fill((0, 0, 0))
        if showMainMenu:
            mainMenu_startButton.draw(canvas)
            mainMenu_exitButton.draw(canvas)
            if mainMenu_startButton.isClicked():
                showMainMenu = False
                gameStartTime = current_second_time()
            if mainMenu_exitButton.isClicked():
                quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        else:
            ################################# CHECK PLAYER INPUT #################################
            game_exitButton.draw(canvas)
            if game_exitButton.isClicked():
                quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                player1.event(event)
                player2.event(event)

            ################################# UPDATE/ Animate SPRITE #################################
            
            if startup:
                canvas.blit(font32.render("Beide Spieler müssen Hoch drücken um zu starten!", True, (255, 255, 255)), (285, 10))
                if player1.UP_KEY == True and player2.UP_KEY == True:
                    startup = False
                if player1.UP_KEY == True:
                    canvas.blit(tick, (10,50))
                if player2.UP_KEY == True:
                    canvas.blit(tick, (1240,50))
            else:
                player1.update()
                player2.update()
                ballEvent = ball.update(player1, player2)
                if(ballEvent == "goalPlayer1"):
                    player1.score += 1
                if(ballEvent == "goalPlayer2"):
                    player2.score += 1
                
                upcount()
                canvas.blit(font(32).render(f"{minutesTimePlayed}:{secondsTimePlayed}", True, (255, 255, 255)), (650, 10))
                canvas.blit(font(32).render(str(player1.score), True, (255, 255, 255)), (10, 10))
                canvas.blit(font(32).render(str(player2.score), True, (255, 255, 255)), (1248, 10))
                canvas.blit(font(16).render(str(int(clock.get_fps())), True, (255, 255, 255)), (0, 704))
            ############################### DRAW PLAYER #################################
            player1.draw(canvas)
            player2.draw(canvas)
            ball.draw(canvas)
            #############################################################################

        clock.tick(60)  # Auf 60 Bilder pro Sekunde beschränken
        window.blit(canvas, (0, 0))
        pygame.display.update()


################################# WebSockets #################################


def connectToWebSocket():
    global ws
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://s1.astrago.de:6969",  # wss://wss.astrago.de #    "ws://s1.astrago.de:6969"
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    # rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
    


def on_error(ws, error):
    print(error)
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

            elif recievedWsEvent["data"]["action"] == "upReleased":
                player1.UP_KEY = False

            # Down Key
            if recievedWsEvent["data"]["action"] == "downPressed":
                player1.DOWN_KEY = True

            elif recievedWsEvent["data"]["action"] == "downReleased":
                player1.DOWN_KEY = False


        # Actions of 2nd Player
        if recievedWsEvent["sender"] == "player2":

            # Up Key
            if recievedWsEvent["data"]["action"] == "upPressed":
                player2.UP_KEY = True

            elif recievedWsEvent["data"]["action"] == "upReleased":
                player2.UP_KEY = False


            # Down Key
            if recievedWsEvent["data"]["action"] == "downPressed":
                player2.DOWN_KEY = True

            elif recievedWsEvent["data"]["action"] == "downReleased":
                player2.DOWN_KEY = False



################################# END #################################

def showWarning():
    print(str(pyfiglet.figlet_format("WARNUNG!", font32="banner3")))
    print("Aufgrund eines Bugs darf der Schließen-Klopf des Spielfensters NICHT gedrückt werden.\nSchließen Sie das Spiel bitte NUR über den Schließen-Knopf der Konsole.\nVielen Dank.")
    time.sleep(2)


if __name__ == "__main__":

    # showWarning()

    wsConnection = threading.Thread(target=connectToWebSocket)
    wsConnection.start()

    mainGame()

    wsConnection.join()


# todo:
# - add a button to go to the main menu
# - add a button to go to the credits
# - add a button to go to the instructions
# - add a button to go to the high scores
# - add a button to go to the options
