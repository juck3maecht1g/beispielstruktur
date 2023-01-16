
import sys
import os
from .backend_logic.__init__ import app
import json
from .backend_logic.ExperimentManager import *
from flask import request
# from backend_logic.ExperimentManager import *


@app.route("/commands")
def members():
    data = {'members': 'M1'}
    return data


@app.route("/about")
def about():
    return "<h1 style='color: red'>About</h1>"


@app.route("/post-data", methods=['POST'])
def post_data():
    data = request.get_json()
    if data == 'abc':
        return 'Done', 201

    with open('testing.txt', 'w') as f:
        f.write(data)

    return 'Done', 201


@app.route("/reset-cmd", methods=['POST'])
def reset_cmd():
    data = request.get_json()
    if data == 'reset scene':
        reset_scene()
        return 'Done', 201
    return 'wrong', 201


@app.route("/save_position-cmd", methods=['POST'])
def save_position_cmd():
    data = request.get_json()
    if data == 'save position':
        save_position()
        return 'Done', 201
    return 'wrong', 201


@app.route("/gripper-cmd", methods=['POST'])
def gripper_cmd():
    data = request.get_json()
    if data == 'open':
        open_gripper()
        return 'Done', 201
    return 'wrong', 201


@app.route("/move-cmd", methods=['POST'])
def move_cmd():
    data = request.get_json()
    if data == 'move':
        move_robot()
        return 'Done', 201
    return 'wrong', 201


@app.route("/start-cmd", methods=['POST'])
def start_cmd():
    data = request.get_json()
    if data == 'start':
        start_logging()
        return 'Done', 201
    return 'wrong', 201


@app.route("/gripper-info")
def gripper_info():
    data = json.dumps(get_gripper())
    return data


@app.route("/start-info")
def start_info():
    data = json.dumps(get_experiment_name())
    return data
