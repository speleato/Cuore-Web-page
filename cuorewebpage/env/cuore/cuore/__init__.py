from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
#     def add_render_globals(event):
#     	request = event['request']
#     	userID = authenticated_userid(request)
#     	event.update(dict(
#     		USER_ID=userID))
        
    
    config = Configurator(settings=settings)
#     config.add_subscriber(add_renderer_globals, BeforeRender)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
