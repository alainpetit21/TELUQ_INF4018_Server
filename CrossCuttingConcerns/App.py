# ======================================================================================================================
# importing external modules
import time
import logging


# ======================================================================================================================
# class App : Implement generic method for a application object. The only thing that remains on client side are client
#             specfic application logic / orchestration / etc.
class App(object):
    # ==================================================================================================================
    # Class attributes
    objInstance = None

    # List Countainers to countains all registered model and views. In Most case only 1 of each will be used. But we
    # support more
    lst_obj_model = None

    # Generic attributes, used internally
    is_running = False
    str_name = None

    # Support for multi-threaded, list of launched Thread
    lst_sub_thread = None

    # ==================================================================================================================
    # Class Methods
    # ==================================================================================================================
    # __init__ : Constructor methode that manage the Singleton DP and generic constructor management for this object
    def __init__(self, p_str_name, debug_level = 3):
        App.objInstance = self   # TODO eventually create a real singleton

        self.str_name = p_str_name

        # List Countainers to countains all registered model and views
        self.lst_obj_model = []

        # Support for multi-threaded, list of launched Thread
        self.lst_sub_thread = []

        # Set basic logging output format
        if debug_level == 0:    logging.basicConfig(level=logging.NOTSET, format='[%(levelname)s] (%(threadName)-10s) %(message)s')
        if debug_level == 1:    logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')
        if debug_level == 2:    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-10s) %(message)s')
        if debug_level == 3:    logging.basicConfig(level=logging.WARNING, format='[%(levelname)s] (%(threadName)-10s) %(message)s')
        if debug_level == 4:    logging.basicConfig(level=logging.ERROR, format='[%(levelname)s] (%(threadName)-10s) %(message)s')
        if debug_level == 5:    logging.basicConfig(level=logging.CRITICAL, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

    # ==================================================================================================================
    # Methods implementation from IApp Interface

    # ==================================================================================================================
    # register_model : Method for adding a Model into the Model list countainer and create (future support) list of
    #                   message for this model
    def register_model(self, p_obj_model):
        self.lst_obj_model.append(p_obj_model)
        # self.ar_lst_msg_Model.append(self.obj_manager.Queue())
        return self.lst_obj_model.__len__() - 1

    # ==================================================================================================================
    # get_model : Method for getting a registered model object by its index
    def get_model(self, p_idx):
        return self.lst_obj_model[p_idx]

    # ==================================================================================================================
    # launch_thread : Public interface method for launching a system.Thread
    def launch_thread(self, p_obj_thread):
        self.lst_sub_thread.append(p_obj_thread)
        p_obj_thread.start()

    # ==================================================================================================================
    # Methods implementation from IRunnable Interface
    # ==================================================================================================================
    # main : Mostly for internal purposes only, shall contains the main loop
    def main(self, param1= None):
        self.is_running = True

        while self.is_running:
            logging.debug('Performing one loop')
            self.event_one_loop()
            time.sleep(0.1)

        # Ensure that no other thread are running
        logging.debug('About to quit, but first check if any other threads are running')
        other_thread_is_running= True
        while other_thread_is_running:
            other_thread_is_running = False

            for obj_thread in self.lst_sub_thread:
                if obj_thread.is_running:
                    logging.debug('Found a thread : {}'.format(obj_thread.str_name))
                    other_thread_is_running = True

                logging.debug('Trying to join : {}'.format(obj_thread.str_name))
                obj_thread.join()
            time.sleep(1)

    # ==================================================================================================================
    # event_one_loop : Mostly for internal purposes only, shall contain only one loop of the main loop
    def event_one_loop(self, param1= None):
        self.on_manage()

    # ==================================================================================================================
    # on_manage : Mostly for external client-side purposes only. Callback style that will be implemented beyond a level
    def on_manage(self, param1= None):
        pass

