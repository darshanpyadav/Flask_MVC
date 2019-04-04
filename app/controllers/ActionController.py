from . import Controller
from flask import request


class ActionController(Controller):
    def sandbox_mount_failed(self):
        # get the action script from database
        script_path = self._script_dir + "/hello.py"
        script = "python " + script_path

        # convert the request to pass it as command line arguments to scripts
        args = self.command_with_args(request.args)

        # execute the command with arguments
        command = script + " " + args
        result = self.run_command(command)
        if result["stderr"]:
            pass

        return self.json_response(str(result))

