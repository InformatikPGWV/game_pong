import json
# Version 1.0

class jsonHandler():
    ############################################################################
    # Constructor
    # PARAMS:
    #  - filePath (str): Path to the json file
    # Returns:
    # - None
    ############################################################################
    def __init__(self, filePath):
        self.filePath = filePath # Initialisierung mit dem angegebenen Dateipfad
    
    ############################################################################
    # getData()
    # PARAMS:
    #  - none
    # Returns:
    # - data (dict): The data from the json file
    ############################################################################
    def getData(self):
        with open(self.filePath) as file: # öffne Datei
            self.data = json.load(file) # setze data auf Inhalt der Datei
            file.close() # schließe Datei
            return self.data # gebe data zurück

    ############################################################################
    # writeData()
    # PARAMS:
    #  - data (dict): The data to be written to the file
    # Returns:
    # - None
    ############################################################################
    def writeData(self, data):
        with open(self.filePath, 'w') as file: # öffne Datei (oder Erstelle wenn nicht vorhanden)
            json.dump(data, file) # schreibe Daten in Datei
            file.close() # Schließen der Datei