from . import Controller
from flask import request


class ActionController(Controller):
    def index(self):
        return self.json_response(request.args.get("name"))

