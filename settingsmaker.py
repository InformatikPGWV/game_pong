from packages.jsonHandler import jsonHandler
# Initialisiere Einstellungsdatei und lese Daten
file = jsonHandler("settings.json")
file.getData()

# Speicher alte Einstellungen zwischen
oldInfiniteGame = file.data["infiniteGame"]
oldLimitedGameTimeMinutes = file.data["LimitedGameTimeMinutes"]
oldLimitedGameTimeSeconds = file.data["LimitedGameTimeSeconds"]

def timeSettings():
    global LimitedGameTimeSeconds
    global LimitedGameTimeMinutes
    # Zeige die alten Einstellungen
    print(f"Alte Einstellungen \nLaufzeit Minuten: {oldLimitedGameTimeMinutes} \nLaufzeit Sekunden: {oldLimitedGameTimeSeconds}")
    LimitedGameTimeMinutes = input("Bitte geben Sie die Minuten ein (Int): ")
    # Wenn leer übernehme alte Einstellungen
    if(LimitedGameTimeMinutes == ""):
        LimitedGameTimeMinutes = oldLimitedGameTimeMinutes
    LimitedGameTimeSeconds = input("Bitte geben Sie die Sekunden ein (Int): ")
    if(LimitedGameTimeSeconds == ""):
        LimitedGameTimeSeconds = oldLimitedGameTimeSeconds
        
    
print("\n\n\n\n\n\n\n\n\nBeantworte die folgenden Fragen um die Spieleinstellungen zu treffen! \n Lasse die Eingabe leer um den alten Wert bezubehalten")

# Zeige den User die aktuelle Einstellung
print(f"infiniteGame: {oldInfiniteGame}")
infiniteGame = input("Soll das Spiel immer laufen?(y/n) ")
if infiniteGame == "y":
    # Wenn das Spiel unendlich laufen soll, behalte die Zeiteinstellungen bei, da sie irrelevant sind
    infiniteGame = True
    LimitedGameTimeMinutes = oldLimitedGameTimeMinutes
    LimitedGameTimeSeconds = oldLimitedGameTimeSeconds
elif infiniteGame == "n":
    # Frage nach Zeit Einstellungen
    infiniteGame = False
    timeSettings()
else:
    # Wenn leer übernehme alte Einstellung, wenn die Einstellung aut endlich ist dann frage nach Zeit
    infiniteGame = oldInfiniteGame
    if oldInfiniteGame == False:
        timeSettings()
        
# Speicher in settings.json

json_data = {
        "infiniteGame" : infiniteGame,
        "LimitedGameTimeMinutes": LimitedGameTimeMinutes,
        "LimitedGameTimeSeconds": LimitedGameTimeSeconds
    }
# Gib dem User eine Info wenn die Einstellungen gespeichert wurden
if(file.writeData(json_data)):
    print("Einstellungen gespeichert! Viel Spaß beim Spielen! \n\n\n\n\n")
    
