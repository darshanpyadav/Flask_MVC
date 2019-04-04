from . import Controller
from flask import request


class ActionController(Controller):
    def index(self):
        # get the action script from database
        script = "python hello.py"

        # convert the request to pass it as command line arguments to scripts
        args = self.command_with_args(request.args)

        # execute the command with arguments
        command = script + " " + args
        # command = "pwd"
        result = self.run_command(command)
        if result["stderr"]:
            pass

        return self.json_response(str(result))

