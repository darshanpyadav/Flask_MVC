from flask.views import View
from flask import current_app as app
from flask import jsonify


class Controller(View):
    def __init__(self, action_name):
        super(Controller, self).__init__()

        self.__action_name = action_name
        self._app = app

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
