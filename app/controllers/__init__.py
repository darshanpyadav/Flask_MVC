from flask.views import View
from flask import current_app as app
from flask import jsonify
from subprocess import Popen, PIPE
import shlex


class Controller(View):
    def __init__(self, action_name):
        super(Controller, self).__init__()

        self.__action_name = action_name
        self._app = app
        self._script_dir = app.config["SCRIPTS_DIR"]

    def dispatch_request(self, *args, **kwargs):
        action = getattr(self, self.__action_name, None)
        if action is None:
            raise Exception('action_name', 'Action {0} not found'.format(self.__action_name))
        return action(*args, **kwargs)

    @staticmethod
    def json_response(data):
        message = {
            'success': True,
            'result': data
        }
        resp = jsonify(message)
        resp.status_code = 200

        return resp

    @staticmethod
    def command_with_args(data):
        args = ""
        for k, v in data.items():
            if k == "ERROR":
                continue
            args += "--" + k + " " + v + " "
        return args.rstrip()

    @staticmethod
    def run_command(command, wait=False):
        result = {}
        try:
            if wait:
                p = Popen([command], stdout=PIPE)
                p.wait()
            else:
                p = Popen(shlex.split(command), stdout=PIPE, stderr=PIPE)

            (stdout, stderr) = p.communicate()

            result["exit_code"] = p.returncode
            result["stdout"] = stdout.decode("utf-8")
            result["stderr"] = stderr.decode("utf-8")
            result["command"] = command

        except Exception as e:
            result["stderr"] = e

        return result
