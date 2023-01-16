from __init__ import app
import json

class Test:

    @staticmethod
    @app.route("/about")
    def about():
        return json.dumps("afdnjkasdl")
