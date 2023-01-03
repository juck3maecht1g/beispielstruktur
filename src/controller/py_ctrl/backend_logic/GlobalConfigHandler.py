from configparser import ConfigParser
from PcDataHandler import get_cwd, change_directory_to_root, change_directory, cwd_contains



global_config = ConfigParser()
global_config_file = "global_config.ini"

global_config["DEFAULT"] = {
    "user": "Max"
}

global_config["Max"] = {
    "language": "Deutsch",
    "available_robots": ["11.1.1.1", "101.3.3.3", "10"],
    "available_laboratories": ["Lab1","Lab2"]
}

global_config["Moritz"] = {
    "language": "Englisch",
    "available_robots": ["11.1.1.1", "101.3.3.3"],
    "available_laboratories": ["Lab1","Lab2"]
}

def createGlobalConfig():
    old_path = get_cwd()
    change_directory_to_root()
    
    if not (cwd_contains(global_config_file)):
        with open(global_config_file, "w") as config_file:
            global_config.write(config_file)

    global_config.read(global_config_file)
    change_directory(old_path)

def changeGlobalConfig():
    old_path = get_cwd()
    change_directory_to_root()
    
    if (cwd_contains(global_config_file)):
        with open(global_config_file, "w") as config_file:
            global_config.write(config_file)

    change_directory(old_path)
    

def get_user():
    return global_config.get("DEFAULT", "user")

def set_user(new_user):
    if(new_user in global_config.sections()):
        global_config.set("DEFAULT", "user" , new_user)
        changeGlobalConfig()


def get_users():
    return global_config.sections()

def get_language():
    return global_config.get(get_user(), "language")

def set_language(new_language):
    global_config.set(get_user(), "language" , new_language)
    changeGlobalConfig()

def get_available_robots():
    return global_config.get(get_user(), "available_robots")

def set_available_robots(new_available_robots):
    global_config.set(get_user(), "available_robots" , new_available_robots)
    changeGlobalConfig()

def get_available_laboratories():
    return global_config.get(get_user(), "available_laboratories")

def set_available_laboratories(new_available_laboratories):
    global_config.set(get_user(), "available_laboratories" , new_available_laboratories)
    changeGlobalConfig()

