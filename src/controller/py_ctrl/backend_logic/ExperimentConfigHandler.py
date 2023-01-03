from configparser import ConfigParser

from PcDataHandler import is_root, is_child_from_root, copy_file_from_parent, cwd_contains, get_cwd, change_directory, navigate_to_parent

experiment_config = ConfigParser()
experiment_config_file = "experiment_config.ini"

experiment_config["Settings"] = {
    "gripper": [],
    "recording": []
}

experiment_config["Variables"] = {
}

def createExperimentConfig():
    if not (is_root()):

        if(is_child_from_root()):
            if not (cwd_contains(experiment_config_file)):
                with open(experiment_config_file, "w") as config_file:
                    experiment_config.write(config_file)

        elif not (cwd_contains(experiment_config_file)):
            copy_file_from_parent(experiment_config_file)
            experiment_config.remove_section("Variables")
            experiment_config.add_section("Variables")
        
        experiment_config.read(experiment_config_file)

def changeExperimentConfig():
    if not (is_root()):
        with open(experiment_config_file, "w") as config_file:
            experiment_config.write(config_file)

def get_variables():
    old_path = get_cwd()
    variables = dict()

    while not (is_root()):
        parent_variables = dict(experiment_config.items("Variables"))

        for var_name in parent_variables:
            if not (var_name in variables):
                variables.update({var_name: parent_variables.get(var_name)})
        
        navigate_to_parent()

    change_directory(old_path)
    return variables

def get_gripper():
    return experiment_config.get("Settings", "gripper")

def set_gripper(new_gripper):
        experiment_config.set("Settings", "gripper" , new_gripper)
        changeExperimentConfig()

def get_recording():
    return experiment_config.get("Settings", "recording")

def set_recording(new_recording):
        experiment_config.set("Settings", "recording" , new_recording)
        changeExperimentConfig()


def add_variable(name, value):
    if not (experiment_config.has_option("Variables", name)):
        experiment_config.set("Variables", name, value)
        changeExperimentConfig()

def change_variable(name, value):
    if (experiment_config.has_option("Variables", name)):
        experiment_config.set("Variables", name, value)    
        changeExperimentConfig()
    
def remove_variable(name):
    experiment_config.remove_option("Variables", name)  
    changeExperimentConfig() 

