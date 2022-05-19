# Documentation: https://websockets.readthedocs.io/en/stable/intro/index.html

# Imports
try:
    from websockets import connect
    import asyncio
    import json
except:
    import subprocess
    subprocess.call("pip install -r requirements.txt", shell=True)

    from websockets import connect
    import asyncio
    import json


# Code
def runWsReciever():
    asyncio.run(recieveWsData("wss://wss.astrago.de"))


async def recieveWsData(uri):
    async with connect(uri) as ws:
        while True:
            handleWsEvent(await ws.recv())


def handleWsEvent(event):
    recievedWsEvent = json.loads(event)
    # Pong Game
    if recievedWsEvent["game"] == "pong":
        # Actions of 1st Player
        if recievedWsEvent["sender"] == "player1":
            if recievedWsEvent["data"]["action"] == "upPredded":
                pass
            elif recievedWsEvent["data"]["action"] == "upReleased":
                pass
