"""
Module for CherryPyExposureINF4018_Server class. 1 vclasses in this module : CherryPyExposureINF4018_Server
------------------------------------------------------------------------------------------------------------------------
"""

# ======================================================================================================================
# importing external modules
import cherrypy

# ======================================================================================================================
# importing library modules
from CrossCuttingConcerns.WebApp import CherryPyExposure


class CherryPyExposureINF4018_Server(CherryPyExposure):
    """
    Class WebAppINF4018_Server_CherryPyExposure Description :
        The purpose of this class is to be the "main" exposure object for the whole WebApp and either display the main
        page or dispatch to sub-App.
    Class Attributes :
        dic_SubCherryPyExposure:dict : Python dictionary that will. The WebApp.load() will update this value with the
        proper exposur instance for each PluginWebApp.

        strWebExposureName:str : String that will be the tag that will be used to access this plugin app from the
            browser.
    """

    def __init__(self, pObjRESTfulService=None):
        """ __init__ Description : (public visibility) :
            Constructor of the WebAppINF4018_Server_CherryPyExposure object.

        Parameters :
            :param pObjRESTfulService: defaulted to none. If the WebApp is using a REST service in addition of the
            WebApp, this parameter will countain an object of a class that define the POST, GET, PUT and DELETE methods.
        """
        super().__init__(pObjRESTfulService)

    @cherrypy.expose
    def index(self):
        """ index Description : (public visibility) :
            Constructor of the MyCherryPyExposure object.

        Parameters :
            :return The direct output to the browser (i.e. the html code) wither directly hardcoded here or as a file
            with the open() function.
        """
        return """
                <html>
                <body>
        
                <h2>Welcome to WebAppINF4018_Server_CherryPyExposure</h2>
        
                </body>
                </html>
        """
