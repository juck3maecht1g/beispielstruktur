from GlobalConfigHandler import createGConfig, get_users, set_user, get_available_robots, get_user
from ExperimentConfigHandler import set_gripper, set_recording
from ExperimentManager import create_experiment
from PcDataHandler import navigate_to_parent

createGConfig()
original_user = get_user()
for user in get_users():
    create_experiment(user)
    set_user(user)
    set_gripper(get_available_robots())
    set_recording(get_available_robots())
    navigate_to_parent()
set_user(original_user)











