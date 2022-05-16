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
        self.filePath = filePath
    
    ############################################################################
    # getData()
    # PARAMS:
    #  - none
    # Returns:
    # - data (dict): The data from the json file
    ############################################################################
    def getData(self):
        with open(self.filePath) as file:
            self.data = json.load(file)
            file.close()
            return self.data

    ############################################################################
    # writeData()
    # PARAMS:
    #  - data (dict): The data to be written to the file
    # Returns:
    # - None
    ############################################################################
    def writeData(self, data):
        with open(self.filePath, 'w') as file:
            json.dump(data, file)
            file.close()