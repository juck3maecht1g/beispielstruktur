from app import app
import json
from flask import request


@app.route("/")
def members(): 
    data = {'members': 'M1'}
    return data

@app.route("/about")
def about():
    return "<h1 style='color: red'>About</h1>"


@app.route("/post-data", methods=['POST'])
def post_data():
    data = request.get_json()
    with open('testing.txt', 'w') as f:
        f.write(data)
        
    return 'Done', 201


    
