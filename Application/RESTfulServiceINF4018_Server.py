"""
Module for RESTfulServiceINF4018_Server class. 1 classes in this module : RESTfulServiceINF4018_Server
------------------------------------------------------------------------------------------------------------------------
"""
# ======================================================================================================================
# importing external modules
import cherrypy
import os


@cherrypy.expose
class RESTfulServiceINF4018_Server:
    """
    Class RESTfulServiceINF4018_Server Description :
        Main Exposure of our API.

    Class Attributes (Static attributes):
        None

    Instance Attributes :
        None
    """

    # ==================================================================================================================
    @cherrypy.tools.accept(media='text/xml')
    def POST(self, userID, time):
        """ POST Description : (public visibility) :
            Post exposure of our Server. This is where we received the XML Stream from the client.
            In a REST-ful API, this function gets call for each HTTP POST request
            (usually Upating the Service).

        Parameters :
        """

        strDataXML = cherrypy.request.body.read()

        #Simply save the received Xml string as per received for the user and the time of transmition
        with open(os.getcwd() + "/SavedSessions/{}-{}.xml".format(userID, time), "wb") as file:
            file.write(strDataXML)

        return "POST"
