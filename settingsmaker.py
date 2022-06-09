from packages.jsonHandler import jsonHandler

file = jsonHandler("settings.json")
file.getData()

oldInfiniteGame = file.data["infiniteGame"]
oldLimitedGameTimeMinutes = file.data["LimitedGameTimeMinutes"]
oldLimitedGameTimeSeconds = file.data["LimitedGameTimeSeconds"]

def timeSettings():
    global LimitedGameTimeSeconds
    global LimitedGameTimeMinutes
    print(f"Alte Einstellungen \nLaufzeit Minuten: {oldLimitedGameTimeMinutes} \nLaufzeit Sekunden: {oldLimitedGameTimeSeconds}")
    LimitedGameTimeMinutes = int(input("Bitte geben Sie die Minuten ein (Int): "))
    if(LimitedGameTimeMinutes == ""):
        LimitedGameTimeMinutes = oldLimitedGameTimeMinutes
    LimitedGameTimeSeconds = int(input("Bitte geben Sie die Sekunden ein (Int): "))
    if(LimitedGameTimeSeconds == ""):
        LimitedGameTimeSeconds = oldLimitedGameTimeSeconds
        
    
print("\n\n\n\n\n\n\n\n\nBeantworte die folgenden Fragen um die Spieleinstellungen zu treffen! \n Lasse die Eingabe leer um den alten Wert bezubehalten")

print(f"infiniteGame: {oldInfiniteGame}")
infiniteGame = input("Soll das Spiel immer laufen?(y/n) ")
if infiniteGame == "y":
    infiniteGame = True
    LimitedGameTimeMinutes = oldLimitedGameTimeMinutes
    LimitedGameTimeSeconds = oldLimitedGameTimeSeconds
elif infiniteGame == "n":
    infiniteGame = False
    timeSettings()
else:
    infiniteGame = oldInfiniteGame
    if oldInfiniteGame == True:
        timeSettings()

json_data = {
        "infiniteGame" : infiniteGame,
        "LimitedGameTimeMinutes": LimitedGameTimeMinutes,
        "LimitedGameTimeSeconds": LimitedGameTimeSeconds
    }
if(file.writeData(json_data)):
    print("Einstellungen gespeichert! Viel Spaß beim Spielen! \n\n\n\n\n")
    
