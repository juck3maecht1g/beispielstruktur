from configparser import ConfigParser
from .PcDataHandler import createGlobalConfig, changeGlobalConfig



global_config = ConfigParser()
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

def createGConfig():
    createGlobalConfig(global_config)

def get_user():
    return global_config.get("DEFAULT", "user")

def set_user(new_user):
    if(new_user in global_config.sections()):
        global_config.set("DEFAULT", "user" , new_user)
        changeGlobalConfig(global_config)


def get_users():
    return global_config.sections()

def get_language():
    return global_config.get(get_user(), "language")

def set_language(new_language):
    global_config.set(get_user(), "language" , new_language)
    changeGlobalConfig(global_config)

def get_available_robots():
    return global_config.get(get_user(), "available_robots")

def set_available_robots(new_available_robots):
    global_config.set(get_user(), "available_robots" , new_available_robots)
    changeGlobalConfig(global_config)

def get_available_laboratories():
    return global_config.get(get_user(), "available_laboratories")

def set_available_laboratories(new_available_laboratories):
    global_config.set(get_user(), "available_laboratories" , new_available_laboratories)
    changeGlobalConfig(global_config)

