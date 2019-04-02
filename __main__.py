# ======================================================================================================================
# __main__.py : entry point script for this example

# ======================================================================================================================
# importing internal modules
from Application.WebAppINF4018_Server import WebAppINF4018_Server


if __name__ == "__main__":
    print("Hello Python World")

    obj_app = WebAppINF4018_Server()
    obj_app.load()
    obj_app.main()
