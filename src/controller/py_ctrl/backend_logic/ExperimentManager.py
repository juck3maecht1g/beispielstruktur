from .ExperimentConfigHandler import *
from .PcDataHandler import createDirectory, navigate_to_child, navigate_to_parent

def reset_scene():
    return 0
    

def save_position():
    return


def open_gripper():
    return


def move_robot():
    return


def start_logging():
    return 0


def stop_logging():
    return 0


def abort_logging():
    return 0


def save_logging():
    return 0


def get_gripper():
    return ['test', '2']


def get_experiment_name():
    return "test"


def build_scene(robotList):
    return 0


def create_experiment(name):
    createDirectory(name)
    navigate_to_child(name)
    createEConfig()
