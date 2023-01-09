from abc import ABC, abstractmethod

class ConfigHandler(ABC):

    @abstractmethod
    def __init__(self, data_handler, file) -> None:
        self.data_handler = data_handler
        self.file = file
        self.data = {}


    @abstractmethod
    def createConfig(self):
        pass
    
    