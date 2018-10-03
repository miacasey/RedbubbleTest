# data.py
# Import the json module
import json

class Data:
    '''
    This class implements a method to parse and return the data of a JSON file.
    '''
    # Function __init__ initializes the JSON data that we want to parse
    #       Parameters: The name of the JSON file we want to get data from
    #       Returns: Nothing
    #       Raises: IOError if the file does not exist
    def __init__(self, file):
        try:
            self.file= open(file, "r")
        except IOError:
            raise IOError("File: {path} is not valid file name".format(path= file))
    # Function get_data
    #       Parameters: None
    #       Returns: The data from the JSON file, using the JSON library
    #       Raises: ValueError if the JSON file is not a valid JSON file
    def get_data(self):
        try:
            return json.loads(self.file.read())
        except ValueError:
            raise ValueError("File: {path} is not a valid JSON object".format(path= self.file.name))
