"""
Module for WebAppINF4018_Server class. 2 classes in this module : WebAppINF4018_Server, RESTServiceINF4018_Server
------------------------------------------------------------------------------------------------------------------------
"""
# ======================================================================================================================
# importing external modules
import cherrypy
import os
import xml.dom.minidom

# ======================================================================================================================
# importing library modules
from CrossCuttingConcerns.WebApp import WebApp, CherryPyExposure
from Presentation.WebAppINF4018_Server_CherryPyExposure import WebAppINF4018_Server_CherryPyExposure

# ======================================================================================================================
# importing internal modules
from Domain.DomainFacade import DomainFacade


@cherrypy.expose
class RESTServiceINF4018_Server(object):
    """
    Class MyCherryPyRestService Description :
        Unused for now, reserved for future support.
    Class Attributes :
    """

    def __init__(self):
        print ("In constructor")

    @cherrypy.tools.accept(media='text/xml')
    def POST(self, userID, time):
        """ POST Description : (public visibility) :
            Unused, reserved for future usage. In a REST-ful API, this function gets call for each HTTP POST request
            (usually Upating the Service).

        Parameters :
        """
        strCWD = os.getcwd()
        strData = cherrypy.request.body.read()
        print(strData)


        with open(strCWD + "/SavedSessions/{}-{}.xml".format(userID, time), "wb") as f:
            f.write(strData)

        return "POST"


    def GET(self):
        """ GET Description : (public visibility) :
            Unused, reserved for future usage. In a REST-ful API, this function gets call for each HTTP GET request
            (usually Reading from the Service).

        Parameters :
        """
        return "GET"

    def PUT(self, strXML):
        """ PUT Description : (public visibility) :
            Unused, reserved for future usage. In a REST-ful API, this function gets call for each HTTP PUT request
            (usually Creating an entry into the Service).

        Parameters :
        """
        strID = cherrypy.session.id
        strXML = strXML

        return "PUT"

    def DELETE(self):
        """ DELETE Description : (public visibility) :
            Unused, reserved for future usage. In a REST-ful API, this function gets call for each HTTP DELETE request
            (usually removing an entry from the Service).

        Parameters :
        """
        return "DELETE"


class WebAppINF4018_Server(WebApp):
    """
    Class WebAppINF4018_Server Description :
        The purpose of this class is to be the main WebApp. It will manage the specificity based on Cherrypy.

    Class Attributes :
        dic_SubAppThread: dict : a python dictionary that will countain all required information about sub-App
        (see EntryPluginWebAppInstance)

        idx_my_model: DomainFacade : Unused reserved for future usages.
    """

    def __init__(self):
        """ __init__ Description : (public visibility) :
            Constructor methods that will create this object. I does not do a lot but, overload the BaseClass
            construction call and initialization the class attributes for this instance.
        """
        super().__init__(p_str_thread_name="AppNakatomiPlaza", obj_webapp_exposure=WebAppINF4018_Server_CherryPyExposure(RESTServiceINF4018_Server()))

        self.idx_my_domain = None


    def load(self):
        """ load Description : (public visibility) :
            Method that is called directly after the creation of the object. Its purpose is to do all loading that is
            beside initial initialization.
        """
        self.idx_my_domain = self.register_model(DomainFacade())
