from GlobalConfigHandler import createGlobalConfig, get_user, get_users, set_user, set_language
from ExperimentManager import create_experiment
from ExperimentConfigHandler import get_variables
from PcDataHandler import navigate_to_parent, get_cwd

createGlobalConfig()

original_user = get_user()
for user in get_users():
    create_experiment(user)
    navigate_to_parent()
print(get_cwd())
print(get_variables())
set_user(original_user)










