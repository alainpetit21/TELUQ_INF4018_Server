# ======================================================================================================================
# WebApp.py :

# ======================================================================================================================
# importing external modules
import cherrypy
import os, os.path
import time

# ======================================================================================================================
# importing internal modules
from firework.system.App import App
from firework.system.Thread import Thread


class CherryPyExposure(Thread):
    # ==================================================================================================================
    # Class attributes
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd() + "/Web")
        },
        '/rest_service': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/public': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }

    # ==================================================================================================================
    # __init__ : Constructor for a new app object
    def __init__(self, p_obj_rest_service=None):
        super().__init__("Thread-WebAppCherryPy")
        self.rest_service = p_obj_rest_service

    def load(self):
        cherrypy.config.update({'server.socket_host': '192.168.0.133',
                                'server.socket_port': 8081,
                                'request.show_tracebacks': False
                                })

    def on_manage(self, param1= None):
        cherrypy.quickstart(self, '/', self.conf)   # this call is blocking (e.g. when we go to the next line it mean that the server has ended)
        self.is_running = False                     # This is why we need to stop the thread after the server has ended


# ======================================================================================================================
# class WebApp :
class WebApp(App):
    thread_web_exposure = None

    # ==================================================================================================================
    # Class Methods
    # ==================================================================================================================
    # __init__ : Constructor for a new app object, basically redirecting to super class the construction
    def __init__(self, p_str_thread_name: str, obj_webapp_exposure: CherryPyExposure):
        self.thread_web_exposure = obj_webapp_exposure
        super().__init__(p_str_thread_name)

        self.thread_web_exposure.start()
        time.sleep(0.1)
