# Register all the routes here
def register_routes(app):
    # format
    # add_route(app, '='<route_name>', 'Controller_name', 'url', 'methods = []')

    from .controllers.ActionController import ActionController
    add_route(app, 'index', '/', ActionController, 'index', methods=['GET'])


def add_route(app, route_name, pattern, controller, action, **kwargs):
    app.add_url_rule(pattern, view_func=controller.as_view(route_name, action), **kwargs)
