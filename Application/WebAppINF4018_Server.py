"""
Module for WebAppINF4018_Server class. 1 classes in this module : WebAppINF4018_Server
------------------------------------------------------------------------------------------------------------------------
"""

# ======================================================================================================================
# importing library modules
from CrossCuttingConcerns.WebApp import WebApp

# ======================================================================================================================
# importing internal modules




class WebAppINF4018_Server(WebApp):
    """
    Class WebAppINF4018_Server Description :
        The purpose of this class is to be the main WebApp. It will manage the specificity based on Cherrypy.

    Class Attributes :
        dic_SubAppThread: dict : a python dictionary that will countain all required information about sub-App
        (see EntryPluginWebAppInstance)

        idx_my_model: DomainFacade : Unused reserved for future usages.
    """

    def __init__(self, objExposure):
        """ __init__ Description : (public visibility) :
            Constructor methods that will create this object. I does not do a lot but, overload the BaseClass
            construction call and initialization the class attributes for this instance.
        """
        super().__init__(p_str_thread_name="WebAppINF4018_Server", obj_webapp_exposure=objExposure)


    def load(self):
        """ load Description : (public visibility) :
            Method that is called directly after the creation of the object. Its purpose is to do all loading that is
            beside initial initialization.
        """
        pass
