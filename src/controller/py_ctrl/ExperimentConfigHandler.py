from configparser import ConfigParser

from PcDataHandler import changeExperimentConfig, createExperimentConfig

experiment_config = ConfigParser()

experiment_config["DEFAULT"] = {
    "gripper": [],
    "recording": []
}

def createEConfig():
    createExperimentConfig(experiment_config)

def get_gripper():
    return experiment_config.get("DEFAULT", "gripper")

def set_gripper(new_gripper):
        experiment_config.set("DEFAULT", "gripper" , new_gripper)
        changeExperimentConfig(experiment_config)

def get_recording():
    return experiment_config.get("DEFAULT", "recording")

def set_recording(new_recording):
        experiment_config.set("DEFAULT", "recording" , new_recording)
        changeExperimentConfig(experiment_config)

