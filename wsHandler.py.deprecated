# Documentation: https://websockets.readthedocs.io/en/stable/intro/index.html

# Imports
try:
    from websockets import connect
    import asyncio
    import json
    import threading
except:
    import subprocess
    subprocess.call("pip install -r requirements.txt", shell=True)

    from websockets import connect
    import asyncio
    import json
    import threading

# from main import player1
# from main import player2

# Code


def runWsReciever():
    asyncio.run(recieveWsData("wss://wss.astrago.de"))


async def recieveWsData(uri):
    async with connect(uri) as ws:
        while True:
            handleWsEvent(await ws.recv())


def handleWsEvent(event):
    print(event)
    recievedWsEvent = json.loads(event)

    # Pong Game
    if recievedWsEvent["game"] == "pong":

        # Actions of 1st Player
        if recievedWsEvent["sender"] == "player1":

            # # Up Key
            # if recievedWsEvent["data"]["action"] == "upPredded":
            #     main.player1.UP_KEY = True
            # elif recievedWsEvent["data"]["action"] == "upReleased":
            #     main.player1.UP_KEY = False

            # # Down Key
            # if recievedWsEvent["data"]["action"] == "downPredded":
            #     main.player1.DOWN_KEY = True
            # elif recievedWsEvent["data"]["action"] == "downReleased":
            #     main.player1.DOWN_KEY = False

            pass


wsResciever = threading.Thread(target=runWsReciever)
wsResciever.start()
wsResciever.join()
