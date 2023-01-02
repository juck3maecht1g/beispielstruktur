#Todo sauberes Error handling


root = r"C:\Users\morit\OneDrive\Desktop\Datastructure"
global_config_file = "global_config.ini"
experiment_config_file = "experiment_config.ini"

import shutil
import os
os.chdir(root)


def navigate_to_parent():
    if not (os.getcwd() == root):
        new_path = os.path.dirname(os.getcwd())
        os.chdir(new_path)

def navigate_to_child(name):
    if(name in list_children()):
        new_path = os.path.join(os.getcwd(), name)
        os.chdir(new_path)
    
def list_children():
    return os.listdir()

def createGlobalConfig(global_config):
    old_path = os.getcwd()
    os.chdir(root)
    
    if not (global_config_file in list_children()):
        with open(global_config_file, "w") as config_file:
            global_config.write(config_file)

    os.chdir(old_path)

def changeGlobalConfig(global_config):
    old_path = os.getcwd()
    os.chdir(root)
    
    with open(global_config_file, "w") as config_file:
        global_config.write(config_file)

    os.chdir(old_path)

def createExperimentConfig(experiment_config):
    if not (root == os.getcwd()):

        if(root == os.path.dirname(os.getcwd())):
            if not (experiment_config_file in list_children()):
                with open(experiment_config_file, "w") as config_file:
                    experiment_config.write(config_file)

        elif not (experiment_config_file in list_children()):
            target = os.path.join(os.getcwd(), experiment_config_file)
            parent = os.path.dirname(os.getcwd())
            file_in_parent = os.path.join(parent, experiment_config_file)
            shutil.copyfile(file_in_parent, target)

    

def changeExperimentConfig(experiment_config):
    if not (root == os.getcwd()):
        with open(experiment_config_file, "w") as config_file:
            experiment_config.write(config_file)


def createDirectory(name):
    if not (name in list_children()):
        os.mkdir(name)

def deleteFile(name):
    remove_path = os.path.join(os.getcwd(), name)
    os.remove(remove_path)

def deleteDirectory(name):
    remove_path = os.path.join(os.getcwd(), name)
    shutil.rmtree(remove_path)
    
#notwendig?
def delete(name):
    if (name in list_children()):
        if('.' in name):
            deleteFile(name)
        else:
            deleteDirectory(name)
    return None