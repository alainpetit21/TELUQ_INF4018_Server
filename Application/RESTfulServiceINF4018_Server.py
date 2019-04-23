# ======================================================================================================================
# importing external modules
import cherrypy
import os


@cherrypy.expose
class RESTfulServiceINF4018_Server(object):
    """
    Class MyCherryPyRestService Description :
        Main Exposure of our API.
    Class Attributes :
    """

    @cherrypy.tools.accept(media='text/xml')
    def POST(self, userID, time):
        """ POST Description : (public visibility) :
            Unused, reserved for future usage. In a REST-ful API, this function gets call for each HTTP POST request
            (usually Upating the Service).

        Parameters :
        """
        strDataXML = cherrypy.request.body.read()

        #Simply save the received Xml string as per received for the user and the time of transmition
        with open(os.getcwd() + "/SavedSessions/{}-{}.xml".format(userID, time), "wb") as file:
            file.write(strDataXML)

        return "POST"

    def GET(self):
        """ GET Description : (public visibility) :
            Unused, reserved for future usage. In a REST-ful API, this function gets call for each HTTP GET request
            (usually Reading from the Service).

        Parameters :
        """
        return "GET"

    def PUT(self):
        """ PUT Description : (public visibility) :
            Unused, reserved for future usage. In a REST-ful API, this function gets call for each HTTP PUT request
            (usually Creating an entry into the Service).

        Parameters :
        """
        return "PUT"

    def DELETE(self):
        """ DELETE Description : (public visibility) :
            Unused, reserved for future usage. In a REST-ful API, this function gets call for each HTTP DELETE request
            (usually removing an entry from the Service).

        Parameters :
        """
        return "DELETE"