
from src.model.data.PcDataHandler import *
import ConfigHandler

experiment_config_file = "experiment_config.yml"


class ExperimentConfigHandler(ConfigHandler):

    def __init__(self, data_handler, file) -> None:
        self.file = file
        self.data_handler = data_handler
        self.data = { 
            "Settings": { 
                "gripper": "hey", 
                "recording": "ho"}, 
            "Variables": {
            }
        }


    def create_config(self):
        if not (self.data_handler.is_root()):

            if(self.data_handler.is_child_from_root()):
                if not (self.data_handler.path_contains(self.file)):
                    self.__write_config()

            elif not (self.data_handler.path_contains(self.file)):
                self.data_handler.copy_file_from_parent(self.file)
                self.data.update({"Variables": {}})
                self.__write_config()
        
            
    def __read_config(self):
        self.data = self.data_handler.read_experiment_config(self.file)

    def __write_config(self):
        self.data_handler.write_experiment_config(self.data, self.file)
        
    def get_gripper(self):
        self.__read_config()
        return self.data["Settings"]["gripper"]

    def set_gripper(self, new_gripper):
        self.__read_config()
        self.data["Settings"]["gripper"] = new_gripper
        self.__write_config()

    def __get_variables(self):
        self.__read_config()
        return self.data["Variables"]


    def get_variables(self):
        old_path = self.data_handler.get_path()
        variables = dict()

        while not (self.data_handler.is_root()):
            parent_variables = self.__get_variables()

            for var_name in parent_variables:
                if not (var_name in variables):
                    variables.update({var_name: parent_variables.get(var_name)})
        
            self.data_handler.navigate_to_parent()

        self.data_handler.set_path(old_path)
        return variables




