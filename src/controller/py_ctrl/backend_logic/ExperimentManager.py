from ExperimentConfigHandler import createExperimentConfig
from PcDataHandler import createDirectory, navigate_to_child


def start_logging():
    return 0

def stop_logging():
    return 0

def abort_logging():
    return 0

def save_logging():
    return 0

def build_scene(robotList):
    return 0

def create_experiment(name):
    createDirectory(name)
    navigate_to_child(name)
    createExperimentConfig()
