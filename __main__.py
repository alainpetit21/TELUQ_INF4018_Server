# ======================================================================================================================
# __main__.py : entry point script for this example

# ======================================================================================================================
# importing internal modules
from Application.WebAppINF4018_Server import WebAppINF4018_Server
from Presentation.CherryPyExposureINF4018_Server import CherryPyExposureINF4018_Server
from Application.RESTfulServiceINF4018_Server import RESTfulServiceINF4018_Server


if __name__ == "__main__":
    print("Hello Python World")

    objRESTfulAPI = RESTfulServiceINF4018_Server()
    objCPExposure = CherryPyExposureINF4018_Server(objRESTfulAPI)
    obj_app = WebAppINF4018_Server(objCPExposure)

    obj_app.load()
    obj_app.main()
