
from src.model.data.PcDataHandler import *
import ConfigHandler


class GlobalConfigHandler(ConfigHandler):

    def __init__(self, data_handler, file) -> None:
        self.file = file
        self.handler = data_handler
        self.data = { 
            "User": "Max",

            "Users":{
                "Max": { 
                    "language": "german",
                    "available robots": {},
                    "available labatories": {}
                },

                "Moritz": { 
                    "language": "german",
                    "available robots": {},
                    "available labatories": {}
                }
            }
        }


    def create_config(self):
        if not (self.handler.path_contains(self.file)):
            self.handler.write_global_config(self.data, self.file)

    def __read_config(self):
        self.data = self.handler.read_global_config(self.file)

    def __write_config(self):
        self.handler.write_global_config(self.data, self.file)

    def get_user(self):
        self.__read_config()
        return self.data["User"]

    def set_user(self, user):
        self.__read_config()
        self.data["User"] = user
        self.__write_config()

    def get_users(self):
        self.__read_config()
        return self.data["Users"].keys()

 