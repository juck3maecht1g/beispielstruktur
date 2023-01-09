
from src.model.data.config.ExperimentConfigHandler import *
from src.model.data.config.GlobalConfigHandler import *
from src.model.data.PcDataHandler import *


root_path = r"C:\Users\morit\OneDrive\Desktop\Datastructure"
experiment_config_file = "experiment_config.yml"
global_config_file = "global_config.yml"

data_handler = PcDataHandler(root_path)
experiment_config = ExperimentConfigHandler(data_handler, experiment_config_file)
global_config = GlobalConfigHandler(data_handler, global_config_file)


global_config.create_config()

original_user = global_config.get_user()

for user in global_config.get_users():
    data_handler.createDirectory(user)
    data_handler.navigate_to_child(user)
    experiment_config.create_config()
    
global_config.set_user(original_user)










